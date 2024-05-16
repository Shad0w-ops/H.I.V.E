![H.I.V.E Logo](https://user-images.githubusercontent.com/43708460/215892281-dd242251-909e-40b0-bcba-c932269ec482.png)


[![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.6-yellow.svg?style=for-the-badge)](https://www.python.org/)
![Develope & tested on Kali Linux & Black Arch](https://img.shields.io/badge/Developed%20&%20tested%20on-Kali%20Linux%20&%20Black%20Arch-blueviolet.svg?style=for-the-badge)

**DISCLAIMER:** This tool is intended solely for educational purposes. The creators cannot be held accountable for any unauthorized use. Your utilization of this resource signifies your understanding and acceptance of this disclaimer.

# Table Of Contents

* [Installation (Linux)](#installation-linux)
     * [How to get Truecaller ID](#how-to-get-truecaller-id)
* [Running the script](#running-the-script)
* [Module Breakdown](#module-breakdown)
   * [1) Truecaller Reverse Lookup](#1-truecaller-reverse-lookup)
   * [2) Shodan Crawler](#2-shodan-crawler)
   * [3) IP Geolocation](#3-ip-geolocation)
   * [4) IntelX Database Lookup](#4-intelx-database-lookup)
   * [5) Email Verifier](#5-email-verifier)
   * [6) Sherlock](#6-sherlock)
   * [7) Misc](#7-misc)
      * [1) Anonymous Mode](#1-anonymous-mode)
      * [2) Spoof your MAC address](#2-spoof-your-mac-address)
   * [8) CredFetch (previously Phonekit)](#8-credfetch-previously-phonekit)
* [API Account Options Table](#api-account-options-table)
* [HIVE Flow Diagram](#hive-flow-diagram) (Needs to be updated)
* [Credits](#credits)

## v1.3 To-do List:

- [ ] Add regex support to [CredFetch](#8-credfetch-previously-phonekit)
- [ ] Attempt to replace all local tools (such as [Anonsurf](#1-anonymous-mode) and [Sherlock module](#6-sherlock))
    - [ ] Make it so that the setup.py script pulls/clones Anonsurf from the repository to download an up-to-date version (it will not be included in the repo by default)
    - [ ] Try to replace Sherlock with an API, if not, the script will be downloaded from the repo and (ideally) imported into the script instead of executed using "os.system()"
- [ ] Organize the outputs into one output directory with a directory for each tool/module
- [ ] Add IntelX output folder (possibly other modules as well)
- [ ] Maybe add more APIs or replace some APIs with more competent ones

## Setup & Installation (Linux)

    python3 setup.py

 Edit the vars.py file by adding your APIs In the following format:

    SHODAN_API = ''
    INTELX_API = ''
    HUNTER_API = ''
    TRUECALLER_ID = ''
    DBFILE = ''

Or simply use the new define function in the script.

## How to get Truecaller ID

For your truecaller ID run:

    truecallerpy login

and follow the steps to get your ID.
If you cant see your ID run:

    truecallerpy -i

or

    truecallerpy --installationid

## Running the script

You can run the script using the following command:

    sudo python3 hive.py

## Module Breakdown

### 1) Truecaller Reverse Lookup

Truecaller Reverse Lookup allows you to reverse-search any phone number and extract data such as their name directly from the truecaller remote servers.

### 2) Shodan Crawler

The shodan crawler utilises the shodan API to generate YAML formatted reports on a given IP address passively and saves the report in the Shodan_Output folder.

This module can be used to do recon on a webserver and get most information needed to develop an attack passivly, meaning the webserver itself wont receive any requests from the attacker and will not be able to detect an attack.

### 3) IP Geolocation

The IP geolocation module gives you an esimated location for a given IP address. Due to the flawed nature of IP addresses this module will not provide a 100% accurate location, but it will provide the country and city. This module can also provide the user with their own public IP if the input field is left empty.

### 4) IntelX Database Lookup

The database lookup module utilises the IntelX API to search for a given query in thousands of leaked databases

(NOTE) the output may not be complete and in that case take the id of the leak and search for it in the IntelX website and search for your query in the database to find that exact term/query.

In this module you can search for:
 * Email addresses
 * Domains
 * URLs
 * IP Addresses
 * Phone Numbers
 * Bitcoin addresses
 * MAC addresses
 * IPFS Hashes
 * Credit Card Numbers
 * IBANs
 * Ethereum addresses

### 5) Email Verifier

This module utilises the Hunter.io API and allows you to check if an email address exists, this can be used to check which emails are valid after bruteforcing a partially redacted email address.

### 6) Sherlock

This module can be used to find usernames across many social networks and saves the output in the Sherlock_Output folder.

### 7) Misc

#### 1) Anonymous Mode

Allows you to enter commands for anonsurf/tor-router to activate system-wide tor-routing for improved privacy and security. Commands include: start, stop, restart and status.

#### 2) Spoof your MAC address

In this module you can change your MAC address to a random or specific MAC address.

### 8) CredFetch (previously Phonekit)

This module has been completely revised and now neatly sorts all data extracted from each single line, allows the user to search for names, phone numbers, and emails within a text database, and the ability to filter data more efficiently has been added as well.

For example, if one wants to search for a certain John Doe, with an American or Canadian phone number, they could input the following text:

    john doe +1

Or if the user wants to find another John Doe that has a GMail address attatched, they can search:

    john doe @gmail[.com]

In the future, regex will be used to better sort text databases of all kinds.

## API Account Options Table

|API|Website|Status|
|----|----|----|
|Shodan API|Shodan.io|Free, Paid, Academic|
|Intelx API|intelx.io|Free, Paid, Academic|
|Hunter API|hunter.io|Free, Paid|

(NOTE) Academic means that there is a better subscription plan for free/discounted that they provide for accounts created with student emails (.edu)

## HIVE Flow Diagram
![hive (2)](https://user-images.githubusercontent.com/43708460/215889147-25a2bed3-df29-40a0-8e7d-deba0934e97c.jpeg)

---

# Credits
* [Truecallerpy](https://github.com/sumithemmadi/truecallerpy)
* [Shodan-Python](https://github.com/achillean/shodan-python)
* [Geocoder](https://github.com/DenisCarriere/geocoder)
* [Intelx.py](https://github.com/IntelligenceX/Python)
* [Hunter.io](https://hunter.io/)
* [Sherlock](https://github.com/sherlock-project/sherlock)
