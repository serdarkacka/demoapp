from flask import Flask
from flask import render_template
from flask import request
from algorithm import *

import yaml


app = Flask(__name__)

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/compute', methods=['GET','POST'])
def compute():
	if request.method == 'GET':
		return render_template('compute.html')
	else:
		input1 = request.form['input1']
		input2 = request.form['input2']
		input3 = request.form['input3']

		array = yaml.safe_load(input1)
		f = int(input2)
		t = int(input3)

		result = concat(array, f, t)
		print result
		return render_template('compute.html', result=result)

if __name__ == "__main__":
	app.run()
