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
	kod_ipr = db.Column(db.String(50))
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
	masih_belajar = db.Column(db.String(50))
	ipr_status = db.Column(db.String(50))

#############################
# SEEDER
#############################
@app.route('/api/seeder/<input>', methods=['GET'])
def seeder(input):
	if input == 'ipr':
		kiss = IprCheck(
			kod_ipr = 'kiss', 
			nama_ipr = "Kasih Ibu Smart Selangor",
			max_umur_pemohon = '21',
			min_umur_pemohon = '18',
			jantina_pemohon = 'Perempuan',
			status_pemohon = 'namasini',
			negeri_kelahiran_pemohon = 'Selangor',
			mastautin_pemohon = '10',
			max_pendapatan_pemohon = '2000',
			min_pendapatan_pemohon = '0',
			jantina_pasangan = 'Lelaki',
			max_umur_pasangan = '21',
			min_umur_pasangan = '18',
			max_gaji_pasangan = '2000',
			min_gaji_pasangan = '0',
			# bilangan_anak = 'namasini',
			masih_belajar = 'Ya',
			ipr_status = 'active',
			)
		db.session.add(kiss)
		db.session.commit()
		return jsonify({'message' : 'Done seed IPR!'})
	return jsonify({'message' : 'Input is missing!'})


@app.route('/api/check', methods=['POST'])
def api_check():

	# dalam db akan ada max gaji & min gaji
	# status kahwin
	# max umur dan min umur
	# nama ipr

	 # nama
	# tarikh_lahir
	# jantina
	# mastautin
	# tempat_lahir
	# gaji
	# pendapatan_isi_rumah
	# status_kahwin

	# nama_pasangan
	# tarikh_lahir_pasangan
	# jantina_pasangan
	# gaji_pasangan

	# bilangan_anak

	nama = request.form['nama']
	tarikh_lahir = request.form['tarikh_lahir']
	jantina = request.form['jantina']
	mastautin = request.form['mastautin']
	tempat_lahir = request.form['tempat_lahir']
	gaji = request.form['gaji']
	pendapatan_isi_rumah = request.form['pendapatan_isi_rumah']
	status_kahwin = request.form['status_kahwin']
	nama_pasangan = request.form['nama_pasangan']
	tarikh_lahir_pasangan = request.form['tarikh_lahir_pasangan']
	jantina_pasangan = request.form['jantina_pasangan']
	gaji_pasangan = request.form['gaji_pasangan']
	bilangan_anak = request.form['bilangan_anak']
	
	# cek kelayakan


	return jsonify({'message' : 'api'})

@app.route('/')
def main_page():

	return render_template('home.html')

@app.route('/result')
def result_page():

	return render_template('result.html')

if __name__ == '__main__':
	app.run(port=8000, debug=True)