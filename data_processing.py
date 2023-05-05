import pandas as pd
import requests


def get_lane(role, lane):
    return lane if lane != 'NONE' else role
