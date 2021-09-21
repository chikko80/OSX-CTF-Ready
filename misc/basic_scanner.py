#!/usr/bin/env python3

import warnings
warnings.simplefilter("ignore", UserWarning)

import argparse
import os
import requests
from Wappalyzer import Wappalyzer, WebPage
import re
import subprocess
import shlex
import threading
import sys

subdirectories = []

parser = argparse.ArgumentParser(description='Basic Scanner for CTF')
parser.add_argument('host', help='directory to start')
parser.add_argument('--rec','-r', help='recursive gobuster scan', action='store_true')
parser.add_argument('--subdomains','-s', help='scan subdomains', action='store_true')
args = parser.parse_args()
ip = args.host
rec = args.rec
sub = args.subdomains

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'


def menu_decorator(color_args):
    def function_wrapper(func):
        def draw_outlines(*args):
            print_colored_line(color_args['color'])
            print_colored_string(color_args['color'], f"\t{color_args['text']}")
            print_colored_line(color_args['color'])
            print(color_args['color'], end='')
            func(*args)
            print_colored_line(color_args['color'])
            print('\033[0m')
        return draw_outlines
    return function_wrapper

def main():
    global ip
    print_colored_line(GREEN)
    print_colored_string(GREEN, f"Scanning {ip}...")

    nmap_scan(ip)
    gobuster_scan(ip)
    if sub:
        wfuzz_scan(ip)
    comment_scan(ip)
    wappalyzer_scan(ip)

# nmap scan
@menu_decorator({"color": CYAN, "text": "Aggressiv NMAP SCAN" })
def nmap_scan(ip):
    print(subprocess.getoutput(f"nmap -A {ip}"))

# gobuster scan
@menu_decorator({"color": YELLOW, "text": "Gobuster Scan" })
def gobuster_scan(ip):
    global rec
    def scan_recursive(route='/'):
        if not route == '/':
            print(route)
        global subdirectories
        subdirectories.append(route)
        # output = subprocess.run(shlex.split(f"gobuster dir -u http://{ip}{route} -w /usr/share/wordlists/dirb/common.txt -t 100 --timeout 20s"), stdout=subprocess.PIPE).stdout.decode('utf-8')
        output = subprocess.run(shlex.split(f"gobuster dir -u http://{ip}{route} -w common.txt -t 100 --timeout 20s"), stdout=subprocess.PIPE).stdout.decode('utf-8')
        delete_line()
        output = output.split('\n')

        if rec:
            thread_list = []
            for name in get_dirnames(output):
                def scan_rec(route,name):
                    if route == '/':
                        scan_serial(f'{route}{name}')
                    else:
                        scan_serial(f'{route}/{name}')

                thread = threading.Thread(target=scan_rec, args=(route,name))
                thread_list.append(thread)
                thread.start()
            
            for thread in thread_list:
                thread.join()
        else:
            for name in get_dirnames(output):
                print(f'{route}{name}')
        
    scan_recursive()


def scan_serial(route):
    print(route)
    global subdirectories
    subdirectories.append(route)
    output = subprocess.run(shlex.split(f"gobuster dir -u http://{ip}{route} -w /usr/share/wordlists/dirb/common.txt -t 100 --timeout 20s"), stdout=subprocess.PIPE).stdout.decode('utf-8')
    # output = subprocess.run(shlex.split(f"gobuster dir -u http://{ip}{route} -w common.txt -t 100 --timeout 20s"), stdout=subprocess.PIPE).stdout.decode('utf-8')
    delete_line()
    output = output.split('\n')

    for name in get_dirnames(output):
        if len(name.split('.')) == 2:
            if name.split('.')[0] and name.split('.')[1]:
                if not name == 'index.html':
                    print(f'{route}/{name}')
                continue
        if route == '/':
            scan_serial(f'{route}{name}')
        else:
            scan_serial(f'{route}/{name}')


def get_dirnames(output):
    dirs = []
    for line in output:
        line = line.strip()
        if line.startswith('/'):
            line = line.split()[0].replace('/', '') # dirname without anything
            dirs.append(line)
    return dirs

def delete_line():
    sys.stdout.write('\033[F') #back to previous line
    sys.stdout.write('\033[K') #clear line


@menu_decorator({"color": BLUE, "text": "Subdomain Scan" })
def wfuzz_scan(ip):
    command = f'wfuzz -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://{ip}" -H "Host: FUZZ.{ip}"'
    print('Exclude Words --hw x (for example 290, check results)')
    print(command)
    print(subprocess.getoutput(command))

# comment scan
@menu_decorator({"color": GREEN, "text": "Comments Scan" })
def comment_scan(ip):

    def get_comments(ip,subdirectory):
        url = f"http://{ip}{subdirectory}"
        if not subdirectory:
            url = f"http://{ip}/"
        response = requests.get(url)
        html_comments = re.findall(r'\<\!\-\-(?:.|\n|\r)*?-->', response.text)
        css_js_comments = re.findall(r'(\/\*[\w\'\s\r\n\*]*\*\/)|(\/\/[\w\s\']*)|(\<![\-\-\s\w\>\/]*\>)', response.text)

        user_passwd = re.findall(r'[a-zA-Z][a-zA-Z0-9]+:[^: \&\.\~]*[a-zA-Z0-9]+[^:\&\.\~]+', response.text)


        def filter_comments(comments):
            if type(comments[0]) == tuple:
                return list(set([comment for tuplee in comments for comment in tuplee if comment]))
            else:
                return list(set(comments))
        
        print(f"\nComments for {url}")
        if html_comments:
            for comment in filter_comments(html_comments):
                print(comment)

        if css_js_comments:
            for comment in filter_comments(css_js_comments):
                print(comment)
        
        if user_passwd:
            for entry in user_passwd:
                print(entry)

    global subdirectories
    get_comments(ip, None)
    for subdirectory in subdirectories:
        get_comments(ip, subdirectory)

# wappalyzer scan
@menu_decorator({"color": PURPLE, "text": "Wappalyzer Scan" })
def wappalyzer_scan(ip):
    webpage = WebPage.new_from_url(f"http://{ip}/")
    wappalyzer = Wappalyzer.latest()
    parse_wappalyzer_result(wappalyzer.analyze_with_versions_and_categories(webpage))

def parse_wappalyzer_result(result):
    print(f"{'Name':<20} {'Category':<20} {'Name':20}")
    print()
    for key,inner_dict in result.items():
        key = str(key)
        versions = str(inner_dict['versions'])
        categories = str(inner_dict['categories'])
        print(f"{key:<20} {versions:<20} {categories:20}")

def print_colored_line(color):
    print(color + "---------------------------------------------------------------------------------" + '\033[0m')

def print_colored_string(color, string):
    print(color + string + '\033[0m')

if __name__ == '__main__':
    main()
