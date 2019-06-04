import psycopg2

try:
	conn_string = "host='localhost' dbname='mayur' user='postgres' password='Quad2core@'"
 
	# print the connection string we will use to connect
	print(f"Connecting to database {conn_string}")
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print("connected")
except:
    print("I am unable to connect to the database")