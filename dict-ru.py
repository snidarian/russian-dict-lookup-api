#!/usr/bin/python3


import argparse as ap
import requests as rq
import json as j


parser = ap.ArgumentParser(description="Uses api.dictionaryapi to define Russian words in Russian")


parser.add_argument("query", help="Dict term for definition", type=str)


args = parser.parse_args()


result = rq.get(f'https://api.dictionaryapi.dev/api/v2/entries/ru/{args.query}')


print(result.text)


json_object = result.json()

print(type(json_object))

    





