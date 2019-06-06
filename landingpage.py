from flask import Flask, render_template
from processing_vector import find_charities,similar_charities
import json
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/give_back')
def give_back():
    json_object = json.load(open("test_user_vector.json"))
    people_to_charities = json.load(open("charity_dict.json"))
    print(people_to_charities.keys())
    personal_charities = []
    if "personal_charities" in people_to_charities.keys():
        personal_charities = people_to_charities["personal_charities"]
    returned_charities_from_others = find_charities(json_object)
    return render_template('extended.html', charity_list=returned_charities_from_others)


if __name__ == '__main__':
    app.run(debug=True)
