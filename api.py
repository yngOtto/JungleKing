import requests
api_key = ""

api_url = " https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/otto%20from%20asylum"


requests.get(api_url)

api_url = api_url + "?api_key=" + api_key

resp = requests.get(api_url)

player_info = resp.json()

print(player_info)

summoner_name = player_info["name"]

summoner_level = player_info["summonerLevel"]

print(summoner_name)

print(summoner_level)

json_data = resp.json()


def get_summoner_info(summoner_name):
    api_url = " https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/otto%20from%20asylum"
    api_url = api_url + "?api_key=" + api_key
    resp = requests.get(api_url)
    player_info = resp.json()
    return player_info


def get_summoner_name(summoner_name):
    summoner_name = player_info["name"]
    return summoner_name


def get_summoner_level(summoner_name):
    summoner_level = player_info["summonerLevel"]
    return summoner_level


def get_summoner_id(summoner_name):
    summoner_id = player_info["id"]
    return summoner_id
