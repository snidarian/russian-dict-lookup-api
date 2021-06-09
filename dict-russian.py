#!/usr/bin/python3


import argparse as ap
import requests as rq
import json as j


parser = ap.ArgumentParser(description="Uses dictionaryapi to define Russian words in Russian")


parser.add_argument("query", help="Dict term for definition", type=str)



result = rq.get('https://api.dictionaryapi.dev/api/v2/entries/ru/рот')


#print(result.text)


json_object = result.json()

print(type(json_object))

    





