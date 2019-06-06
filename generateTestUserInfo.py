import random
import json
from datetime import datetime, date, time

# https://www.citibank.com/tts/solutions/commercial-cards/assets/docs/govt/Merchant-Category-Codes.pdf
categories = ['Agricultural', 'Contracted', 'Transportation', 'Utility', 'Retail Outlet',
				'Clothing', 'Miscellaneous', 'Business', 'Professional Services and Membership',
				'Government', 'Travel']

gender = ["M", "F", "O"]
race = ["Asian", "White", "Hispanic/Latino", "Pacific Islander", "Native American", "Other", "Did not Disclose"]

starting_date = datetime(2019,1,1,0,0).timestamp()

test_trans_list = []
for j in range(200):
	starting_date += 65000
	test_trans_list.append([random.choice(categories), round(random.uniform(0, 1000), 2), starting_date])
# print(test_trans_list)
test_user = {'trans': test_trans_list, 'gender': random.choice(gender), 'race': random.choice(race), 
			 'age': random.randint(16, 110), 'total_money': (random.randint(5, 250000))}

with open('test_user_info.json', 'w') as tu:
	json.dump(test_user, tu)