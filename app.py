from flask import Flask, request, render_template, jsonify, redirect, url_for
from pymongo import MongoClient

import dog_human_age

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/api/calc_hoimd', methods=['GET', 'POST'])
def hoimd():
    if request.method == 'POST':
        # Then get the data from the form
        d_breed = request.form['dog_breed']
        d_age = request.form['dog_age']
        d_size = request.form['dog_size']

        response = dog_human_age.get_human_age(d_breed, d_age, d_size)
        
        return render_template('calc_hoimd.html', response=response)

    # Otherwise this was a normal GET request
    else:   
        return render_template('main.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
