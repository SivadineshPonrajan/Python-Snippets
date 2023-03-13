# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:02:43 2018

@author: Avis_King
"""

import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        yn =yn.upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist in the data source"

word = input("Enter the word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)