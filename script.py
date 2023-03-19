import pandas as pd
import requests
from riotwatcher import LolWatcher, ApiError

api_key = ""

lol_watcher = LolWatcher(api_key)
my_region = 'euw1'

latest = lol_watcher.data_dragon.versions_for_region(my_region)['n']['champion']
static_champ_list = lol_watcher.data_dragon.champions(latest, False, 'en_US')

me = lol_watcher.summoner.by_name(my_region, 'otto from asylum')
print(me)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

api_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/otto%20from%20asylum"
s = requests.Session()
s.headers.update({'X-Riot-Token': api_key})
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
    api_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    api_url = api_url + "?api_key=" + api_key
    resp = requests.get(api_url)
    player_info = resp.json()
    return player_info


def get_summoner_name(summoner_info):
    return summoner_info["name"]


def get_summoner_level(summoner_info):
    return summoner_info["summonerLevel"]


def get_summoner_id(summoner_info):
    return summoner_info["id"]


def get_account_id(summoner_info):
    return summoner_info["accountId"]


x = get_summoner_info("otto from asylum")
summoner_info = get_summoner_info("otto from asylum")
summoner_name = get_summoner_name(summoner_info)
summoner_level = get_summoner_level(summoner_info)

print(summoner_name)
print(summoner_level)

participants = []
for match in lol_watcher.match.matchlist_by_account(my_region, get_account_id(summoner_info)):
    match_detail = lol_watcher.match.by_id(my_region, match['gameId'])
    for row in match_detail['participants']:
        participants_row = {}
        participants_row['champion'] = row['championId']
        participants_row['spell1'] = row['spell1Id']
        participants_row['spell2'] = row['spell2Id']
        participants_row['win'] = row['stats']['win']
        participants_row['kills'] = row['stats']['kills']
        participants_row['deaths'] = row['stats']['deaths']
        participants_row['assists'] = row['stats']['assists']
        participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        participants_row['goldEarned'] = row['stats']['goldEarned']
        participants_row['champLevel'] = row['stats']['champLevel']
        participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
        participants_row['item0'] = row['stats']['item0']
        participants_row['item1'] = row['stats']['item1']
        participants_row['item
