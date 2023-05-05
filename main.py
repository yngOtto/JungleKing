import requests
from riotwatcher import LolWatcher, ApiError
from config import get_api_key
from riot_api import RiotAPI


def main():
    # get API key from config.ini
    api_key = get_api_key()

    # Create a RiotAPI instance
    riot_api = RiotAPI(api_key, 'euw1')

    # Use the RiotAPI instance to perform the desired tasks
    summoner_name = 'otto from asylum'
    summoner_info = riot_api.get_summoner_info(summoner_name)
    print(summoner_info)

    # Add other tasks and function calls here (todo)
    # - Get summoner's match history
    # - Analyze enemy jungler's pathing
    # - Get win rate of a summoner in ranked soloQ games


if __name__ == "__main__":
    main()
