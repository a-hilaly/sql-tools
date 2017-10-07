import os
import configparser
from .utils import CONFIG_FULL_PATH


def extract_settings(config, o=None):
    #
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FULL_PATH)
    if o:
        return cfg[config][o]
    return dict(cfg[config])


def conflogs():
    try:
        ENV = os.environ['CI']
        LOGS = extract_settings('ci')
    except:
        LOGS = extract_settings('local')
    for k in LOGS.keys():
        if LOGS[k] in '01':
            LOGS[k] = (LOGS[k] == '1')
    return LOGS
