from flask import Flask, render_template, request
from roller_processing import compute_successes, count_successes
app = Flask(__name__)

@app.route('/')
def roller():
	return render_template("index.html")

@app.route('/recieve_pool', methods=["POST"])
def recieve_pool():
	pool = request.form['pool']
	pool = int(pool) if pool else 0
	successes = compute_successes(pool)
	return render_template("result.html", 
		successes = successes, count = count_successes(successes))
