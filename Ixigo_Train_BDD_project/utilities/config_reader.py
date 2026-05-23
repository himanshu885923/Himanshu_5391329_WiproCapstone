import configparser


class ConfigReader:

    @staticmethod
    def get(key):

        config = configparser.ConfigParser()

        config.read("config/config.properties")

        return config["DEFAULT"][key]