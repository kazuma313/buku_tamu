from flask import Flask, request, render_template, url_for, request, jsonify, redirect
from modules.database import Database_bukuTamu as Database, json
from modules.data_validation import input_noTelepon, input_nama

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./form.html')

@app.route('/input', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        db = Database("buku_tamu")
        nomor_telepon = input_noTelepon(data["noTelepon"])
        nama = input_nama(data["nama"])
        alamat = input_nama(data["alamat"])
        try:
            db.insert("buku", nama, alamat, nomor_telepon)
            return redirect("/lihat_data")
        except:
            return render_template('./form.html', alert="perhatikan input anda")
    else:
        return render_template('./form.html', alert="perhatikan input anda")
    
@app.route("/update/<nama>")
def update(nama):
    db = Database("buku_tamu")
    data_db = db.detail("buku", cari=nama)
    data_db = json.loads(data_db)
    alamat = data_db[0]["alamat"]
    noTelepon = data_db[0]["noTelepon"]
    return render_template('./form_update.html', nama=nama, alamat=alamat, noTelepon=noTelepon)

@app.route("/update_data", methods=["POST"])
def update_data():
    if request.method == "POST":
        data = request.form.to_dict()
        db = Database("buku_tamu")
        nomor_telepon = input_noTelepon(data["noTelepon"])
        alamat = input_nama(data["alamat"])
        nama = data["nama"]
        try:
            db.update("buku", alamat,  nomor_telepon, nama=nama)
            return redirect("/lihat_data")
        except:
            return render_template('./form.html', alert="perhatikan input anda")
    else:
        return render_template('./form.html', alert="perhatikan input anda")

@app.route("/lihat_data")
def lihat_data():
    db = Database("buku_tamu")
    data_db = db.select(table_name="buku")
    return data_db

@app.route("/hapus_data/<nama>")
def hapus_data(nama):
    db = Database("buku_tamu")
    db.delete("buku", nama=nama)
    return redirect("/lihat_data")

@app.route("/search_data/<arg>")
def search_data(arg):
    db = Database("buku_tamu")
    data_db = db.search("buku", cari=arg)
    return data_db

@app.route("/detail_data/<nama>")
def detail_data(nama):
    db = Database("buku_tamu")
    data_db = db.detail("buku", cari=nama)
    print(data_db)
    return data_db


if __name__ == '__main__':
    app.secret_key='ItIsSecret'
    app.debug = True
    app.env="development"
    app.run()
