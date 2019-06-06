import json
import datetime, time
import processing_vector

listing = ['Retail Outlet', 'Agricultural', 'Government', 'Transportation', 'Miscellaneous', 'Clothing', 'Professional Services and Membership', 'Travel', 'Business', 'Contracted', 'Utility']
other_vector_stuff = {"Asian": 0, "White":1, "Hispanic/Latino":2, "Pacific Islander":3, "Native American":4, "Other":5, "Did not Disclose":6, "M":7, "F":8, "O":9}
lower_bound = time.time() - 30*24*3600

test_user_dict = json.load(open("test_user_info.json"))
test_user_vector = []
curr_dict = dict((el,0) for el in listing)
thirty_days_dict = dict((el,0) for el in listing)
total_money = 0
total_thirty_day_money = 0

for trans in test_user_dict["trans"]:
    curr_cat = trans[0]
    curr_price = trans[1]
    curr_date = trans[2]
    curr_dict[curr_cat] += curr_price
    total_money += curr_price
    if curr_date > lower_bound and curr_date < time.time():
        thirty_days_dict[curr_cat] += curr_price
        total_thirty_day_money += curr_price

for item in curr_dict:
    curr_dict[item] = curr_dict[item]/total_money
    test_user_vector.append(curr_dict[item])

for item in thirty_days_dict:
    thirty_days_dict[item] = thirty_days_dict[item]/total_money
    test_user_vector.append(thirty_days_dict[item])

other_list = [0 for i in range(20)]
other_list[other_vector_stuff[test_user_dict['gender']]] = 1
other_list[other_vector_stuff[test_user_dict['race']]] = 1
age_bracket = (test_user_dict['age'] - 15)//17
other_list[age_bracket + 10] = 1
money_bracket = (test_user_dict['total_money'])//50000
other_list[money_bracket + 15] = 1
test_user_vector = test_user_vector + other_list

with open('test_user_vector.json', 'w') as tv:
	json.dump(test_user_vector, tv)