from configparser import ConfigParser

config=ConfigParser()

with open("neatconfigparser.ini","w") as f:
    config.write(f)
