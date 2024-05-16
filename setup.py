#!/usr/bin/python3
import os, distro

tools = ["macchanger"]
os.system("python3 -m pip install -r requirements.txt")
if distro.like() == "debian":
    os.system("sh Extras/kali-anonsurf/installer.sh")
    os.system("apt install " + " ".join(tools))
elif distro.like() == "arch":
    tools.append("tor-router")
    os.system("pacman -Sy " + " ".join(tools))