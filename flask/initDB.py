import psycopg2

def connect():
	conn = psycopg2.connect(
	    host="db",
	    database="test_db",
	    user="test",
	    password="aytjdfviuran9ce9829")
	
	return conn

def init():
	con = connect()
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS testTable (id INTEGER PRIMARY KEY)")
	cur.execute("INSERT INTO testTable VALUES(1) ON CONFLICT (id) DO UPDATE SET id=2")
	con.commit()
