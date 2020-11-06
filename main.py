from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

'''
pip3 install flask-sqlalchemy
python3 terminal:
	from api import db
	db.create_all()
	exit()
Admin:12345
'''

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class IprCheck(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nama_ipr = db.Column(db.String(50))
	max_umur_pemohon = db.Column(db.String(50))
	min_umur_pemohon = db.Column(db.String(50))
	jantina_pemohon = db.Column(db.String(50))
	status_pemohon = db.Column(db.String(50))
	negeri_kelahiran_pemohon = db.Column(db.String(50))
	mastautin_pemohon = db.Column(db.String(50))
	max_pendapatan_pemohon = db.Column(db.String(50))
	min_pendapatan_pemohon = db.Column(db.String(50))
	jantina_pasangan = db.Column(db.String(50))
	max_umur_pasangan = db.Column(db.String(50))
	min_umur_pasangan = db.Column(db.String(50))
	max_gaji_pasangan = db.Column(db.String(50))
	min_gaji_pasangan = db.Column(db.String(50))
	bilangan_anak = db.Column(db.String(50))
	ipr_status = db.Column(db.String(50))


@app.route('/api/check', methods=['POST'])
def api_check():
	# nama
	# tarikh lahir
	# jantina
	# mastautin
	# tempat lahir
	# gaji
	# pendapatan isi rumah
	# status kahwin

	# nama pasangan
	# tarikh lahir pasangan
	# jantina pasangan
	# gaji

	# bilangan anak

	# dalam db akan ada max gaji & min gaji
	# status kahwin
	# max umur dan min umur
	# nama ipr


	return jsonify({'message' : 'api'})

@app.route('/')
def main_page():

	return render_template('home.html')

@app.route('/result')
def result_page():

	return render_template('result.html')

if __name__ == '__main__':
	app.run(port=8000, debug=True)