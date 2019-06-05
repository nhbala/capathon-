import random
import json

# https://www.citibank.com/tts/solutions/commercial-cards/assets/docs/govt/Merchant-Category-Codes.pdf
categories = ['Agricultural', 'Contracted', 'Transportation', 'Utility', 'Retail Outlet', 
				'Clothing', 'Miscellaneous', 'Business', 'Professional Services and Membership',
				'Government', 'Travel']


accounts = {}
for i in range(5):
	accounts['User'+str(i)] = []
	for j in range(100):
		accounts['User'+str(i)].append((random.choice(categories), round(random.uniform(0, 1000), 2)))

with open('accounts.json', 'w') as fp:
	json.dump(accounts, fp)