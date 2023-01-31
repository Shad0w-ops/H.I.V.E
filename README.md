# H.I.V.E

![New Project (1)](https://user-images.githubusercontent.com/43708460/215883692-c6e63445-f9cd-4757-bfbc-f91c176aa63a.jpg)


### Disclaimer: This tool is intended solely for educational purposes. The creators cannot be held accountable for any unauthorized use. Your utilization of this resource signifies your understanding and acceptance of this disclaimer.

## Table Of Contents

* [installation (Linux)](#installation-linux)
* [Running the application](#running-the-application)
* [Module Breakdown](#module-breakdown)
   * [1) Phonekit:](#1-phonekit)
   * [2) Shodan Crawler:](#2-shodan-crawler)
   * [3) IP Geolocation:](#3-ip-geolocation)
   * [4) Database Lookup:](#4-database-lookup)
   * [5) Email Verifier](#5-email-verifier)
   * [6) Sherlock](#6-sherlock)
   * [7) Metadata](#7-metadata)
   * [8) Misc](#8-misc)
      * [1) Show IP:](#1-show-ip)
      * [2) Start Anonymous Mode:](#2-start-anonymous-mode)
      * [3) Check Anonymous mode status:](#3-check-anonymous-mode-status)
      * [4) Stop Anonymous Mode:](#4-stop-anonymous-mode)
      * [5) Change anonymous mode identity:](#5-change-anonymous-mode-identity)
* [API Status Table](#api-status-table)
* [HIVE Flow Diagram](#hive-flow-diagram)

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

(NOTE) this module will not fully work without the FB19.txt database (which is not and will not provided)

### 2) Shodan Crawler:

The shodan crawler utilises the shodan API to generate YAML formatted reports on a given IP address passively and saves the report in the Shodan_Output folder.

This module can be used to do research on a webserver and get most information needed to develop an attack passivly, meaning the webserver itself wont notice if someone is gathering information on it, as no data is being sent to the webserver.

### 3) IP Geolocation:

The IP geolocation module gives you an esimated location for a given IP address this module is not percise the best it can do is get the country and city.

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
#### 1) Show IP: 
This module shows your current public IP address
#### 2) Start Anonymous Mode:
This module uses the anonsurf tool to tunnel all of your traffic through TOR servers 

Note: This module can make other modules and tools not work properly while using it
#### 3) Check Anonymous mode status:
Checks if anonymous mode is active or disabled
#### 4) Stop Anonymous Mode:
Stops anonymous mode (You can use this to stop the module if other tools stop working.) 
#### 5) Change anonymous mode identity:
if you think your identity got leaked you can use this to change the TOR circuit that you are currently using
## API Status Table

|API|Website|Status|
|----|----|----|
|Shodan API|Shodan.io|Free, Paid, Educational|
|Intelx API|intelx.io|Free, Paid, Educational|
|Hunter API|hunter.io|Free, Paid|

(NOTE) Educational means that there is a better subscription plan for free that they provide for accounts created with student Emails (.edu)

## HIVE Flow Diagram
![hive](https://user-images.githubusercontent.com/43708460/215874114-3ead445a-c12c-4634-949e-13b9f91fdd68.png)
