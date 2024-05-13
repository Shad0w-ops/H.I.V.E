## Author:       SHAD0W-0PS, UX0l0l
## Script Name:  H.I.V.E
## Start Date:   26/8/2022
## End Date:     --/--/----
## Purpose:      To automate some OSINT tasks

# Importing the Modules
import os
import shodan
import requests
from truecallerpy import search_phonenumber
import yaml
import Banners
import vars
import distro
import geocoder

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# Defining necessary variables
##############################
def define():
    clear()
    print(Banners.bannermain)
    with open('vars.py', 'r+') as file:
        for line in file:
            vals = line.split(" ")
            print(f"{vals[0]}: {vals[2]}")
        print("Note: If not all inputs are filled then some features may not work")
        SHODAN_API = input("Shodan API Key: ")
        INTELX_API = input("IntelX API Key: ")
        HUNTER_API = input("Hunter API Key: ")
        TRUECALLER_ID = input("TrueCaller ID: ")
        DBFILE = input("Text DB file path: ")
    
        file.truncate(0)  # Clear the file first
        file.seek(0)
        file.write(f"SHODAN_API = '{SHODAN_API}'\nINTELX_API = '{INTELX_API}'\nHUNTER_API = '{HUNTER_API}'\nTRUECALLER_ID = '{TRUECALLER_ID}'\nDBFILE = '{DBFILE}'\n")
    main()

# Defining needed Functions
#########################################################

def anon():
    action = input("Enter the desired action {start|stop|change/restart|status}: ")
    if action == "start":
        os.system("anonsurf start" if distro.like() == "debian" else "tor-router start")
    elif action == "stop":
        os.system("anonsurf stop" if distro.like() == "debian" else "tor-router stop")
    elif action == "change" or "restart":
        os.system("anonsurf change" if distro.like() == "debian" else "tor-router restart")
    elif action == "status":
        os.system("anonsurf status" if distro.like() == "debian" else "systemctl status tor-router")
    print(f"Your current IP is now {geocoder.ip("me").ip}")
    input("Press enter to go back to the hive menu: ")
    main()

def CredFetch():
    Found = False
    clear()
    print(Banners.credbanner)
    to_find = input("Enter your search query (name, email, number, etc): ")
    findlist = to_find.split(" ")
    clear()
    labels = ["User ID", "", "Email", "Phone Number", "Religion", "DOB", "First Name", "Last Name", "Gender", "Link", "Language", "Username", "Full Name", "Bio", "Workplace", "Job", "Hometown", "Location", "Education", "", "", "", "", "", "", "Relationship Status", "", "", "", "", "", "", "", "", ""]
    with open(vars.DBFILE, encoding="utf8") as a_file:
        i = 1
        user_info_list = []
        for line in a_file:
            if all(elem in line.lower() for elem in findlist):
                Found = True
                info = line.split(",")
                full_name = ""
                phone_number = ""
                for index, content in enumerate(info):
                    if content and content != "0" and content != "" and content != "1/1/0001 12:00:00 AM" and not content.endswith("@facebook.com") and labels[index] and labels[index] != "":
                        if labels[index] == "Full Name":
                            full_name = content
                        elif labels[index] == "Phone Number":
                            phone_number = content
                if full_name:
                    user_info_list.append(info)
                    print(f"{i}: {full_name} - Phone Number: {phone_number}")
                    i += 1
        if Found:
            select = input("Select user(s) to print full information (e.g. '1 2 3' or type 'all'): ")
            clear()
            if select.lower() == "all":
                selected_users = range(1, len(user_info_list) + 1)
            else:
                selected_users = [int(num) for num in select.split() if num.isdigit() and 0 < int(num) <= len(user_info_list)]
            for user_num in selected_users:
                selected_info = user_info_list[user_num - 1]
                for index, content in enumerate(selected_info):
                    if content and content != "0" and content != "" and content != "1/1/0001 12:00:00 AM" and not content.endswith("@facebook.com") and labels[index] and labels[index] != "":
                        print(f"{labels[index]}: {content}")
                print("--------------------")
            input("Press enter to go back to the hive menu: ")
            main()
        else:
            clear()
            print("Target not found")
            print("--------------------")
            input("Press enter to go back to the hive menu: ")
            main()

def truecaller():
    clear()
    #print(Banners.bannerphone)
    numtosearch = str(input("Enter the number you want to search: "))
    country = input("Enter the country identifier example [CA]: ")
    xlist = search_phonenumber(numtosearch, country, vars.TRUECALLER_ID)
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
        main()

# Shodan module
#--------------
def shodancrawl():
    print(Banners.bannershod)
    ip = input("Enter the IP address you want to search for: ")
    api = shodan.Shodan(vars.SHODAN_API)
    results = api.host(ip)
    yaml_data = yaml.safe_dump(results, default_flow_style=False)
    print(yaml_data)
    with open(f"Shodan_Output/{ip}.txt", "w") as outfile:
        outfile.write(yaml_data)
    print(f"Information about {ip} saved to file.")
    input("Press enter to go back to the hive menu: ")
    main()

# IP geolocation Module
#------------------------
def geo():
    print(Banners.ipgeobanner)
    ip = input("Enter the IP of your Target (leave empty to see yours): ")
    print("Locating IP...")
    response = geocoder.ip(ip).json.get("raw")
    if response:
        for key, value in response.items():
            if key not in ["timezone", "readme"]:  # Exclude these keys
                if key == "ip":
                    print(f"IP: {value}")
                elif key == "loc":
                    print(f"Location: {value}")
                elif key == "org":
                    print(f"ISP: {value}")
                else:
                    print(f"{key.capitalize()}: {value}")
    else:
        print("No data found for the IP.")
    input("Press enter to go back to the hive menu: ")
    main()

# Intelligencex API module
#------------------------
def intel():
    clear()
    print(Banners.list2)
    target2 = str(input("Enter the query you want to search: "))
    clear()
    os.system(f"python Extras/intel.py -search {target2} -buckets \"pastes, dumpster, darknet, web.public, whois, usenet, documents.public, leaks.public\" -apikey {vars.INTELX_API} -limit 100")
    print("Note: if the output isnt satifactory, you can paste the ID\ninto the intelx website then search in that specific database for other info")
    input("Press enter to go back to the hive menu: ")
    main()

# Email Verifier Module
#------------------------
def emver():
    print(Banners.emvbanner)
    email = input('Enter the email you want verified: ')
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={vars.HUNTER_API}'
    response = requests.get(url)
    data = response.json()
    status = data['data']['status']
    if status == 'valid':
        print(f"The email {email} is valid")
    else:
        print(f"The email {email} is not valid")
    input("Press enter to go back to the hive menu: ")
    main()

# integrated Sherlock module
def sher():
    print(Banners.sherbanner)
    target = input("Enter the username of your target: ")
    clear()
    os.system(f"python Extras/sherlock/sherlock/sherlock.py {target} --nsfw -fo Sherlock_Output")
    input("Press enter to go back to the hive menu: ")
    main()

# TO BE USED IN A SEPERATE SCRIPT
#metadata extractor module
#def meta():
#    print(Banners.meta)                        
#    infoDict = {}
#    exifToolPath = ("exiftool")
#    imgPath = input("Enter the path of your file: ")
#    process = subprocess.Popen([exifToolPath,imgPath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) 
#    for tag in process.stdout:
#        line = tag.strip().split(':')
#        infoDict[line[0].strip()] = line[-1].strip()
#    for k,v in infoDict.items():
#        print(k,':', v)
#    print("-------------------------")
#    input("Press enter to go back to the hive menu: ")
#    main()

def misc():
    print(Banners.miscbanner)
    print("----------------")
    choice = input("Choose an option: ")
    if choice =="1":
        anon()
    if choice =="2":
        clear()
        print(Banners.macchange)
        macad = input("Choose an option: ")
        dev_name = input("Enter the device name: ")
        if macad =="1":
            os.system(f"macchanger -r -b {dev_name}")
            input("Press enter to go back to the hive menu: ")
            main()
        if macad =="2":
            macspoof = str(input("Enter the MAC address you want to change to: "))
            os.system(f"macchanger -m {macspoof} {dev_name}")
            input("Press enter to go back to the hive menu: ")
            main()
        if macad =="3":
            os.system(f"macchanger -p {dev_name}")
            input("Press enter to go back to the hive menu: ")
            main()
    input("Press enter to go back to the hive menu: ")
    main()

def modulechoice():
        choice1 = input("Enter the number of the module you want to use: ").strip()
        options = {
            "1": truecaller,
            "2": shodancrawl,
            "3": geo,
            "4": intel,
            "5": emver,
            "6": sher,
            "7": misc,
            "8": CredFetch,
            "9": define,
            "0": exit
        }

        if choice1 in options:
            clear()
            options[choice1]()
        else:
            print("Enter a valid module number!")
            modulechoice()

###########################################################################

# Script start
#------------------------
def main():
    clear()
    print(Banners.bannermain)
    print(Banners.tool_list)
    print("--------------------------------------------")
    modulechoice()

if __name__ == '__main__':
    if os.geteuid() != 0:
        exit("[*] Root privileges not present.\n[*] Run the script using 'sudo python3 hive.py'.")
    elif any(value == '' for value in vars.__dict__.values()):
        define()
    else:
        main()