import json, re, requests
from pymongo import MongoClient

# Connect pymongo to MongoDB
client = MongoClient('mongo', 27017)
db = client['dogs_db']
coll_raca = db['racas']

def get_human_age(dog_breed, dog_age, dog_size):

    id_c = int(dog_age)

    human_age = [0, 15, 24, 28, 32, 36, 
                [40, 42, 45], [44, 47, 50], 
                [48, 51, 55], [52, 56, 61],
                [56, 60, 66], [60, 65, 72],
                [64, 69, 77], [68, 74, 82],
                [72, 78, 88], [76, 83 ,93],
                [80, 87, 120]]
    
    regexP = re.compile('(P|p)equeno')
    regexM = re.compile('(M|m)(e|é)dio')
    regexG = re.compile('(G|g)rande')
    
    if regexP.match(dog_size):
        dog_size = 'pequeno' 
    if regexM.match(dog_size):
        dog_size = 'medio'
    if regexG.match(dog_size):
        dog_size = 'grande'
    
    #finding dog breed and size
    mydict=coll_raca.find_one({'$text': {'$search': '"%s" "%s"' % (dog_breed, dog_size)}})
    
    #print(mydict)

    if mydict != None:
        try:    
            res = requests.get(mydict['api_uri']).json()
            dog_img_url = res['message']
        except:
            dog_img_url = mydict['api_uri']
        if dog_size == "":
            dog_size = mydict['porte']
        else:
            dog_size = dog_size

        if id_c <= 5:
            return mydict['raca'], human_age[id_c], mydict['origem'], mydict['personalidade'], dog_img_url

        elif 5 < id_c <= 16:

            if dog_size == "pequeno":
                return mydict['raca'], human_age[id_c][0], mydict['origem'], mydict['personalidade'], dog_img_url
            elif dog_size == "medio":
                return mydict['raca'], human_age[id_c][1], mydict['origem'], mydict['personalidade'], dog_img_url
            elif dog_size == "grande":
                return mydict['raca'], human_age[id_c][2], mydict['origem'], mydict['personalidade'], dog_img_url
        else:
            return "error"
    else:
        return "error"

#response = get_human_age('poodle', 4, 'pequeno')
#print(response)
