import os
from sql_tools.utils import PROJECT_DIRECTORY

api_path = "{0}/{1}".format(PROJECT_DIRECTORY, "sql_tools_api.py")

class SQLtools_API(object):

    def __init__(self, sys, path):
        pass

    def command_server(self, command):
        """
        0 : Start
        1 : Stop
        2 : Reboot
        """
        pass

    @classmethod
    def RunServer(cls):
        pass

    @classmethod
    def StopServer(cls):
        pass

    @classmethod
    def RestartServer(cls):
        pass
