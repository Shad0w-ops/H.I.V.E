## Author:       SHAD0W-0PS, UX0l0l
## Script Name:  H.I.V.E
## Start Date:   26/08/2022
## End Date:     --/--/----
## Purpose:      To automate some OSINT tasks

# Importing the Modules
import os
import shodan
import requests
import Banners
import subprocess
import yaml
import vars
import distro
import geocoder
from intelxapi import intelx
from truecallerpy import search_phonenumber

# Defining necessary variables
##############################

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

itemvars = []

def define() -> None:
    clear()
    print(f"{Banners.bannermain}\n")
    
    global itemvars
    itemvars = [(key, value) for key, value in list(vars.__dict__.items()) if not key.startswith("__") and not callable(value)]
    
    for key, value in itemvars:
        print(f"{key} = '{value}'")

    print("\nNote: If not all inputs are filled then some features may not work\nPlease fill out the following information:\n")

    with open('vars.py', 'r+') as file:
        file.truncate(0)
        file.seek(0)
        for key, value in itemvars:
            input_value = input(f"{key}: ")
            file.write(f"{key} = '{input_value}'\n")
    return main()

intelx = intelx(vars.INTELX_API)

# Defining needed Functions
###########################
def spoof(choice=None) -> None:
    match choice:
        case None:
            print(Banners.spoofbanner)
            print("----------------")
            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                clear()
                print("Please enter a valid number!")
                choice = None
            return spoof(choice)
        case 1:
            action = input("Enter the desired action {start|stop|restart|status}: ")
            commands = {
                "start": "anonsurf start" if distro.like() == "debian" else "tor-router start",
                "stop": "anonsurf stop" if distro.like() == "debian" else "tor-router stop",
                "restart": "anonsurf change" if distro.like() == "debian" else "tor-router restart",
                "status": "anonsurf status" if distro.like() == "debian" else "systemctl status tor-router"
            }
            command = commands.get(action)
            if command:
                os.system(command)
                print(f"Your current IP is now {geocoder.ip('me').ip}")
            else:
                print("Invalid action")
                return spoof(1)
        case 2 | 3 | 4 | 5:
            dev_name = input("Enter the device name: ")
            os.system(f"ifconfig {dev_name} down")
            match choice:
                case 2:
                    command = f"macchanger -r -b {dev_name}"
                case 3:
                    command = f"macchanger -r {dev_name}"
                case 4:
                    macspoof = input("Enter the MAC address you want to change to: ")
                    command = f"macchanger -m {macspoof} {dev_name}"
                case 5:
                    command = f"macchanger -p {dev_name}"
            os.system(command)
            os.system(f"ifconfig {dev_name} up")
        case _:
            clear()
            print("Invalid choice")
            return spoof()
    input("Press enter to go back to the hive menu: ")
    return main()

def CredFetch() -> None:
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
                        match labels[index]:
                            case "Full Name":
                                full_name = content
                            case "Phone Number":
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
            return main()
        else:
            clear()
            print("Target not found\n----------------")
            input("Press enter to go back to the hive menu: ")
            return main()

def truecaller() -> None:
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
    return main()

# Shodan module
#--------------
def shodancrawl() -> None:
    print(Banners.bannershod)
    ip = input("Enter the IP address you want to search for: ").strip()
    api = shodan.Shodan(vars.SHODAN_API)
    results = api.host(ip)
    yaml_data = yaml.safe_dump(results, default_flow_style=False)
    subprocess.run(['less'], input=yaml_data.encode())
    save = input("Would you like to save the output? [Y/n] ")
    if save.lower() != "n":
        with open(f"output/shodan/{ip}.yaml", "w") as outfile:
            outfile.write(yaml_data)
            print(f"Information about {ip} saved in output directory.")
    input("Press enter to go back to the hive menu: ")
    return main()

# IP geolocation Module
#------------------------
def geo() -> None:
    print(Banners.ipgeobanner)
    ip = input("Enter the IP of your Target (leave empty to see yours): ")
    print("Locating IP...")
    response = geocoder.ip(ip).json.get("raw")
    if response:
        for key, value in response.items():
            match key:
                case "timezone" | "readme":
                    pass
                case "ip":
                    print(f"IP: {value}")
                case "loc":
                    print(f"Location: {value}")
                case "org":
                    print(f"ISP: {value}")
                case _:
                    print(f"{key.capitalize()}: {value}")
    else:
        print("No data found for the IP.")
    input("Press enter to go back to the hive menu: ")
    return main()

# Intelligencex API module
#-------------------------
def intel() -> None:
    clear()
    print(Banners.list2)
    target = input("Enter the query you want to search: ").strip()
    buckets = ["pastes", "dumpster", "darknet", "web.public", "whois", "usenet", "documents.public", "leaks.public"]
    try:
        result = intelx.search(target, buckets=buckets)
        yaml_data = yaml.dump(result)
        subprocess.run(['less'], input=yaml_data.encode())
        save = input("Would you like to save the output? [Y/n] ")
        if save.lower() != "n":
            with open(f"output/intelx/{target}.yaml", "w") as outfile:
                outfile.write(yaml_data)
                print(f"Saved to {target}.yaml in output directory.")
        print("Note: if the output isnt satifactory, you can paste the ID\ninto the intelx website then search in that specific database for other info")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press enter to go back to the hive menu: ")
        return main()

# Email Verifier Module
#------------------------
def emver() -> None:
    print(Banners.emvbanner)
    email = input('Enter the email you want verified: ')
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={vars.HUNTER_API}'
    response = requests.get(url)
    data = response.json()
    status = data['data']['status']
    print(f"The email {email} is {'valid' if status == 'valid' else 'not valid'}")
    input("Press enter to go back to the hive menu: ")
    return main()

# integrated Sherlock module
def sher() -> None:
    print(Banners.sherbanner)
    target = input("Enter the username of your target: ")
    clear()
    os.system(f"python Extras/sherlock/sherlock/sherlock.py {target} --nsfw -fo output/sherlock")
    print("Results saved to the sherlock output directory")
    input("Press enter to go back to the hive menu: ")
    return main()

# TO BE USED IN A SEPERATE SCRIPT
#metadata extractor module
#def meta() -> None:
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
#    return main()

def modulechoice() -> None:
    choice = input("Enter the number of the module you want to use: ").strip()
    options = {
        "1": truecaller,
        "2": shodancrawl,
        "3": geo,
        "4": intel,
        "5": emver,
        "6": sher,
        "7": spoof,
        "8": CredFetch,
        "9": define,
        "0": exit
    }

    if choice in options:
        clear()
        return options[choice]()
    else:
        print("Enter a valid module number!")
        return modulechoice()

#########################
# Script start
#------------------------
def main() -> None:
    clear()
    print(Banners.bannermain)
    print(Banners.tool_list)
    return modulechoice()

if __name__ == '__main__':
    if os.geteuid() != 0:
        exit("[*] Root privileges not present.\n[*] Run the script using 'sudo python3 hive.py'.")
    elif all(value == '' for _, value in itemvars):
        define()
    else:
        main()