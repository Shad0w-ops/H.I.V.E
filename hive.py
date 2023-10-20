## Author:       SHAD0W-0PS
## Script Name:  H.I.V.E
## Start Date:   26.8.2022
## End Date:     6/3/2023
## Purpose:      To automate some OSINT tasks

# Importing the Modules
import os
import shodan
import requests
import json
from truecallerpy import search_phonenumber
import yaml
import Banners
import apis
import subprocess
import time

# Defining needed Functions
#########################################################

# phonekit module
# ---------------
def Phone():
    def NPHONE():
        Found = False
        os.system("clear")
        print(Banners.bannerphone)
        to_find = input("Enter Name Of Your Target: ")
        os.system("clear")
        with open("FB19.txt", encoding="utf8") as a_file:
            for line in a_file:
                if to_find in line:
                    Found = True
                    print("Target Found :)")
                    print("--------------------")
                    info = line.split(",,,")
                    print(to_find + ": " + info[1])
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
        print(Banners.bannerphone)
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
        print(Banners.bannerphone)
        numtosearch = str(input("Enter the number you want to search: "))
        country = str(input("Enter the country identifier example [CA]: "))
        xlist = search_phonenumber(numtosearch, country, apis.TRUECALLER_ID)
        print("-------------------------------------")
        print(" ")
        print("Access: ", xlist["data"][0]["access"])
        print("Name: ", xlist["data"][0]["name"])
        print("Id: ", xlist["data"][0]["id"])
        print("Phone: ", xlist["data"][0]["phones"][0]["e164Format"])
        print("------------------------")
        print("type back to go back to main menu")
        choice2 = input("type in your choice: ")
        if choice2 == "back":
            os.system("python hive.py")

    print(Banners.bannerphone)
    print("1: Name To Phone Number Finder")
    print("2: Phone Number To Name Finder")
    print("3: Truecaller phone number lookup")
    print("Type back to go to back to the main menu")
    choice2 = input("Choose an Option: ")
    if choice2 == "1":
        NPHONE()
    if choice2 == "2":
        PhoneN()
    if choice2 == "3":
        truecaller()
    if choice2 == "back":
        os.system("python hive.py")
    else:
        print("invalid input")
        time.sleep(1)
        os.system("clear")
        Phone()


# shodan module
# --------------
def shodancrawl():
    print(Banners.bannershod)
    ip = input("Enter the IP address you want to search for: ")
    api = shodan.Shodan(apis.SHODAN_API_KEY)
    results = api.host(ip)
    yaml_data = yaml.safe_dump(results, default_flow_style=False)
    print(yaml_data)
    with open("Shodan_Output/{}.txt".format(ip), "w") as outfile:
        outfile.write(yaml_data)
    print("Information about {} saved to file.".format(ip))
    back = input("Type back to go back to the HIVE menu: ")
    if back == "back":
        os.system("python hive.py")


# IP geolocation Module
# ------------------------
def geo():
    print(Banners.ipgeobanner)

    def get_location():
        ip = input("Enter the IP of your Target: ")
        response = requests.get(f"https://ipapi.co/{ip}/json/").json()
        location_data = {
            "ip": ip,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name"),
        }
        return location_data

    print(get_location())
    back = input("type back to go back to the main menu: ")
    if back == "back":
        os.system("python hive.py")


# Intelligencex API module
# ------------------------
def intel():
    os.system("clear")
    print(Banners.list2)
    target2 = str(input("Enter the query you want to search: "))
    os.system("clear")
    os.system(
        "python Extras/intel.py -search "
        + target2
        + ' -buckets "pastes, dumpster, darknet, web.public, whois, usenet, documents.public, leaks.public" -apikey '
        + apis.INTELX_API
        + " -limit 100"
    )
    print(
        "Note: if the output isnt satifactory, you can paste the ID\ninto the intelx website then search in that specific database for other info"
    )
    back = input("type back to go back to the hive menu: ")
    if back == "back":
        os.system("python hive.py")


# Email Verifier Module
# ------------------------
def emver():
    print(Banners.emvbanner)
    email = input("Enter the email you want verified: ")
    url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={apis.HUNTER_API}"
    response = requests.get(url)
    data = response.json()
    status = data["data"]["result"]
    if status == "deliverable":
        print("The email " + email + " is valid")
    else:
        print("The email " + email + " is not valid")
    back = input("Type back to go back to the main menu: ")
    if back == "back":
        os.system("python hive.py")


# integrated Sherlock module
def sher():
    print(Banners.sherbanner)
    target = input("Enter the username of your target: ")
    os.system("clear")
    os.system(
        "python Extras/sherlock/sherlock/sherlock.py "
        + target
        + " --nsfw -fo Sherlock_Output"
    )
    back = input("type back to back to the main menu: ")
    if back == "back":
        os.system("python hive.py")


# metadata extractor module
def meta():
    print(Banners.meta)
    infoDict = {}
    exifToolPath = "exiftool"
    imgPath = input("Enter the path of your file: ")
    process = subprocess.Popen(
        [exifToolPath, imgPath],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )
    for tag in process.stdout:
        line = tag.strip().split(":")
        infoDict[line[0].strip()] = line[-1].strip()
    for k, v in infoDict.items():
        print(k, ":", v)
    print("-------------------------")
    back = input("type back to back to the main menu: ")
    if back == "back":
        os.system("python hive.py")


def misc():
    print(Banners.miscbanner)
    print("----------------")
    choice = input("Choose an option: ")
    if choice == "1":
        os.system("curl api.ipify.org")
        print("")
        back1 = input("type back to go to main menu: ")
        if back1 == "back":
            os.system("python hive.py")
    if choice == "2":
        print("Anonymizing session...")
        print("----------------------")
        print("")
        os.system("anonsurf start")
        print("You are now in a TOR tunnel :)")
        time.sleep(2)
        back1 = input("type back to go to main menu: ")
        if back1 == "back":
            os.system("python hive.py")
    if choice == "3":
        os.system("anonsurf status")
        back1 = input("type back to go to main menu: ")
        if back1 == "back":
            os.system("python hive.py")
    if choice == "4":
        os.system("clear")
        print("Exiting TOR tunnel...")
        os.system("anonsurf stop")
        back1 = input("type back to go to main menu: ")
        if back1 == "back":
            os.system("python hive.py")
    if choice == "5":
        os.system("anonsurf change")
        back1 = input("type back to go to main menu: ")
        if back1 == "back":
            os.system("python hive.py")
    if choice == "6":
        os.system("clear")
        print(Banners.macchange)
        macad = input("Choose an option: ")
        if macad == "1":
            device_name = input("Enter the name of the device: ")
            os.system("macchanger -r " + device_name)
            back2 = input("type back to go back to the main menu: ")
            os.system("python hive.py")
        if macad == "2":
            dev_name = str(input("Enter the device name: "))
            macspoof = str(input("Enter the MAC address you want to change to: "))
            os.system("macchanger -m " + macspoof + " " + dev_name)
            back3 = input("type back to go back to the main menu: ")
            os.system("python hive.py")
        if macad == "3":
            deviname = input("Enter the name of the device: ")
            os.system("macchanger -p " + deviname)
            back4 = input("Type back to go back to the main menu: ")
            os.system("python hive.py")
    if choice == "back":
        os.system("python hive.py")

    else:
        print("invalid input")
        time.sleep(3)
        os.system("clear")
        misc()


###########################################################################

# script start
# ------------------------
os.system("clear")
print(Banners.bannermain)
print(Banners.tool_list)
print("type exit to exit the script")
print("--------------------------------------------")
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

if choice1 == "5":
    os.system("clear")
    emver()

if choice1 == "6":
    os.system("clear")
    sher()

if choice1 == "7":
    os.system("clear")
    meta()

if choice1 == "8":
    os.system("clear")
    misc()

if choice1 == "exit":
    os.system("clear")
    exit()

else:
    print("Invalid Input")
    time.sleep(3)
    os.system("python hive.py")
