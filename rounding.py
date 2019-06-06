import json

user_info = json.load(open("app/accounts.json"))

def round(user_id, amount=1):
	'''
	user_id: (str) 
	amount: (int) nearest dollar amount to round to
	returns: (2 decimal float) amount of money (in dollars/cents) that will be donated
	'''
	info  = user_info[user_id]
	return sum((amount-charge%amount) for category, charge, date in info['trans'] if charge%amount >= amount/2)

	
# print(round('User0', 5))