import json
from pymongo import MongoClient
import re

# Connect pymongo to MongoDB
client = MongoClient('mongo', 27017)
db = client['dogs_db']
coll_raca = db['racas']

def get_human_age(dog_breed, dog_age, dog_size):
    x=[]
    id_c = int(dog_age)

    human_age = [0, 15, 24, 28, 32, 36, 
                [40, 42, 45], [44, 47, 50], 
                [48, 51, 55], [52, 56, 61],
                [56, 60, 66], [60, 65, 72],
                [64, 69, 77], [68, 74, 82],
                [72, 78, 88], [76, 83 ,93],
                [80, 87, 120]]

    mydict=coll_raca.find({'$text': {'$search': "\"%s\"" % (dog_breed)}})

    for x in mydict:
        print(x)

    if len(x) == 0:
        return "error"

    if dog_size == "":
        dog_size = x['porte']
    else:
        dog_size = dog_size

    if id_c <= 5:
        return x['raca'], human_age[id_c], x['origem'], x['personalidade']

    elif 5 < id_c <= 16:
        regexP = re.compile('(P|p)equeno')
        regexM = re.compile('(M|m)(e|é)dio')
        regexG = re.compile('(G|g)rande')
        if regexP.match(dog_size):
            return x['raca'], human_age[id_c][0], x['origem'], x['personalidade']
        elif regexM.match(dog_size):
            return x['raca'], human_age[id_c][1], x['origem'], x['personalidade']
        elif regexG.match(dog_size):
            return x['raca'], human_age[id_c][2], x['origem'], x['personalidade']
    else:
        return "Error"

#response = get_human_age("aki", 5, "")

#print(response)
