#!/usr/bin/env python3

import readline
import glob


def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]


readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)


def main():
    service = check_target(input("http-post-form(hpf) / ssh (s) / ftp (f): "))
    username = check_username(input('username or list: '))
    password = check_password(input('password or list: '))
    ip = input('ip: ')
    port = check_port(input(f'port (default {service} ): '), service)
    threads = check_threads(input('threads (default 64): '))
    if service == 'http-post-form':
        route = check_route(input('route (default /): '))
        payload = input('payload (set parameter ^USER^, ^PASS^): ')
        error_msg = input('error message: ')
        print(f'hydra {username} {password} {ip} {port} {service} "{route}:{payload}:{error_msg}" -t {threads}')
    else:
        print(f"hydra {username} {password} {ip} {port} {service} -t {threads}")


def check_target(user_input):
    if user_input == 'hpf':
        return "http-post-form"
    elif user_input == 's':
        return "ssh"
    elif user_input == 'f':
        return "ftp"
    else:
        print("Invalid service")
        return


def check_username(user_input):
    if "/" in user_input:
        return f"-L {user_input}"
    else:
        return f"-l {user_input}"


def check_password(user_input):
    if "/" in user_input:
        return f"-P {user_input}"
    else:
        return f"-p {user_input}"

def check_port(user_input, service):
    if user_input == '':
        if service == 'http-post-form':
            return "-s 80"
        elif service == 'ssh':
            return "-s 22"
        elif service == 'ftp':
            return "-s 21"
    else:
        return f"-s {user_input}"

def check_threads(user_input):
    if user_input == '':
        return '64'
    else:
        return user_input

def check_route(user_input):
    if user_input == '':
        return '/'
    else:
        return user_input

if __name__ == '__main__':
    main()
