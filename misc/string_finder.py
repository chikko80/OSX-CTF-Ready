#!/usr/bin/env python3

import os
from multiprocessing import Pool
import subprocess
import argparse

interesting_paths = ['config']

parser = argparse.ArgumentParser(description='This programm finds all files containing the specified string')
parser.add_argument('directory', help='directory to start')
parser.add_argument('-s', '--string', help='string to find', required=True)
args = parser.parse_args()
dir_name = args.directory
string = args.string

def print_banner():
    return """
  █████████   █████               ███                     
 ███░░░░░███ ░░███               ░░░                      
░███    ░░░  ███████   ████████  ████  ████████    ███████
░░█████████ ░░░███░   ░░███░░███░░███ ░░███░░███  ███░░███
 ░░░░░░░░███  ░███     ░███ ░░░  ░███  ░███ ░███ ░███ ░███
 ███    ░███  ░███ ███ ░███      ░███  ░███ ░███ ░███ ░███
░░█████████   ░░█████  █████     █████ ████ █████░░███████
 ░░░░░░░░░     ░░░░░  ░░░░░     ░░░░░ ░░░░ ░░░░░  ░░░░░███
                                                  ███ ░███
                                                 ░░██████ 
                                                  ░░░░░░  
 ███████████  ███                 █████                   
░░███░░░░░░█ ░░░                 ░░███                    
 ░███   █ ░  ████  ████████    ███████   ██████  ████████ 
 ░███████   ░░███ ░░███░░███  ███░░███  ███░░███░░███░░███
 ░███░░░█    ░███  ░███ ░███ ░███ ░███ ░███████  ░███ ░░░ 
 ░███  ░     ░███  ░███ ░███ ░███ ░███ ░███░░░   ░███     
 █████       █████ ████ █████░░████████░░██████  █████   
    """

def main():
    global dir_name
    print_banner()
    print("-------------------------------------------------------------")
    print("This programm finds all files containing the specified string")
    print("-------------------------------------------------------------")
    files = get_all_files(dir_name)

    with Pool() as pool:
        results = pool.map(check_if_in_file, files)


def gprint(string):
    print('\033[92m' + string + '\033[0m')

def rprint(string):
    print('\033[91m' + string + '\033[0m')

def check_if_in_file(file_name):
    global string
    encoding = get_file_encoding(file_name)
    if encoding:
        try:
            check_file(file_name, string, encoding)
        except (UnicodeDecodeError, LookupError):
            try:
                check_file(file_name, string, 'utf-8')
            except UnicodeDecodeError:
                pass

def check_file(file_name,string,encoding):
    with open(file_name,mode='r', encoding=encoding) as reader:
        if string.lower() in reader.read().lower():
            if any(subpath in file_name for subpath in interesting_paths):
                rprint(file_name)
            else:
                gprint(file_name)

            with open(file_name,mode='r', encoding=encoding) as inner:
                for line in inner:
                    if string.lower() in line.lower():
                        if len(line) > 200:
                            print(line[:200].strip())
                        else:
                            print(line.strip())
                print()
            return True
    return False

def get_file_encoding(file_name):
    output = subprocess.run(['file', '-ib', file_name], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    if output == 'regular file':
        return 'utf-8'
    else:
        try:
            encoding = [string for string in output.split(' ') if string.startswith('charset=')][0].split('=')[1]
        except IndexError:
            print('Index Error', file_name)
            return False
        if encoding == 'binary': # filter binary file
            return False
        return encoding


#iterate over directory
def get_all_files(start_directory):
    all_files = []
    for root, dirs, files in os.walk(start_directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files



if __name__ == '__main__':
    main()