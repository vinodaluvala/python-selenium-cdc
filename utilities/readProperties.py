import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig:
    @staticmethod
    def getappURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getfooterLocation():
        location = config.get('common info', 'footerLocation')
        return location

    @staticmethod
    def getfooterSize():
        size = config.get('common info', 'footerSize')
        return size
