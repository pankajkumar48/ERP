#An ERP project

import flask
from flask import request, jsonify, render_template, url_for
import json
import datetime
import psycopg2
from helpers import getSearchBarData

app = flask.Flask(__name__,static_url_path='',
			static_folder='static',
			template_folder='templates')
app.config["DEBUG"] = True

hostname = 'localhost'
username = 'postgres'
password = '1234'
database = 'postgres'
conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
cur = conn.cursor()

@app.route('/', methods=['GET'])
def home():
	names = getSearchBarData()
	return render_template('home.html', names=names)



@app.route('/addVendors', methods=['GET', 'POST'])
def addVendors():
	if request.method == 'GET':
		names = getSearchBarData()
		return render_template('addVendors.html', names=names)
	if request.method == 'POST':
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
		# conn = None
		try:
			# conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
			# cur = conn.cursor()
			cur.execute("INSERT INTO vendors(cardNo, vendorName, vendorAddress, vendorRate, item) VALUES(%s,%s,%s,%s,%s)",(cardNo, vendorName, vendorAddress, vendorRate, product))
			conn.commit()
			# cur.close()
			res = "Successfully Inserted"
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			res = str(error)
		finally:
			if conn is not None:
				# conn.close()
				res = "successfully inserted"
		return jsonify(res)

@app.route('/updateVendors', methods=['GET', 'POST'])
def updateVendors():
	if request.method == 'GET':
		names = getSearchBarData()
		return render_template('updateVendors.html', names=names)
	if request.method == 'POST':
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
		# conn = None
		try:
			# conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
			# cur = conn.cursor()
			cur.execute("UPDATE vendors SET vendorName = %s, vendorAddress = %s, vendorRate = %s, item = %s WHERE cardno = %s",(vendorName, vendorAddress, vendorRate, product, cardNo))
			conn.commit()
			# cur.close()
			res = "Successfully Inserted"
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			res = str(error)
		finally:
			if conn is not None:
				# conn.close()
				res = "successfully updated"
		return jsonify(res)


@app.route('/deleteVendors', methods=['GET','POST'])
def deleteVendors():
	if request.method == 'GET':
		names = getSearchBarData()
		return render_template('deleteVendors.html', names=names)
	if request.method == 'POST':
		cardNo = str(request.form.get("cardNo"))
		try:
			cur.execute(f"delete from vendors where cardno = {cardNo}")
			# allVendorData = cur.fetchall()
			conn.commit()
			res = 'successfully deleted'
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
			res = str(error)
		finally:
			if conn is not None:
				# conn.close()
				print("Used delete")
		return jsonify(res)



@app.route('/generateBill', methods=['GET'])
def generateBill():
	names = getSearchBarData()
	return render_template('generateBill.html', names=names)

@app.route('/allTransactions', methods=['GET'])
def allTransactions():
	names = getSearchBarData()
	return render_template('allTransactions.html', names=names)


# This is used to populate data after doing a search from search bar
@app.route('/getFormAfterSearch', methods=['POST'])
def getFormAfterSearch():
	vendorString = request.form.get("vendorString")
	print(vendorString)
	vendorString = vendorString.split(':')
	vendorCardNo = vendorString[1].strip()

	# conn = None
	try:
		# conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
		# cur = conn.cursor()
		cur.execute(f"select * from vendors where cardno = {vendorCardNo}")
		allVendorData = cur.fetchall()
		conn.commit()
		# cur.close()

		resDict = {}
		resDict['cardNo'] = allVendorData[0][0]
		resDict['vendorName'] = allVendorData[0][1]

		temp = allVendorData[0][2]
		temp = temp.split(',')
		temp = [t.strip() for t in temp]
		resDict['inputAddress1'] = temp[0]
		resDict['inputAddress2'] = temp[1]
		resDict['inputCity'] = temp[2]
		resDict['inputState'] = temp[3]
		resDict['inputZip'] = temp[4]

		resDict['vendorRate'] = allVendorData[0][3]
		resDict['item'] = allVendorData[0][4]

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		resDict = str(error)
	finally:
		if conn is not None:
			# conn.close()
			print("Used search")
	return jsonify(resDict)





if __name__ == '__main__':
	app.run(debug=True)
