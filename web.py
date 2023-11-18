from flask import Flask
from flask import request, render_template, url_for, request, jsonify, redirect
import json
from database import Database

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./form.html')

@app.route('/input', methods=['GET', 'POST'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        db = Database("buku_tamu")
        db.insert("buku", data["nama"], data["alamat"], data["noTelepon"])
        return redirect("/lihat_data")
    else:
        return 'Something went wrong. Try again!'
    
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
    return data_db

    

