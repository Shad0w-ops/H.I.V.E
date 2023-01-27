## Author:       SHAD0W-0PS
## Script Name:  H.I.V.E
## Start Date:   23.12.2022
## End Date:     27/1/2023  
## Purpose:      To automate some OSINT tasks

#Importing the Modules
import os
import shodan
import requests
import json
from truecallerpy import search_phonenumber
import yaml

#APIs
#######################################################################
#Shodan API key
SHODAN_API_KEY = ""
#intelx academia API
INTELX_API = ""
#Hunter.io API
HUNTER_API = ""
#Truecaller id
TRUECALLER_ID = "" #your truecaller ID here use (truecallerpy --login) to log into the account (truecallerpy --installationid) to view installation ID

#Script Banner Art
#######################################################################

#Main Banner
bannermain = '''
 /$$   /$$     /$$$$$$  /$$    /$$ /$$$$$$$$
| $$  | $$    |_  $$_/ | $$   | $$| $$_____/
| $$  | $$      | $$   | $$   | $$| $$      
| $$$$$$$$      | $$   |  $$ / $$/| $$$$$   
| $$__  $$      | $$    \  $$ $$/ | $$__/   
| $$  | $$      | $$     \  $$$/  | $$      
| $$  | $$ /$$ /$$$$$$ /$$\  $//$$| $$$$$$$$
|__/  |__/|__/|______/|__/ \_/|__/|________/
)-------------------V.1.1------------------(                                            
'''

#PhoneKit Banner
bannerphone = '''
 /$$$$$$$  /$$                                     /$$   /$$ /$$   /$$    
| $$__  $$| $$                                    | $$  /$$/|__/  | $$    
| $$  \ $$| $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$ | $$ /$$/  /$$ /$$$$$$  
| $$$$$$$/| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$$$$/  | $$|_  $$_/  
| $$____/ | $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  $$  | $$  | $$    
| $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/| $$\  $$ | $$  | $$ /$$
| $$      | $$  | $$|  $$$$$$/| $$  | $$|  $$$$$$$| $$ \  $$| $$  |  $$$$/
|__/      |__/  |__/ \______/ |__/  |__/ \_______/|__/  \__/|__/   \___/  
--------------------------------------------------------------------------
'''

#Shodan Banner
bannershod = '''
  /$$$$$$  /$$                       /$$                    
 /$$__  $$| $$                      | $$                    
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$$ 
|  $$$$$$ | $$__  $$ /$$__  $$ /$$__  $$ |____  $$| $$__  $$
 \____  $$| $$  \ $$| $$  \ $$| $$  | $$  /$$$$$$$| $$  \ $$
 /$$  \ $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$
|  $$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$
 \______/ |__/  |__/ \______/  \_______/ \_______/|__/  |__/
 ------------------------------------------------------------
'''

#Email Verifier Banner
emvbanner = '''

 /$$$$$$$$                         /$$ /$$       /$$    /$$                    /$$  /$$$$$$  /$$                    
| $$_____/                        |__/| $$      | $$   | $$                   |__/ /$$__  $$|__/                    
| $$       /$$$$$$/$$$$   /$$$$$$  /$$| $$      | $$   | $$ /$$$$$$   /$$$$$$  /$$| $$  \__/ /$$  /$$$$$$   /$$$$$$ 
| $$$$$   | $$_  $$_  $$ |____  $$| $$| $$      |  $$ / $$//$$__  $$ /$$__  $$| $$| $$$$    | $$ /$$__  $$ /$$__  $$
| $$__/   | $$ \ $$ \ $$  /$$$$$$$| $$| $$       \  $$ $$/| $$$$$$$$| $$  \__/| $$| $$_/    | $$| $$$$$$$$| $$  \__/
| $$      | $$ | $$ | $$ /$$__  $$| $$| $$        \  $$$/ | $$_____/| $$      | $$| $$      | $$| $$_____/| $$      
| $$$$$$$$| $$ | $$ | $$|  $$$$$$$| $$| $$         \  $/  |  $$$$$$$| $$      | $$| $$      | $$|  $$$$$$$| $$      
|________/|__/ |__/ |__/ \_______/|__/|__/          \_/    \_______/|__/      |__/|__/      |__/ \_______/|__/      
-------------------------------------------------------------------------------------------------------------------
'''

#IPGeolocation Banner
ipgeobanner = '''
 /$$$$$$ /$$$$$$$          /$$$$$$  /$$$$$$$$  /$$$$$$ 
|_  $$_/| $$__  $$        /$$__  $$| $$_____/ /$$__  $$
  | $$  | $$  \ $$       | $$  \__/| $$      | $$  \ $$
  | $$  | $$$$$$$//$$$$$$| $$ /$$$$| $$$$$   | $$  | $$
  | $$  | $$____/|______/| $$|_  $$| $$__/   | $$  | $$
  | $$  | $$             | $$  \ $$| $$      | $$  | $$
 /$$$$$$| $$             |  $$$$$$/| $$$$$$$$|  $$$$$$/
|______/|__/              \______/ |________/ \______/ 
-------------------------------------------------------'''

#List Banners
###########################################################

#Main tool list
tool_list = '''
1) PhoneKit
2) Shodan Crawler
3) IP geolocation
4) Database Lookup
5) Email Verifier
'''
#intelx capabilities banner
list2 = '''
In this module you can search for any of those
----------------------------------------------
Email address       Ethereum address
Domain              MAC address
URL                 IPFS Hash
IP Addresses        Credit Card Number
Phone Numbers       Social Security Number
Bitcoin address     IBAN
----------------------------------------------
'''

#Defining needed Functions
#########################################################

#phonekit module
#---------------
def Phone():
    def NPHONE():
        Found = False
        os.system("clear")
        print(bannerphone)
        to_find = input("Enter Name Of Your Target: ")
        os.system("clear")
        with open("FB19.txt", encoding="utf8") as a_file:
                for line in a_file:
                    if to_find in line:
                        Found = True
                        print("Target Found :)")
                        print("--------------------")
                        info = line.split(",,,")
                        print(to_find +": "+ info[1])
                        print("--------------------")
                        print("other info: ")
                        print(line)
                        print("--------------------")
                if Found:
                    print("type main to go back to the HIVE menu")
                    print("type back to go back to Phonekit menu")
                    back = input("whats your next step?: ")
                    if back == "main":
                        os.system("clear")
                        os.system("python hive.py")
                    if back == "back":
                        os.system("clear")
                        Phone()
                elif not Found:
                    os.system("clear")
                    print("target not found")
                    print("--------------------")
                    print("type main to go back to the HIVE menu")
                    print("type back to go back to Phonekit menu")
                    back = input("whats your next step?: ")
                    if back == "main":
                        os.system("clear")
                        os.system("python hive.py")
                    if back == "back":
                        os.system("clear")
                        Phone()


    def PhoneN():
        Found = False
        os.system("clear")
        print(bannerphone)
        to_find = input("Enter The Phone number Of Your Target(include +962): ")
        os.system("clear")
        with open("FB19.txt", encoding="utf8") as a_file:
                for line in a_file:
                    if to_find in line:
                        Found = True
                        print("Target Found :)")
                        print("--------------------")
                        print(to_find)
                        print("--------------------")
                        print(line)
                        print("--------------------")
                if Found:
                    print("type main to go back to the HIVE menu")
                    print("type back to go back to Phonekit menu")
                    back = input("whats your next step?: ")
                    if back == "main":
                        os.system("clear")
                        os.system("python hive.py")
                    if back == "back":
                        os.system("clear")
                        Phone()
                elif not Found:
                    os.system("clear")
                    print("target not found")
                    print("--------------------")
                    print("type main to go back to the HIVE menu")
                    print("type back to go back to Phonekit menu")
                    back = input("whats your next step?: ")
                    if back == "main":
                        os.system("clear")
                        os.system("python hive.py")
                    if back == "back":
                        os.system("clear")
                        Phone()
    def truecaller():
        os.system("clear")
        print(bannerphone)
        numtosearch = str(input("Enter the number you want to search: "))
        country = str(input("Enter the country identifier example [CA]: "))
        xlist = search_phonenumber(numtosearch,country, TRUECALLER_ID)
        print("-------------------------------------")
        print(" ")
        print("Access: ", xlist["data"][0]["access"])
        print("Name: ", xlist["data"][0]["name"])
        print("Id: ", xlist["data"][0]["id"])
        print("Phone: ", xlist["data"][0]["phones"][0]["e164Format"])
        print("------------------------")
        print("type back to go back to main menu")
        choice2 = input("type in your choice: ")
        if choice2 =="back":
            os.system("python hive.py")

    print(bannerphone)
    print("1: Name To Phone Number Finder")
    print("2: Phone Number To Name Finder")
    print("3: Truecaller phone number lookup")
    print("Type back to go to back to the main menu")
    choice2 = input("Choose an Option: ")
    if choice2 =="1":
        NPHONE()
    if choice2 == "2":
        PhoneN()
    if choice2 == "3":
        truecaller()
    if choice2 == "back":
        os.system("python hive.py")

#shodan module
#--------------
def shodancrawl():
    print(bannershod)
    ip = input("Enter the IP address you want to search for: ")
    api = shodan.Shodan(SHODAN_API_KEY)
    results = api.host(ip)
    yaml_data = yaml.safe_dump(results, default_flow_style=False)
    print(yaml_data)
    with open("Shodan_Output/{}.txt".format(ip), "w") as outfile:
        outfile.write(yaml_data)
    print("Information about {} saved to file.".format(ip))
    back = input("Type back to go back to the HIVE menu: ")
    if back =="back":
        os.system("python hive.py")

#IP geolocation Module
#------------------------
def geo():
    print(ipgeobanner)
    def get_location():
        ip = input("Enter the IP of your Target: ")
        response = requests.get(f'https://ipapi.co/{ip}/json/').json()
        location_data = {
            "ip": ip,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        return location_data
    print(get_location())
    back = input("type back to go back to the main menu: ")
    if back =="back":
        os.system("python hive.py")

#Intelligencex API module
#------------------------
def intel():
    os.system("clear")
    print(list2)
    target2 = str(input("Enter the query you want to search: "))
    os.system("clear")
    os.system("python Extras/intel.py -search "+ target2+" -buckets \"pastes, dumpster, darknet, web.public, whois, usenet, documents.public, leaks.public\" -apikey " +INTELX_API+ " -limit 100")
    print("Note: if the output isnt satifactory, you can paste the ID\ninto the intelx website then search in that specific database for other info")
    back = input("type back to go back to the hive menu: ")
    if back =="back":
        os.system("python hive.py")

#Email Verifier Module
#------------------------
def emver():
    print(emvbanner)
    email = input('Enter the email you want verified: ')
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={HUNTER_API}'
    response = requests.get(url)
    data = response.json()
    status = data['data']['result']
    if status == 'deliverable':
        print("The email "+email+" is valid")
    else:
        print("The email "+email+" is not valid")
    back = input("Type back to go back to the main menu: ")
    if back =="back":
        os.system("python hive.py")
###########################################################################

#script start
#------------------------
os.system("clear")
print(bannermain)
print(tool_list)
print("type exit to exit the script")
choice1 = input("Enter The Number of The Module you want to use: ")

if choice1 == "1":
    os.system("clear")
    Phone()

if choice1 == "2":
    os.system("clear")
    shodancrawl()

if choice1 == "3":
    os.system("clear")
    geo()

if choice1 == "4":
    os.system("clear")
    intel()

if choice1 =="5":
    os.system("clear")
    emver()
else:
    print("Sad to see you go :(")
    exit()
