from CTigerDemon import *

def main():
    tigerDemon = CTigerDemon("ryley","https://arrera-software.fr/depots.json")
    print(tigerDemon.checkUpdate())
    print(tigerDemon.getVersionSoft())

if __name__ == "__main__":
    main()