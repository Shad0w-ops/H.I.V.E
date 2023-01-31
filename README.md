# H.I.V.E

![lol](https://user-images.githubusercontent.com/43708460/215424857-d42f836d-782c-4db8-a66c-8c3af78bc960.jpg)

H.I.V.E OSINT automation multi tool 

(DISCLAIMER)
This tool is made for educational purposes only, and i wont be held responsible for any missuse of this tool.

## installation (Linux)

    python3 setup.py

 Edit the apis.py file by adding your APIs In the following format

SHODAN_API_KEY = "YOUR API KEY HERE"

INTELX_API = "YOUR API KEY HERE"

HUNTER_API = "YOUR API KEY HERE"

TRUECALLER_ID = "YOUR INSTALLATION ID HERE" 

(How to get Truecaller ID)

for your truecaller ID run:

    truecallerpy --login 
and follow the steps to get your ID
if you cant see it run:

    truecallerpy -i

## Running the application

    python3 hive.py

## Module Breakdown

### 1) Phonekit:

Phonekit allows you to get someones phone number from their name and vice versa using a database called FB19.txt in addition to having a builtin truecaller module to reverse lookup phone numbers without the database.

(NOTE) this module will not fully work without the FB19.txt database (which is not provided)

### 2) Shodan Crawler:

The shodan crawler utilises the shodan API to generate YAML formatted reports on a given IP address passively and saves the report in the Shodan_Output folder.

### 3) IP Geolocation:

The IP geolocation module gives you an esimated location for a given IP address.

### 4) Database Lookup:

The database lookup module utilises the IntelX API to search for a given query in thousands of leaked databases

(NOTE) the output may not be complete and in that case take the id of the leak and search for it in the INTELX website and search for your query in the database to find that exact term/query.

In this module you can search for:

Email addresses, Domains, URLs, IP Addresses, Phone Numbers, Bitcoin addresses, MAC addresses, IPFS Hashes, Credit Card Numbers, IBANs and Ethereum addresses

### 5) Email Verifier

This module utilises the Hunter.io API and allows you to check if an email address exists, this can be used to check which emails are valid after bruteforcing a partially redacted email address.

### 6) Sherlock

This module can be used to find usernames across many social networks and saves the output in the Sherlock_Output folder.

### 7) Metadata

This module is used to find the metadata of any file you provide for example (camera lense, dimensions, location, etc...)
to use this module just provide the full path of the file or just drag and drop the file onto the terminal and hit Enter

### 8) Misc
#### 1) Show IP: This module shows your current public IP address
#### 2) Start Anonymous Mode: This module uses the anonsurf tool to tunnel all of your traffic through TOR servers 
Note: This module can make other modules and tools not work properly while using it
#### 3) Check Anonymous mode status: Checks if anonymous mode is active or disabled
#### 4) Stop Anonymous Mode: Stops anonymous mode (You can use this to stop the module if other tools stop working.) 
## API Status Table

|API|Website|Status|
|----|----|----|
|Shodan API|Shodan.io|Free, Paid, Educational|
|Intelx API|intelx.io|Free, Paid, Educational|
|Hunter API|hunter.io|Free, Paid|

(NOTE) Educational means that there is a better subscription plan for free that they provide for accounts created with student Emails (.edu)

## HIVE Flow Diagram
![hive (1)](https://user-images.githubusercontent.com/43708460/215424218-987e73c5-132a-4db4-9974-c7567a712adc.jpeg)
