import json
import unittest
import os
import requests

API_KEY = 'd6138d2114b64120b05c0cbdb7c92f60'


def read_cache(CACHE_FNAME):
    """
    This function reads from the JSON cache file and returns a dictionary from the cache data.
    If the file doesn't exist, it returns an empty dictionary.
    """
    try:
        cache_file = open(CACHE_FNAME, 'r', encoding="utf-8") # Try to read the data from the file
        cache_contents = cache_file.read()  # If it's there, get it into a string
        CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
        cache_file.close() # Close the file, we're good, we got the data in a dictionary.
        return CACHE_DICTION
    except:
        CACHE_DICTION = {}
        return CACHE_DICTION

def write_cache(CACHE_FNAME, CACHE_DICT):
    """
    This function encodes the cache dictionary (CACHE_DICT) into JSON format and
    writes the JSON to the cache file (CACHE_FNAME) to save the search results.
    """
    with open(CACHE_FNAME, 'w') as f:
        json.dump(CACHE_DICT, f)

#spoontacular API
cuisine_list = ["African", "American", "British", "Cajun", "Caribbean", "Chinese", "Eastern European", "European",
"French", "German", "Greek", "Indian", "Irish", "Italian", "Japanese", "Jewish", "Korean", "Latin American", 
"Mediterranean", "Mexican", "Middle Eastern", "Nordic", "Southern", "Spanish", "Thai", "Vietnamese"]


food = input("What food are you looking for?")
while True:
    c = input("What cuisine are you looking for?")
    c = c[0].upper() + c[1:]
    if c in cuisine_list:
        cuisine = c
        break
    else:
        print("Sorry, try again")
num = '10'
base_url = 'https://api.spoonacular.com/'
params = "?apiKey=" + API_KEY + "?query" + food + "?cuisine" + cuisine + "?number" + num
r = requests.get((base_url + params))
data = json.loads(r.text)
print(data)


#Tasty API 



