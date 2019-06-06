import json
from numpy import dot
from numpy.linalg import norm
import random


def cos_sim(compare_vector):
    json_object = json.load(open("vectors.json"))
    final_listing = []
    for item in json_object:
        curr_vector = json_object[item]
        cos_sim = dot(compare_vector, curr_vector)/(norm(compare_vector)*norm(curr_vector))
        final_values = (cos_sim, item)
        final_listing.append(final_values)

    sorted_list = sorted(final_listing, key=lambda x: x[0], reverse=True)
    return sorted_list[1:30]

def process_results(sorted_list):
    charity_dict = json.load(open("charity_dict.json"))
    count_dict = {}
    for _,user in sorted_list:
        charity_list = charity_dict[user]
        for charity in charity_list:
            curr_tup = (charity[0], charity[1])
            count_dict[curr_tup] = count_dict.setdefault(user, 0) + 1
    sorted_count = sorted(count_dict.keys(), key=lambda k:count_dict[k], reverse=True)[:5]
    return sorted_count

def find_charities(input_vector):
    sorted_list = cos_sim(input_vector)
    return process_results(sorted_list)

def similar_charities(curr_charities):
    charity_dict = json.load(open("charities.json"))
    categories = []
    for charity in curr_charities:
        for key in charity_dict.keys():
            curr_list = [charity[0], charity[1]]
            if curr_list in charity_dict[key]:
                categories.append((charity, key))
                break

    final_lst = []
    for category_tup in categories:
        curr_charity = category_tup[0]
        curr_category = category_tup[1]
        charity_list = charity_dict[curr_category]
        suggestion = random.choice(charity_list)
        final_lst.append((suggestion, curr_charity))
    return final_lst








if __name__ == '__main__':
    json_object = json.load(open("vectors.json"))
    list_thing = [0.10595888622531335, 0.12871396130095566, 0.08370241990531156, 0.07106857129701835, 0.05154500829473249, 0.06209479430027622, 0.09581375251099884, 0.09152323794243412, 0.07622712553626515, 0.12178292573936854, 0.11156931694732596, 0.013850855377684329, 0.02382106281584868, 0.011730685945155795, 0.01652059633922003, 0.006106973419273493, 0.028475597194174664, 0.015832402131306475, 0.01428551470728577, 0.011313538919915841, 0.0378347432706019, 0.015710307919437894, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
    curr_charities = [('http://www.oasisnet.org/', 'OASIS Institute'), ('http://www.globalfundforwomen.org/', 'Global Fund for Women'), ('http://www.wings-of-hope.org/', 'Wings of Hope'), ('http://www.easterseals.com/site/PageServer', 'Easter Seals'), ('http://www.covenanthouse.org/', 'Covenant House')]
