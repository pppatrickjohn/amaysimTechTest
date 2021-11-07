import configparser

config = configparser.RawConfigParser()
config.read(".//config//config.ini")

class readConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('Common Data', 'baseURL')
        return url