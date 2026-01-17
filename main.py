from version_demon import *

def main():
    conf = soft_config(name_soft="ryley",version="I2025-0.00")
    tigerDemon = demon(conf,"https://arrera-software.fr/depots.json")
    print(f"Etat internet : {tigerDemon.getInternet()}")
    print(f"Etat Update : {tigerDemon.checkUpdate()}")
    print(f"Version : {tigerDemon.getVersionSoft()}")

if __name__ == "__main__":
    main()