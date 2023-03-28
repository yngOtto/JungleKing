import requests
from riotwatcher import LolWatcher, ApiError
import pandas as pd

lol_watcher = LolWatcher('')
my_region = 'euw1'

# Get the latest champion version and list of champions
latest = lol_watcher.data_dragon.versions_for_region(my_region)[
    'n']['champion']
static_champ_list = lol_watcher.data_dragon.champions(latest, False, 'en_US')

# Get summoner information
me = lol_watcher.summoner.by_name(my_region, 'otto from asylum')
print(me)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

# Set up the API URL and request headers
api_key = ""
api_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/otto%20from%20asylum"
s = requests.Session()
s.headers.update({'X-Riot-Token': api_key})

# Map the champion IDs to their names
champ_dict = {}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[row['key']] = row['id']

# Print the list of participants with champion names
for row in participants:
    print(str(row['champion']) + ' ' + champ_dict[str(row['champion'])])
    row['championName'] = champ_dict[str(row['champion'])]

# Convert lane and role information to a standardized format
df = pd.DataFrame(participants)
df['lane'] = df.apply(lambda row: get_lane(row['role'], row['lane']), axis=1)
print(df)

# Get summoner information using the Riot API
requests.get(api_url)
api_url = api_url + "?api_key=" + api_key
resp = requests.get(api_url)
player_info = resp.json()
summoner_name = player_info["name"]
summoner_level = player_info["summonerLevel"]
print(summoner_name)
print(summoner_level)

# Define functions for getting summoner information from the Riot API


def get_summoner_info(summoner_name):
    api_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/otto%20from%20asylum"
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


def get_account_id(summoner_name):
    account_id = player_info["accountId"]
    return account_id


# Get summoner information using the Riot API
summoner_info = get_summoner_info(summoner_name)
summoner_name = get_summoner_name(summoner_name)
summoner_level = get_summoner_level(summoner_name)
summoner_id = get_summoner_id(summoner_name)
account_id = get_account_id(summoner_name)
print(summoner_name)

# Get match history using the Riot API
api_url = "https: // euw1.api.
[...]
