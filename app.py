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

@app.route('/addVendors', methods=['GET'])
def addVendors():
	return render_template('addVendors.html')

@app.route('/updateVendors', methods=['GET'])
def updateVendors():
	return render_template('updateVendors.html')

@app.route('/deleteVendors', methods=['GET'])
def deleteVendors():
	return render_template('deleteVendors.html')


@app.route('/generateBill', methods=['GET'])
def generateBill():
	return render_template('generateBill.html')

@app.route('/allTransactions', methods=['GET'])
def allTransactions():
	return render_template('allTransactions.html')

if __name__ == '__main__':
	app.run(debug=True)
