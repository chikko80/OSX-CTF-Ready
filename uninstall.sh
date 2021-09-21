#! /bin/bash

GREEN='\033[0;31m'
NC='\033[0m' # No Color

sudo -v

printf "${GREEN} Uninstall Burpsuite...${NC}\n"
brew uninstall burp-suite
printf "${GREEN} Uninstall ZAP...${NC}\n"
brew uninstall owasp-zap
printf "${GREEN} Uninstall Ghidra...${NC}\n"
brew uninstall ghidra
printf "${GREEN} Uninstall Wireshark...${NC}\n"
brew uninstall wireshark

printf "${GREEN} Uninstall nmap...${NC}\n"
brew uninstall nmap
printf "${GREEN} Uninstall gobuster...${NC}\n"
brew uninstall gobuster
printf "${GREEN} Uninstall nikto...${NC}\n"
brew uninstall nikto
printf "${GREEN} Uninstall wpscan...${NC}\n"
brew uninstall wpscanteam/tap/wpscan
printf "${GREEN} Uninstall metasploit...${NC}\n"
brew uninstall metasploit
printf "${GREEN} Uninstall exploitdb...${NC}\n"
brew uninstall exploitdb
printf "${GREEN} Uninstall john...${NC}\n"
brew uninstall john 
printf "${GREEN} Uninstall hashcat...${NC}\n"
brew uninstall hashcat
printf "${GREEN} Uninstall samba...${NC}\n"
brew uninstall samba

printf "${GREEN} Uninstall binwalk...${NC}\n"
brew uninstall binwalk
printf "${GREEN} Uninstall exiftool...${NC}\n"
brew uninstall exiftool
printf "${GREEN} Uninstall aircrack-ng...${NC}\n"
brew uninstall aircrack-ng
printf "${GREEN} Uninstall hydra...${NC}\n"
brew uninstall hydra
printf "${GREEN} Uninstall sqlmap...${NC}\n"
brew uninstall sqlmap


printf "${GREEN} Uninstall smbmap...${NC}\n"
sudo rm /usr/local/bin/smbmap
sudo rm -rf /usr/local/Cellar/smbmap

printf "${GREEN} Uninstall enum4linux...${NC}\n"
sudo rm /usr/local/bin/enum4linux
sudo rm -rf /usr/local/Cellar/enum4linux

# --------- install CrackMapExec ------------
printf "${GREEN} Uninstall CrackMapExec...${NC}\n"
pipx uninstall crackmapexec
# -----------------------------------

# --------- install Pwncat Requires Python >= 3.8------------
printf "${GREEN} Uninstall pwncat...${NC}\n"
pipx uninstall pwncat
# -----------------------------------

# --------- Wordlists ------------
printf "${GREEN} Uninstall wordlist...${NC}\n"
sudo rm -rf /usr/local/share/wordlists
printf "${GREEN} Uninstall seclist...${NC}\n"
sudo rm -rf /usr/local/share/seclists
# -----------------------------------