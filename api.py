import requests
api_key = ""

api_url = " https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/otto%20from%20asylum"


requests.get(api_url)

api_url = api_url + "?api_key=" + api_key

resp = requests.get(api_url)

player_info = resp.json()
