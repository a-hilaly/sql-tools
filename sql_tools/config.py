import os
import configparser
from .utils import CONFIG_DIRECTORY

def extract_settings(system, config, o=None):
    Config = configparser.ConfigParser()
    conf_dir = "{0}/{1}_conf.ini".format(CONFIG_DIRECTORY, system)
    Config.read(conf_dir)
    if o:
        ci = Config[config][o]
        return ci if (ci == '1') in '01' else ci
    data = dict(Config[config])
    for k in data.keys():
        if data[k] in '01':
            data[k] = (data[k] == '1')
    return data

def get_logs(system):
    if 'CI' in list(os.environ.keys()):
        ENV = os.environ['CI']
        LOGS = extract_settings(system, 'ci.logs')
    else:
        LOGS = extract_settings(system, 'logs')
    return LOGS
