import configparser
import os

#https://docs.python.org/3/library/configparser.html
CONFIG = configparser.ConfigParser()

def loadDefaultConfig():
    dirs = {
        "fme": "C:\\Program Files\\FME\\fme.exe",
        "workspace": ".\\",
        "output": ".\\convertedData",
        "mc": "{0}{1}\\AppData\\Roaming\\.minecraft\\saves".format(os.getenv("HOMEDRIVE"), os.getenv("HOMEPATH"))
    }
    CONFIG["DIRS"] = dirs
def loadConfigFile(path):
    CONFIG.read(path)
    print(os.path.abspath(path))
    print(CONFIG.sections())
def saveConfigFile(path):
    with open(path, "w") as file:
        CONFIG.write(file)



if os.path.isfile("config.ini"):
    loadConfigFile("config.ini")
else:
    loadDefaultConfig()
    saveConfigFile("config.ini")

print(CONFIG.sections())
FME_PATH = CONFIG["DIRS"]["fme"]
WORKSPACE_RELATIVE_PATH = CONFIG["DIRS"]["workspace"]
OUTPUT_DIRECTORY_RELATIVE_PATH = CONFIG["DIRS"]["output"]
MC_SAVE_DIR = CONFIG["DIRS"]["mc"]
