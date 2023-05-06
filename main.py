import requests
from riotwatcher import LolWatcher, ApiError
from config import get_api_key
from riot_api import RiotAPI
# from data_processing import analyze_pathing_weaknesses


def main():
    # get API key from config.ini
    api_key = get_api_key()

    # Create a RiotAPI instance
    riot_api = RiotAPI(api_key, 'euw1')

    # Use the RiotAPI instance to perform the desired tasks
    summoner_name = 'palestineboy69'
    summoner_info = riot_api.get_summoner_info(summoner_name)
    summoner_winrate = riot_api.get_win_rate(summoner_name)
    print((summoner_winrate))
    print(summoner_info)

    # Add other tasks and function calls here (todo)
    # - Get summoner's match history
    # - Get summoner's ranked stats
    # - Analyze enemy jungler's pathing
    # - Get win rate of a summoner in ranked soloQ games
    # - Get win rate of a champion in ranked soloQ games


if __name__ == "__main__":
    main()
