## Author:       SHAD0W-0PS, UX0l0l
## Script Name:  H.I.V.E
## Start Date:   26/08/2022
## End Date:     --/--/----
## Purpose:      To automate some OSINT tasks

# Importing the Modules
import os
import shodan
import requests
import yaml
import Banners
import vars
import distro
import geocoder
from intelxapi import intelx
from truecallerpy import search_phonenumber

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

itemvars = [(key, value) for key, value in list(vars.__dict__.items()) if not key.startswith("__") and not callable(value)]

# Defining necessary variables
##############################
def define():
    clear()
    print(f"{Banners.bannermain}\n")
    
    itemvars = [(key, value) for key, value in list(vars.__dict__.items()) if not key.startswith("__") and not callable(value)]
    
    for key, value in itemvars:
        print(f"{key}: '{value}'")

    print("\nNote: If not all inputs are filled then some features may not work\nPlease fill out the following information:\n")

    with open('vars.py', 'r+') as file:
        file.truncate(0)
        file.seek(0)
        for key, value in itemvars:
            input_value = input(f"{key}: ")
            file.write(f"{key} = '{input_value}'\n")
    main()

# Defining needed Functions
#########################################################

def anon():
    action = input("Enter the desired action {start|stop|restart|status}: ")
    commands = {
        "start": "anonsurf start" if distro.like() == "debian" else "tor-router start",
        "stop": "anonsurf stop" if distro.like() == "debian" else "tor-router stop",
        "restart": "anonsurf change" if distro.like() == "debian" else "tor-router restart",
        "status": "anonsurf status" if distro.like() == "debian" else "systemctl status tor-router"
    }

    if action in commands:
        os.system(commands.get(action, "Invalid action"))
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
            print("Target not found\n----------------")
            input("Press enter to go back to the hive menu: ")
            main()

def truecaller():
    clear()
    #print(Banners.bannerphone)
    numtosearch = input("Enter the number you want to search: ").strip()
    country = input("Enter the country identifier example [CA]: ")
    xlist = search_phonenumber(numtosearch, country, vars.TRUECALLER_ID)
    print("-------------------------------------\n")
    print("Access: ", xlist["data"][0]["access"])
    print("Name: ", xlist["data"][0]["name"])
    print("Id: ", xlist["data"][0]["id"])
    print("Phone: ", xlist["data"][0]["phones"][0]["e164Format"])
    print("------------------------")
    input("Press enter to go back to the hive menu: ")

# Shodan module
#--------------
def shodancrawl():
    print(Banners.bannershod)
    ip = input("Enter the IP address you want to search for: ").strip()
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
    intelx = intelx(vars.INTELX_API)
    target = input("Enter the query you want to search: ").strip()
    buckets = ["pastes", "dumpster", "darknet", "web.public", "whois", "usenet", "documents.public", "leaks.public"]
    try:
        result = intelx.search(target, buckets=buckets)
        print(yaml.dump(result))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
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
    print(f"The email {email} is {'valid' if status == 'valid' else 'not valid'}")
    input("Press enter to go back to the hive menu: ")
    main()

# integrated Sherlock module
def sher():
    print(Banners.sherbanner)
    target = input("Enter the username of your target: ")
    clear()
    os.system(f"python Extras/sherlock/sherlock/sherlock.py {target} --nsfw -fo Sherlock_Output")
    print("Output saved to the Sherlock_Output directory")
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
    choice = input("Enter the number of the module you want to use: ").strip()
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

    if choice in options:
        clear()
        options[choice]()
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
    modulechoice()

if __name__ == '__main__':
    if os.geteuid() != 0:
        exit("[*] Root privileges not present.\n[*] Run the script using 'sudo python3 hive.py'.")
    elif all(value == '' for value in [value for _, value in itemvars]):
        define()
    else:
        main()