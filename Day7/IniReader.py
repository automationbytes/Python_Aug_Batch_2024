import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def readConfig(header,key):
    return config.get(header,key)

print(readConfig('google',"url"))
print(readConfig('facebook',"url"))
