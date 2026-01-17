from version_demon import *

def main():
    conf = soft_config(name_soft="ryley",version="I2025-0.00")
    tigerDemon = demon(conf,"https://arrera-software.fr/depots.json")
    print(tigerDemon.getInternet())
    print(tigerDemon.checkUpdate())
    print(tigerDemon.getVersionSoft())

if __name__ == "__main__":
    main()