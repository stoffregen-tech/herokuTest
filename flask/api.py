from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
import json
import psycopg2
import initDB

app = Flask(__name__)
path = "/usr/src/app/json/"

@app.route('/json/test',methods=['GET'])
def test():
	con = initDB.connect()
	cur = con.cursor()
	cur.execute('SELECT id FROM testTable')
	res = cur.fetchone()
	return jsonify(res)

if __name__ == "__main__":
	initDB.init()
	app.run(host="0.0.0.0", port="5001", debug=True)