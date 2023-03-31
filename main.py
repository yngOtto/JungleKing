import requests
from riotwatcher import LolWatcher, ApiError
import pandas as pd

# Initialize the API and region
api_key = ""
lol_watcher = LolWatcher(api_key)
region = 'euw1'

# Get the latest champion version and list of champions
latest_version = lol_watcher.data_dragon.versions_for_region(region)[
    'n']['champion']
champion_data = lol_watcher.data_dragon.champions(
    latest_version, False, 'en_US')

# Get summoner information
summoner_name = 'otto from asylum'
summoner_info = lol_watcher.summoner.by_name(region, summoner_name)
print(summoner_info)
ranked_stats = lol_watcher.league.by_summoner(region, summoner_info['id'])
print(ranked_stats)

# Map the champion IDs to their names
champ_dict = {}
for champ_key in champion_data['data']:
    row = champion_data['data'][champ_key]
    champ_dict[row['key']] = row['id']

# Print list of plyrs with champ names
participants = []
for row in participants:
    champ_id = str(row['champion'])
    champ_name = champ_dict.get(champ_id)
print(champ_id + ' ' + champ_name)
row['championName'] = champ_name

# Standarize lane and role info
df = pd.DataFrame(participants)
df['lane'] = df.apply(lambda row: get_lane(row['role'], row['lane']), axis=1)
print(df)

# Get summoner info using Riot API
api_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
s = requests.Session()
s.headers.update({'X-Riot-Token': api_key})
resp = s.get(api_url)
player_info = resp.json()
summoner_name = player_info["name"]
summoner_level = player_info["summonerLevel"]
print(summoner_name)
print(summoner_level)

# Defining functions to allow retreival of summoner info from Riot API


def get_summoner_info(summoner_name, region, api_key):
    api_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    s = requests.Session()
    s.headers.update({'X-Riot-Token': api_key})
    resp = s.get(api_url)
    player_info = resp.json()
    return player_info


def get_summoner_name(player_info):
    summoner_name = player_info["name"]
    return summoner_name


def get_summoner_level(player_info):
    summoner_level = player_info["summonerLevel"]
    return summoner_level


def get_summoner_id(player_info):
    summoner_id = player_info["id"]
    return summoner_id


def get_account_id(player_info):
    account_id = player_info["accountId"]
    return account_id


# Get summoner info via Riot API
summoner_info = get_summoner_info(summoner_name, region, api_key)
summoner_name = get_summoner_name(summoner_info)
summoner_level = get_summoner_level(summoner_info)
summoner_id = get_summoner_id(summoner_info)
account_id = get_account_id(summoner_info)
print(summoner_name)

# Get match history using Riot API
api_url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + account_id
api_url = api_url + "?api_key=" + api_key
resp = requests.get(api_url)
match_history = resp.json()
print(match_history)

# Get ranked stats using Riot API
api_url = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + summoner_id
api_url = api_url + "?api_key=" + api_key
resp = requests.get(api_url)
ranked_stats = resp.json()
print(ranked_stats)

# Function for getting match history of a summoner


def get_match_history(summoner_name):
    summoner_info = get_summoner_info(summoner_name)
    account_id = get_account_id(summoner_name)
    api_url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + account_id
    api_url = api_url + "?api_key=" + api_key
    resp = requests.get(api_url)
    match_history = resp.json()
    return match_history


# Get match history of a summoner
match_history = get_match_history(summoner_name)
print(match_history)
