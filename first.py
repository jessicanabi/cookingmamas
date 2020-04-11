import json
import unittest
import os
import requests

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
num = '3'
base_url = 'https://api.spoonacular.com/recipes/search'
params = "?query" + food + "?cuisine" + cuisine + "?number" + num