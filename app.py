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

@app.route('/addVendorToDB', methods=['POST'])
def addVendorToDB():
	vendorName = request.form.get("vendorName")
	vendorRate = request.form.get("vendorRate")
	vendorAddress = request.form.get("vendorAddress")
	print(f"{vendorName}, {vendorRate} \n {vendorAddress}")
	return jsonify("successfully received")

@app.route('/addVendor2DB', methods=['POST'])
def addVendor2DB():
	vendorName = request.form.get("vendorName")
	vendorRate = float(request.form.get("vendorRate"))
	vendorAddress = request.form.get("vendorAddress")
	cardNo = int(request.form.get("cardNo"))
	others = request.form.get("others")
	product = request.form.get("inputProduct")

	if product == 'others':
		product = others
	print(vendorName)
	print(vendorRate)
	print(vendorAddress)
	print(cardNo)
	print(others)
	print(product)
	print("Insertion happening")
	res = "Starting insertion"
	conn = None
	try:
		hostname = 'localhost'
		username = 'pankaj kumar'
		password = 'quad2core'
		database = 'postgres'
		conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
		cur = conn.cursor()
		cur.execute("INSERT INTO vendors(cardNo, vendorName, vendorAddress, vendorRate, item) VALUES(%s,%s,%s,%s,%s)",(cardNo, vendorName, vendorAddress, vendorRate, product))
		conn.commit()
		cur.close()
		res = "Successfully Inserted"
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		res = str(error)
	finally:
		if conn is not None:
			conn.close()
			#res = "successfully inserted"
	return jsonify(res)

if __name__ == '__main__':
	app.run(debug=True)
