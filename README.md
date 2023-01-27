# H.I.V.E

![hive-logo-design-vector-illustration_742779-462](https://user-images.githubusercontent.com/43708460/214978101-913b56fb-e637-460a-98cd-1f1a38822191.jpg)

H.I.V.E OSINT automation tool 

(DISCLAIMER)
This tool is made for educational purposes only, and i wont be held responsible for any missuse of this tool.

## installation

    pip3 install -r requirements.txt

 Edit the hive.py file by adding your APIs In the following format

SHODAN_API_KEY = "YOUR API KEY HERE"

INTELX_API = "YOUR API KEY HERE"

HUNTER_API = "YOUR API KEY HERE"

TRUECALLER_ID = "YOUR INSTALLATION ID HERE" 

(How to get Truecaller ID)

for your truecaller ID run:

    truecallerpy --login 
and follow the steps to get your ID
if you cant see it run:

    truecallerpy --installationid

## Running the application

    python3 hive.py

## Module Breakdown

### Phonekit:

Phonekit allows you to get someones phone number from their name and vice versa using a database called FB19.txt in addition to having a builtin truecaller module to reverse lookup phone numbers without the database

(NOTE) this module will not fully work without the FB19.txt database (which is not provided)

### Shodan Crawler:

The shodan crawler utilises the shodan API to generate JSON formatted reports on a givven IP address passively and saves the report in the Shodan_Output folder

### IP Geolocation:

The IP geolocation module gives you an esimated location for a givven IP address

### Database Lookup:

The database lookup module utilises the IntelX API to dearch for a givven query in thousands of leaked databases

(NOTE) the output may not be complete and in that case take the id of the leak and search for it in the INTELX website and search for your query in the database to find that exact term/query

### Email Verifier

This module utilises the Hunter.io API and allows you to check if an email address exists, this can be used to check which emails are valid after bruteforcing a partially redacted email address

## API Status Table

|API|Website|Status|
|----|----|----|
|Shodan API|Shodan.io|Free, Paid, Educational|
|Intelx API|intelx.io|Free, Paid, Educational|
|Hunter API|hunter.io|Free, Paid|

(Note) Educational means that there is a better subscription plan for free that they provide for accounts created with student Emails (.edu)
