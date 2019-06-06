import random
import json
from datetime import datetime, date, time


# https://www.citibank.com/tts/solutions/commercial-cards/assets/docs/govt/Merchant-Category-Codes.pdf
categories = ['Agricultural', 'Contracted', 'Transportation', 'Utility', 'Retail Outlet',
				'Clothing', 'Miscellaneous', 'Business', 'Professional Services and Membership',
				'Government', 'Travel']

gender = ["M", "F", "O"]
race = ["Asian", "White", "Hispanic/Latino", "Pacific Islander", "Native American", "Other", "Did not Disclose"]
accounts = {}
for i in range(10000):
	accounts['User'+str(i)] = {}
	starting_date = datetime(2019,1,1,0,0).timestamp()
	trans_list = []
	for j in range(200):
		starting_date += 65000
		trans_list.append([random.choice(categories), round(random.uniform(0, 1000), 2), starting_date])
	accounts["User" + str(i)]['trans'] = trans_list
	accounts['User'+str(i)]['gender']=(random.choice(gender))
	accounts['User'+str(i)]['race']=(random.choice(race))
	accounts['User'+str(i)]['age']=(random.randint(16,110))
	accounts['User'+str(i)]['total_money']=(random.randint(5, 250000))



with open('accounts.json', 'w') as fp:
	json.dump(accounts, fp)
