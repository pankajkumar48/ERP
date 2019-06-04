#An ERP project

import flask
from flask import request, jsonify, render_template, url_for
import json
import datetime
import psycopg2

app = flask.Flask(__name__,static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return render_template('home.html')

@app.route('/vendors', methods=['GET'])
def vendors():
	return render_template('vendors.html')

@app.route('/generateBill', methods=['GET'])
def generateBill():
	return render_template('generateBill.html')

@app.route('/allTransactions', methods=['GET'])
def allTransactions():
	return render_template('allTransactions.html')

if __name__ == '__main__':
	app.run(debug=True)
