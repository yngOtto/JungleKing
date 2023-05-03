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

    # todo lisy:
    # - get_summoner_name()
    # - get_summoner_level()
    # - get_summoner_id()
    # - get_account_id()
    # - get_match_history()
    # - get_match_info_jungler()
    # - get_match_info()
    # - get_win_rate()
    # - get_kda()
    # - get_match_info_jungler()
    # - analyze_enemy_jungler_pathing()
