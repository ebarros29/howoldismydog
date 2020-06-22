from flask import Flask, request, render_template, jsonify, redirect, url_for
from pymongo import MongoClient

import dog_human_age

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calc_hoimd', methods = ['GET'])
def hoimd():
    d_breed = request.args.get('dog_breed')
    d_age = request.args.get('dog_age')
    d_size = request.args.get('dog_size')
    #d_breed = request.form['dog_breed']
    #d_age = request.form['dog_age']
    #d_size = request.form['dog_size']

    response = dog_human_age.get_human_age(d_breed, d_age, d_size)
        #response = 'error'
    if response != 'error':
        #return render_template('calc_hoimd.html')
        return render_template('calc_hoimd.html', response=response)
    else:
        return render_template('bnf.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
