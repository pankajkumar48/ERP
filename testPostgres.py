import psycopg2

try:
    # Database credentials
    hostname = 'localhost'
    username = 'pankaj kumar'
    password = 'Quad2core@'
    database = 'postgres'
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
    # create a new cursor object
    cur = conn.cursor()
    # execute the INSERT statement
    cur.execute("select * from karche;")
    # commit the changes to the database
    conn.commit()
    # close the communication with the PostgresQL database
    cur.close()
    res = "Successfully Inserted"
except (Exception, psycopg2.DatabaseError) as error:
    print("hi")
    print(error)
finally:
    if conn is not None:
        conn.close()