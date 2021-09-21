
# OSX CTF Ready
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

This repository makes your Mac OSX system ready for ctfs. It contains a collection of the most popular tools in the pentesting space. 

The install.sh script turns your macos into a kali-like hackstation. Besides the tools of the kali-tools-top10 metapackage many other tools are installed, which are used in conventional CTFs on platforms like HackTheBox or TryHackMe.

In addition, the repo combines many scripts in the area of priveledge escalation and enumeration in one central place, so that you do not have to search for all the scripts individually.

Feel free to make new suggestions or recommendations which scripts should be added to the repo, alternatively you can also create a pull request right away


## Requirements

This installation requires homebrew and python >= 3.8 (recommended & tested on 3.8)

#### Install Homebrew 
```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Install Python3.8 
For safe install download installer via https://www.python.org/downloads/release/python-380/
alternatively (not tested):
```bash
  brew install python@3.8
```

### Manual installations
Steghide require a manual installation steps due to the installation of mac ports

    1. Download and install mac ports https://guide.macports.org/chunked/installing.macports.html
    2. add /usr/local/bin to your path if its missing

```bash
sudo port install steghide
```

## Installation

```bash
  git clone https://github.com/chikko80/OSX-CTF-Ready.git
  cd OSX-CTF-Ready
  chmod +x install.sh
  ./install.sh
```

## Installation Info

Most of the binaries should be directly available since they are installed via brew.

The others:

Script | Location
:-----:|:-----:
tokenbreaker| jwt
jwt-cracker| jwt/jwt-cracker
hash-id| misc
linkfinder | misc/linkfinder

**john** (John The Ripper): by default john is installed via homebrew. Therefore only the john binary is installed and not the jumbo pack. So tools like zip2john or ssh2john are missing. Furthermore the "brew-john" binary **does not support** multithreading via OpenMP. To install John with OpenMP support, read my blog post: TBA
Dont forget to comment john out in the sh file if you are going to install it from source.


## The script installs the following software

### GUI
 - burp-suite community edition
 - owasp-zap
 - ghidra
 - whireshark

### CLI
 - git
 - nmap
 - gobuster
 - nikto
 - wpscan
 - metasploit-framework
 - exploitdb
 - john (**!Read Installation Info above!**)
 - hashcat
 - samba (smbget,smbclient)
 - binwalk
 - exiftool
 - hydra
 - aircrack-ng
 - smbmap
 - enum4linux
 - crackmapexec
 - pwncat
 - tokenbreaker
 - c-jwt-cracker
 - hash-identifier
 - linkfinder
 - steghide

### wordlists
 - kali linux wordlists
 - kali linux seclists


## Script Collection 
### Linux 
 - chisel (osx, amd64, i386) 
 - linpeas.sh (PEASS-ng)
 - linenum.sh
 - linux_smart_enumeration.sh
 - linux_exploit_suggester.sh
 - pspy64
 - pspy32

### Windows 
 - winpeas.bat (PEASS-ng)
 - winpeasany.exe (PEASS-ng)
 - winpeasany_obfuscated.exe (PEASS-ng)
 - powerup.ps1
 - jaws-enum.ps1
 - printspoof.exe

### Reverse Shells
 - invoke-powershelltcp.ps1
 - php-rev-shell.php

### Personal Creation 
 - basic_scanner.py - Does a basic scan on ctf target - nmap, gobuser, extracting comments of found urls, analyzing with wappalyzer api 
 - hydra_buider.py - build hydra commands
 - string_finder.py - finds recursively all files containing string


## Optionals

Install wappalyzer to easily identify technologies on websites
https://www.wappalyzer.com/

## Contributing

Feel free to make new suggestions or recommendations which scripts should be added to the repo, alternatively you can also create a pull request right away

## Credits to repositorys

- https://github.com/zaproxy/zaproxy
- https://github.com/NationalSecurityAgency/ghidra
- https://github.com/wireshark/wireshark

- https://github.com/nmap/nmap
- https://github.com/OJ/gobuster
- https://github.com/sullo/nikto
- https://github.com/wpscanteam/wpscan
- https://github.com/rapid7/metasploit-framework
- https://github.com/offensive-security/exploitdb
- https://github.com/openwall/john
- https://github.com/hashcat
- https://github.com/samba-team/samba
- https://github.com/ReFirmLabs/binwalk
- https://github.com/exiftool/exiftool
- https://github.com/vanhauser-thc/thc-hydra
- https://github.com/aircrack-ng/aircrack-ng
- https://github.com/CiscoCXSecurity/enum4linux
- https://github.com/byt3bl33d3r/CrackMapExec
- https://github.com/calebstewart/pwncat
- https://github.com/cyberblackhole/TokenBreaker
- https://github.com/brendan-rius/c-jwt-cracker
- https://github.com/blackploit/hash-identifier
- https://github.com/GerbenJavado/LinkFinder
- https://github.com/StefanoDeVuono/steghide

- https://github.com/3ndG4me/KaliLists
- https://github.com/danielmiessler/SecLists
  
- https://github.com/jpillora/chisel
- https://github.com/carlospolop/PEASS-ng
- https://github.com/rebootuser/LinEnum
- https://github.com/diego-treitos/linux-smart-enumeration
- https://github.com/mzet-/linux-exploit-suggester
- https://github.com/DominicBreuker/pspy
- https://github.com/PowerShellEmpire/PowerTools
- https://github.com/411Hall/JAWS
- https://github.com/itm4n/PrintSpoofer

- https://github.com/samratashok/nishang
- https://github.com/pentestmonkey/php-reverse-shell

- https://github.com/chikko80/Pen-Scripts.git