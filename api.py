import requests

from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('')

my_region = 'euw1'

me = lol_watcher.summoner.by_name(my_region, 'otto from asylum')
print(me)

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

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


def get_account_id(summoner_name):
    account_id = player_info["accountId"]
    return account_id


def get_summoner_info(summoner_name):
    api_url = " https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/otto%20from%20asylum"
    api_url = api_url + "?api_key=" + api_key
    resp = requests.get(api_url)
    player_info = resp.json()
    return player_info


x = get_summoner_info("otto from asylum")

getsummonername = get_summoner_name("otto from asylum")


try:
    response = lol_watcher.summoner.by_name(
        my_region, 'this_is_probably_not_anyones_summoner_name')
except ApiError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(
            err.response.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        raise


def api_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def league_request(summoner_id):
    url = 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{}?api_key={}'.format(
        summoner_id, api_key)
    return api_request(url)
