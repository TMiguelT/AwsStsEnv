#!/usr/bin/env python3
import json
import sys
import typing


def json_to_env(in_file: typing.io):
    parsed = json.load(in_file)
    return """export AWS_ACCESS_KEY_ID='{AccessKeyId}'
export AWS_SECRET_ACCESS_KEY='{SecretAccessKey}'
export AWS_SESSION_TOKEN='{SessionToken}'""".format(**parsed['Credentials'])


def main():
    print(json_to_env(sys.stdin))


if __name__ == '__main__':
    main()
