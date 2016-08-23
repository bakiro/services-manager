#!/usr/bin/python

import os
import time

apache = mysql = postgresql = mongodb = 0
menu = {}


def getStatusServices():
    global apache, mysql, postgresql, mongodb

    a = os.popen("service apache2 status").read()
    if (a.find("Active: active (running)") > -1):
        apache = 1
    else:
        apache = 0

    b = os.popen("service mysql status").read()
    if (b.find("Active: active (running)") > -1):
        mysql = 1
    else:
        mysql = 0

    c = os.popen("service postgresql status").read()
    if (c.find("Active: active (running)") > -1):
        postgresql = 1
    else:
        postgresql = 0

    d = os.popen("service mongod status").read()
    if (d.find("Active: active (running)") > -1):
        mongodb = 1
    else:
        mongodb = 0


def printStatusServices():
    global apache, mysql, postgresql, mongodb
    getStatusServices()
    if(apache):
        print("Apache : ON")
        menu['1'] = "Turn off Apache"
    else:
        print("Apache : OFF")
        menu['1'] = "Turn on Apache"

    if(mysql):
        print("MySQL : ON")
        menu['2'] = "Turn off MySQL"
    else:
        print("MySQL : OFF")
        menu['2'] = "Turn on MySQL"

    if(postgresql):
        print("PostgreSQL : ON")
        menu['3'] = "Turn off PostgreSQL"
    else:
        print("PostgreSQL : OFF")
        menu['3'] = "Turn on PostgreSQL"

    if(mongodb):
        print("MongoDB : ON")
        menu['4'] = "Turn off MongoDB"
    else:
        print("MongoDB : OFF")
        menu['4'] = "Turn on MongoDB"


def mainMenu():
    global apache, mysql, postgresql, mongodb, menu
    selection = ""
    menu['5'] = "Exit"
    while selection != '5':
        os.system("clear")
        printStatusServices()
        options = list(menu.keys())
        options.sort()
        print("")
        for entry in options:
            print((str(entry) + ') ' + menu[entry]))

        print("")
        selection = raw_input("Please Select:")
        if selection == '1':
            if(apache):
                os.system("sudo service apache2 stop")
            else:
                os.system("sudo service apache2 start")
        elif selection == '2':
            if(mysql):
                os.system("sudo service mysql stop")
            else:
                os.system("sudo service mysql start")
        elif selection == '3':
            if(postgresql):
                os.system("sudo service postgresql stop")
            else:
                os.system("sudo service postgresql start")
        elif selection == '4':
            if(mongodb):
                os.system("sudo service mongod stop")
            else:
                os.system("sudo service mongod start")
        elif selection == '5':
            os.system('clear')
            break
        else:
            print("Unknown Option Selected!")
            time.sleep(3)


mainMenu()