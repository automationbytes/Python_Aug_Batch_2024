import configparser
config = configparser.ConfigParser()
config.read("config.properties")
print(config['google']['url'])
print(config['selenium']['timeouts'])
# print(config['url'])