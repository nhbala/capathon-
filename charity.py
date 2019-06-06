import json
import random

json_object = json.load(open("vectors.json"))
charity_object = json.load(open("charities.json"))
charity_dict = {}
for person_vector in json_object:
    charity_list = []
    for i in range(5):
         key_list = list(charity_object.keys())
         curr_cat = random.choice(key_list)
         curr_charity_list = charity_object[curr_cat]
         curr_charity = random.choice(curr_charity_list)
         charity_list.append(curr_charity)
    charity_dict[person_vector] = charity_list

with open('charity_dict.json', 'w') as fp:
	json.dump(charity_dict, fp)
