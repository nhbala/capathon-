import json

user_info = json.load(open("app/accounts.json"))

def round(user_id, amount=1, minimum_charge=0, percentage=None, categories=None):
	'''
	user_id: (str) 
	amount: (int) nearest dollar amount to round to
	minimum_charge: smallest charge that will be rounded for donation
	percentage: if None, will calculate donations from rounding to the nearest dollar amount; 
		else will calculate percentage of transactions to donate (float from 0 to 1)
	categories: (set) categories of purchases that you want to donate money from
	returns: (2 decimal float) amount of money (in dollars/cents) that will be donated
	'''
	info  = user_info[user_id]
	transactions = info['trans']
	donation = 0
	for category, charge, date in transactions:
		if categories!=None and category not in categories:
			continue
		elif not percentage:
			remainder = charge%amount
			if remainder>=amount/2 and charge>=minimum_charge:
				donation += (amount - remainder)
		else:
			donation += percentage*charge
	return donation

	
# #Tests
# print(round('User0', 5))
# print(round('User0'))
# print(sum(charge for _, charge, _ in user_info['User0']['trans']))
# print(round('User0', percentage=.1))
# print(round('User0', percentage=.1, categories=['Travel', 'Clothing']))
# print(sum(charge for category, charge, _ in user_info['User0']['trans'] if category in {'Travel', 'Clothing'}))