import requests
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import configparser
from config import get_api_key
from riot_api import RiotAPI

# create a configuration parser object
config = configparser.ConfigParser()

# read config file
config.read('config.ini')

# get the API key from the config file
api_key = config['RIOT']['api_key']

# use API key in the api call
params = {'api_key': api_key}
