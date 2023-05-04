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
        resp = s.get(api_url)
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

    # todo list:
    # - get_match_info_jungler()
    # - get_win_rate()
    # - get_kda()
    # - get_match_info_jungler()
    # - analyze_enemy_jungler_pathing()
