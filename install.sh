#! /bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

sudo -v

xcode-select --install

# --------- Requirements ------------
printf "${GREEN} Update Brew...${NC}\n"
brew update

printf "${GREEN} Install OpenSSL...${NC}\n"
brew install openssl
brew link openssl --force
# -----------------------------------

printf "${GREEN} Install Burpsuite...${NC}\n"
brew install burp-suite
printf "${GREEN} Install ZAP...${NC}\n"
brew install owasp-zap
printf "${GREEN} Install Ghidra...${NC}\n"
brew install ghidra
printf "${GREEN} Install Wireshark...${NC}\n"
brew install wireshark

printf "${GREEN} Install git...${NC}\n"
brew install git
printf "${GREEN} Install nmap...${NC}\n"
brew install nmap
printf "${GREEN} Install gobuster...${NC}\n"
brew install gobuster
printf "${GREEN} Install nikto...${NC}\n"
brew install nikto
printf "${GREEN} Install wpscan...${NC}\n"
brew install wpscanteam/tap/wpscan
printf "${GREEN} Install metasploit...${NC}\n"
brew install metasploit
printf "${GREEN} Install exploitdb...${NC}\n"
brew install exploitdb
printf "${GREEN} Install john...${NC}\n"
brew install john 
printf "${GREEN} Install hashcat...${NC}\n"
brew install hashcat
printf "${GREEN} Install samba...${NC}\n"
brew install samba

printf "${GREEN} Install binwalk...${NC}\n"
brew install binwalk
printf "${GREEN} Install exiftool...${NC}\n"
brew install exiftool
printf "${GREEN} Install aircrack-ng...${NC}\n"
brew install aircrack-ng
printf "${GREEN} Install hydra...${NC}\n"
brew install hydra


printf "${GREEN} Install smbmap...${NC}\n"
git clone https://github.com/ShawnDEvans/smbmap.git /usr/local/Cellar/smbmap && python3 -m pip install -r /usr/local/Cellar/smbmap/requirements.txt && ln -s /usr/local/Cellar/smbmap/smbmap.py /usr/local/bin/smbmap
printf "${GREEN} Install enum4linux...${NC}\n"
git clone https://github.com/CiscoCXSecurity/enum4linux.git /usr/local/Cellar/enum4linux && ln -s /usr/local/Cellar/enum4linux/enum4linux.pl /usr/local/bin/enum4linux


# --------- install CrackMapExec ------------
printf "${GREEN} Install CrackMapExec...${NC}\n"
pipx install crackmapexec
# -----------------------------------

# --------- install Pwncat Requires Python >= 3.8------------
printf "${GREEN} Install pwncat...${NC}\n"
pipx install git+https://github.com/calebstewart/pwncat.git
# -----------------------------------

# --------- Wordlists ------------
printf "${GREEN} Install wordlist...${NC}\n"
git clone https://github.com/3ndG4me/KaliLists.git /usr/local/share/wordlists && gzip -d /usr/local/share/wordlists/rockyou.txt.gz
printf "${GREEN} Install seclist...${NC}\n"
wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O /tmp/master.zip ; unzip /tmp/master.zip -d /tmp ; mv /tmp/SecLists-master /tmp/seclists ; mv /tmp/seclists /usr/local/share/
# -----------------------------------


mkdir -p jwt
mkdir -p linux
mkdir -p misc
mkdir -p reverse_shells
mkdir -p windows

# --------- Priv Esc ------------
# chisel
printf "${GREEN} Download chisel...${NC}\n"
wget https://github.com/jpillora/chisel/releases/download/v1.7.6/chisel_1.7.6_darwin_amd64.gz -O chisel_osx.gz && gunzip -c chisel_osx.gz > linux/chisel_osx && rm chisel_osx.gz && chmod +x linux/chisel_osx
wget https://github.com/jpillora/chisel/releases/download/v1.7.6/chisel_1.7.6_linux_amd64.gz -O chisel_linux_64.gz && gunzip -c chisel_linux_64.gz > linux/chisel_linux_64 && rm chisel_linux_64.gz
wget https://github.com/jpillora/chisel/releases/download/v1.7.6/chisel_1.7.6_linux_386.gz -O chisel_linux_386.gz && gunzip -c chisel_linux_386.gz > linux/chisel_linux_386 && rm chisel_linux_386.gz

# PEASS-ng
printf "${GREEN} Download peass-ng...${NC}\n"
wget https://raw.githubusercontent.com/carlospolop/PEASS-ng/master/linPEAS/linpeas.sh -O linux/linpeas.sh
wget https://raw.githubusercontent.com/carlospolop/PEASS-ng/master/winPEAS/winPEASbat/winPEAS.bat -O windows/winpeas.bat
wget https://github.com/carlospolop/PEASS-ng/raw/master/winPEAS/winPEASexe/binaries/Release/winPEASany.exe -O windows/winpeas.exe
wget https://github.com/carlospolop/PEASS-ng/raw/master/winPEAS/winPEASexe/binaries/Obfuscated%20Releases/winPEASany.exe -O windows/winpeas_obfuscated.exe

# linenum
printf "${GREEN} Download linenum...${NC}\n"
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh -O linux/linenum.sh

# linux exploit suggester
printf "${GREEN} Download les...${NC}\n"
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O linux/linux-exploit-suggester.sh

# lse 
printf "${GREEN} Download lse...${NC}\n"
wget https://github.com/diego-treitos/linux-smart-enumeration/blob/master/lse.sh -O linux/lse.sh

# pspy 
printf "${GREEN} Download pspy...${NC}\n"
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.0/pspy64 -O linux/pspy64
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.0/pspy32 -O linux/pspy32

# powerup
printf "${GREEN} Download powerup...${NC}\n"
wget https://raw.githubusercontent.com/PowerShellEmpire/PowerTools/master/PowerUp/PowerUp.ps1 -O windows/powerup.ps1

# jaws
printf "${GREEN} Download jaws...${NC}\n"
wget https://raw.githubusercontent.com/411Hall/JAWS/master/jaws-enum.ps1 -O windows/jaws-enum.ps1

# print spoofer
printf "${GREEN} Download printspoofer...${NC}\n"
wget https://github.com/itm4n/PrintSpoofer/releases/download/v1.0/PrintSpoofer32.exe -O windows/printspoof.exe
# -----------------------------------


# --------- Reverse Shells ------------
# powershells revs
printf "${GREEN} Download power rev shell...${NC}\n"
wget https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1 -O reverse_shells/invoke-powershelltcp.ps1

# php rev shell
printf "${GREEN} Download php rev shell...${NC}\n"
wget https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php -O reverse_shells/php-rev-shell.php
# -----------------------------------


# --------- Tools ------------
# TokenBreaker
printf "${GREEN} Download tokenbreaker...${NC}\n"
wget https://raw.githubusercontent.com/cyberblackhole/TokenBreaker/master/RsaToHmac.py -O jwt/RsaToHmac.py && python3 -m pip install -r https://raw.githubusercontent.com/cyberblackhole/TokenBreaker/master/requirements.txt
chmod +x jwt/RsaToHmac.py
wget https://raw.githubusercontent.com/cyberblackhole/TokenBreaker/master/TheNone.py -O jwt/TheNone.py 
chmod +x jwt/TheNone.py

# jwt cracker
printf "${GREEN} Download and install jwt cracker...${NC}\n"
mkdir -p jwt/jwt-cracker
wget https://raw.githubusercontent.com/brendan-rius/c-jwt-cracker/master/Makefile -O jwt/jwt-cracker/Makefile
wget https://raw.githubusercontent.com/brendan-rius/c-jwt-cracker/master/base64.c -O jwt/jwt-cracker/base64.c
wget https://raw.githubusercontent.com/brendan-rius/c-jwt-cracker/master/base64.h -O jwt/jwt-cracker/base64.h
wget https://raw.githubusercontent.com/brendan-rius/c-jwt-cracker/master/main.c -O jwt/jwt-cracker/main.c
cd jwt/jwt-cracker && make OPENSSL=/usr/local/opt/openssl/include OPENSSL_LIB=-L/usr/local/opt/openssl/lib && cd ../../

# hash identifier
printf "${GREEN} Download hash-id...${NC}\n"
wget https://raw.githubusercontent.com/blackploit/hash-identifier/master/hash-id.py -O misc/hash-id.py
chmod +x misc/hash-id.py

# linkfinder
printf "${GREEN} Download linkfinder...${NC}\n"
git clone https://github.com/GerbenJavado/LinkFinder.git misc/linkfinder
cd misc/linkfinder
python3 -m pip install -r requirements.txt
python3 setup.py install
chmod +x linkfinder.py
cd ../../
# -----------------------------------

# Pentest Scripts
printf "${GREEN} Download chikko80 scripts...${NC}\n"
wget https://raw.githubusercontent.com/chikko80/Pen-Scripts/master/basic_scanner.py -O misc/basic_scanner.py
wget https://raw.githubusercontent.com/chikko80/Pen-Scripts/master/hydra_builder.py -O misc/hydra_builder.py
wget https://raw.githubusercontent.com/chikko80/Pen-Scripts/master/string_finder.py -O misc/string_finder.py
python3 -m pip install -r https://raw.githubusercontent.com/chikko80/Pen-Scripts/master/requirements.txt
chmod +x misc/*