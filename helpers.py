import flask
from flask import request, jsonify, render_template, url_for
import json
import datetime
import psycopg2


# This method returns Vendor name & Card No for poplulating in search bar
def getSearchBarData():
	conn = None
	try:
		hostname = 'localhost'
		username = 'pankaj kumar'
		password = 'quad2core'
		database = 'postgres'
		conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
		cur = conn.cursor()
		cur.execute("select vendorname, cardno from vendors")
		allNames = cur.fetchall()
		conn.commit()
		cur.close()
		names = []
		for al in allNames:
			names.append(al[0] + " : " + str(al[1]))
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		res = str(error)
	finally:
		if conn is not None:
			conn.close()
	return names
