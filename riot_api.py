import requests
from riotwatcher import LolWatcher


class RiotAPI:
    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = region
        self.lol_watcher = LolWatcher(api_key)

    def get_summoner_info(self, summoner_name):
        api_url = f"https://{self.region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
        s = requests.Session()
        s.headers.update({'X-Riot-Token': self.api_key})
        try:
            resp = s.get(api_url)
            resp.raise_for_status()  # produce an HTTPError if response was unsuccessful
        except requests.exceptions.RequestException as e:
            print(f"Request to Riot API failed: {e}")
            return None
        player_info = resp.json()
        return player_info

    def get_summoner_name(self, summoner_name):
        player_info = self.get_summoner_info(summoner_name)
        return player_info['name']

    def get_summoner_level(self, summoner_name):
        player_info = self.get_summoner_info(summoner_name)
        return player_info['summonerLevel']

    def get_summoner_id(self, summoner_name):
        player_info = self.get_summoner_info(summoner_name)
        return player_info['id']

    def get_account_id(self, summoner_name):
        player_info = self.get_summoner_info(summoner_name)
        return player_info['accountId']

    def get_match_history(self, summoner_name):
        account_id = self.get_account_id(summoner_name)
        api_url = f"https://{self.region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}"
        s = requests.Session()
        s.headers.update({'X-Riot-Token': self.api_key})
        resp = s.get(api_url)
        match_history = resp.json()
        return match_history

    def get_match_info(self, match_id):
        api_url = f"https://{self.region}.api.riotgames.com/lol/match/v4/matches/{match_id}"
        s = requests.Session()
        s.headers.update({'X-Riot-Token': self.api_key})
        resp = s.get(api_url)
        match_info = resp.json()
        return match_info

    def get_match_info_jungler(self, match_id):
        match_info = self.get_match_info(match_id)
        return match_info['info']['participants'][0]

    def get_win_rate(self, summoner_name):
        match_history = self.get_match_history(summoner_name)
        wins = 0
        losses = 0
        for match in match_history['matches']:
            match_info = self.get_match_info(match['gameId'])
            if match_info['info']['participants'][0]['win']:
                wins += 1
            else:
                losses += 1
        return wins / (wins + losses)

    def get_kda(self, summoner_name):
        match_history = self.get_match_history(summoner_name)
        kills = 0
        deaths = 0
        assists = 0
        for match in match_history['matches']:
            match_info = self.get_match_info(match['gameId'])
            kills += match_info['info']['participants'][0]['kills']
            deaths += match_info['info']['participants'][0]['deaths']
            assists += match_info['info']['participants'][0]['assists']
        return kills, deaths, assists

    def get_kda_ratio(self, summoner_name):
        kills, deaths, assists = self.get_kda(summoner_name)
        return (kills + assists) / deaths

    def get_cs(self, summoner_name):
        match_history = self.get_match_history(summoner_name)
        cs = 0
        for match in match_history['matches']:
            match_info = self.get_match_info(match['gameId'])
            cs += match_info['info']['participants'][0]['totalMinionsKilled']
        return cs

    def get_cs_per_min(self, summoner_name):
        match_history = self.get_match_history(summoner_name)
        cs = 0
        for match in match_history['matches']:
            match_info = self.get_match_info(match['gameId'])
            cs += match_info['info']['participants'][0]['totalMinionsKilled']
        return cs / len(match_history['matches'])

    def get_gold(self, summoner_name):
        match_history = self.get_match_history(summoner_name)
        gold = 0
        for match in match_history['matches']:
            match_info = self.get_match_info(match['gameId'])
            gold += match_info['info']['participants'][0]['goldEarned']
        return gold

    def get_gold_per_min(self, summoner_name):
        match_history = self.get_match_history(summoner_name)
        gold = 0
        for match in match_history['matches']:
            match_info = self.get_match_info(match['gameId'])
            gold += match_info['info']['participants'][0]['goldEarned']
        return gold / len(match_history['matches'])

    def analyze_enemy_jungler_pathing(self, summoner_name):
        account_id = self.get_account_id(summoner_name)
        jungler_matches = self.get_jungler_matches(account_id)

        for match_id in jungler_matches:
            match_info = self.get_match_info(match_id)
            enemy_jungler_id = self.get_enemy_jungler_id(match_info)
            pathing = self.get_enemy_jungler_pathing(
                match_info, enemy_jungler_id)
            self.print_pathing_results(match_id, pathing)

    def get_jungler_matches(self, account_id):
        api_url = f"https://{self.region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}"
        resp = requests.get(api_url, headers={'X-Riot-Token': self.api_key})
        match_history = resp.json()

        return [match['gameId'] for match in match_history['matches'] if match['queue'] == 420 and match['role'] == 'JUNGLE']

    def get_match_info(self, match_id):
        api_url = f"https://{self.region}.api.riotgames.com/lol/match/v4/matches/{match_id}"
        resp = requests.get(api_url, headers={'X-Riot-Token': self.api_key})
        return resp.json()

    def get_enemy_jungler_id(self, match_info):
        enemy_team = [participant for participant in match_info['participants']
                      if participant['teamId'] != match_info['participantIdentities'][0]['participantId']]
        enemy_jungler = [participant for participant in enemy_team if participant['timeline']
                         ['role'] == 'NONE' and participant['timeline']['lane'] == 'JUNGLE'][0]
        return enemy_jungler['participantId']

    def get_enemy_jungler_pathing(self, match_info, enemy_jungler_id):
        return [(event['position']['x'], event['position']['y']) for frame in match_info['timeline']['frames'] for event in frame['events'] if event['type'] == 'CHAMPION_KILL' and event['killerId'] == enemy_jungler_id]

    def print_pathing_results(self, match_id, pathing):
        if len(pathing) > 0:
            print(f"Enemy jungler pathing in match {match_id}:")
            for i, point in enumerate(pathing):
                print(f"  {i+1}. {point}")
            print("")

            # Analyze the pathing to find weaknesses
            if len(pathing) >= 2:
                start = pathing[0]
                end = pathing[-1]
                mid = pathing[len(pathing)//2]
                print(f"The following weaknesses can be exploited:")
                self.print_weaknesses(start, mid, end)
            else:
                print("Not enough data to analyze pathing!")
        else:
            print(f"No enemy jungler pathing found in match {match_id}.")

    def print_weaknesses(self, start, mid, end):
        if abs(start[0] - end[0]) > abs(start[1] - end[1]):
            # Enemy jungler traveled more horizontally than vertically
            if mid[1] < start[1]:
                print("- Invade their bottom-side jungle early")
            elif mid[1] > start[1]:
                print("- Invade their top-side jungle early")
        else:
            # Enemy jungler traveled more vertically than horizontally
            if mid[0] < start[0]:
                print("- Invade their right-side jungle early")
            elif mid[0] > start[0]:
                print("- Invade their left-side jungle early")
