#!/bin/sh

tools="macchanger"

python3 -m pip install -r requirements.txt

case "$(grep '^ID_LIKE=' /etc/*release | cut -d= -f2)" in
  *debian*)
    sh Extras/kali-anonsurf/installer.sh
    apt install -y $tools
    ;;
  *arch*)
    tools="$tools tor-router"
    pacman -Sy --noconfirm $tools
    ;;
esac
