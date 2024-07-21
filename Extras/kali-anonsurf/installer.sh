#!/bin/sh

# Ensure we are being ran as root
[ $(id -u) -eq 0 ] || { echo "This script must be ran as root"; exit 1; }

# For upgrades and sanity check, remove any existing i2p.list file
rm -f /etc/apt/sources.list.d/i2p.list

# Install gnupg if not installed
command -v gpg >/dev/null || { apt update && apt install -y gnupg; }

# Compile the i2p ppa
echo "deb https://ppa.launchpadcontent.net/i2p-maintainers/i2p/ubuntu noble main" > /etc/apt/sources.list.d/i2p.list # Default config reads repos from sources.list.d
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys AB9660B9EB2CC88B  # Add i2p maintainer keys
apt update # Update repos

apt install -y secure-delete tor i2p i2p-router # install dependencies, just in case

# Configure and install the .deb
dpkg-deb -b kali-anonsurf-deb-src/ kali-anonsurf.deb # Build the deb package
dpkg -i kali-anonsurf.deb || (apt -f install && dpkg -i kali-anonsurf.deb) # this will automatically install the required packages

# Check if kali-anonsurf package is already installed
dpkg -l | grep -qw kali-anonsurf || { echo "The package 'kali-anonsurf' did not install successfully."; exit 1; }

exit 0
