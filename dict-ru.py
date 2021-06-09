#!/usr/bin/python3


import argparse as ap
import requests as rq
import json as j


parser = ap.ArgumentParser(description="Uses api.dictionaryapi to define Russian words in Russian")


# parser.add_argument("query", help="Dict term for definition", type=str)


# args = parser.parse_args()


# result = rq.get(f'https://api.dictionaryapi.dev/api/v2/entries/ru/{args.query}')

result = rq.get('https://api.dictionaryapi.dev/api/v2/entries/ru/рот')


json_payload = result.json()


result_dict = json_payload[0]


print(result_dict)

print(type(result_dict))







