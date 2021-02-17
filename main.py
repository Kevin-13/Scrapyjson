# -*- coding: utf8 -*-
import random
import json
import scrapy


def read_value_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values


def get_random_items(my_list):
    rand_num = random.randint(0, len(my_list) - 1)
    item = my_list[rand_num]
    return item


def get_random_char():
    all_values = read_value_from_json('characters.json', 'character')
    return get_random_items(all_values)


def get_random_quotes():
    all_values = read_value_from_json('quotes.json', 'quote')
    return get_random_items(all_values)


def message(character, quote):
    return "{} a dit : {}".format(character, quote)


user_answer: str = input("Voulez vous une nouvelle citation ? (B pour quitter)")

while user_answer != "B":
    print(message(get_random_char(), get_random_quotes()))
    user_answer: str = input("Voulez vous une nouvelle citation ? (B pour quitter)")
