from flask import Flask, render_template
from processing_vector import find_charities
import json
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/give_back')
def give_back():
    json_object = json.load(open("test_user_vector.json"))
    returned_charities = find_charities(json_object)
    return render_template('extended.html', charity_list=returned_charities)

@app.route('/about_us')
def about_us():
	# return 'Authors: Seri Choi, Hannah Chang, Nathan Bala, Rohit Mandavia, and Winnie Wang'
	return render_template('aboutus.html')

if __name__ == '__main__':
    app.run(debug=True)
