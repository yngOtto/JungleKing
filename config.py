import configparser


def get_api_key(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    api_key = config['RIOT']['api_key']
    return api_key
