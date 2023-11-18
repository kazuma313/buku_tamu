import sqlite3
import json
# con = sqlite3.connect("buku_tamu.db")
# cur = con.cursor()
# # cur.execute("CREATE TABLE buku(nama, alamat, no_telepon)")
# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

# cur.execute("""
#     INSERT INTO buku VALUES
#         ('Kurnia Zulda Matondang', 'Jambi', 0822),
#         ('Seta Murdha Pamungkas', 'Probolinggo', 9821)
# """)
# con.commit()


# # membuat json dari DML
# con.row_factory = sqlite3.Row
# db = con.cursor()
# db.execute("""
#     INSERT INTO buku VALUES
#         ('Fany', 'Jambi', 0822),
#         ('Mauren', 'Probolinggo', 9821)
# """)
# con.commit()
# res = db.execute('''
#     SELECT * from buku
#     ''').fetchall()
# print(res)

# import json
# print(json.dumps([dict(ix) for ix in res]))




# data = [
#     ("Monty Python Live at the Hollywood Bowl", "1982", 7.9),
#     ("Monty Python's The Meaning of Life", "1983", 7.5),
#     ("Monty Python's Life of Brian", "1979", 8.0),
# ] # Terdapat cara untuk input menggunakan dictionary
# cur.executemany("INSERT INTO buku VALUES(?, ?, ?)", data) # Gunakan place holder '?' untuk menghidari sql injection attack menggunakan string
# con.commit()  # Remember to commit the transaction after executing INSERT.

# con.close() # verifikasi database untuk disimpan ke disk






class Database():
    columns = ("nama", "alamat", "noTelepon")
    
    def __init__(self, database_name:str) -> None:
        self.connect = sqlite3.connect(f"{database_name}.db")
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()
        
        # buat nama column lebih responsive
        try:
            self.cursor.execute("CREATE TABLE buku(nama, alamat, noTelepon)")  # try untuk handle jika table sudah ada
        except:
            print("table buku sudah dibuat")
        
    def create_table(self, table_name:str, *columns:str):
        
        columns = ", ".join(columns[:])
        self.cursor.execute(f"CREATE TABLE {table_name} ({columns})")

    def see_table(self):
        res = self.cursor.execute("SELECT name FROM sqlite_master")
        print(res.fetchone()) 
        
    def insert(self, table_name, *data):
        self.cursor.execute(f"""
                            INSERT INTO {table_name} 
                            VALUES {data}
                            """)
        self.connect.commit()
        self.save_data()
    
    def update(self, table_name:str, column_name:str, column_value:str):
        # update ini belum dinamis
        self.cursor.execute(f"""
                                UPDATE {table_name}
                                SET {column_name} = ?
                                WHERE nama = 'kurnia zulda';
                            """, (column_value,))
        self.connect.commit()
        self.save_data()
        
    def delete(self, table_name:str, nama:str):
        self.cursor.execute(f"""
                            DELETE FROM {table_name} 
                            WHERE nama= (?);
                            """, (nama,))
        self.connect.commit()
        self.save_data()
    
    def select(self, table_name, column_name:str = "nama, alamat, noTelepon"):
        res = self.cursor.execute(f"""
                                  SELECT {column_name} 
                                  FROM {table_name}
                                  """)
        json_data = json.dumps([dict(ix) for ix in res.fetchall()])
        return json_data
    
    def search(self, table_name, cari):
        res = self.cursor.execute(f"""
                                  SELECT *
                                  FROM {table_name}
                                  WHERE {table_name}.nama LIKE '%{cari}%'
                                        OR {table_name}.alamat LIKE '%{cari}%'
                                  """)
        json_data = json.dumps([dict(ix) for ix in res.fetchall()])
        return json_data
    
    def detail(self, table_name, cari):
        res = self.cursor.execute(f"""
                                    SELECT *
                                    FROM {table_name}
                                    WHERE {table_name}.nama LIKE '{cari}'
                                    """)
        json_data = json.dumps([dict(ix) for ix in res.fetchall()])
        return json_data
    
    def save_data(self):
        self.connect.close()
        
        
# database = Database("buku_tamu")
# print(database)
# database.create_table("buku", "nama", "alamat", "noTelepon") # berikan kondisi supaya bisa dirun walau sudah ada tuble
# database.see_table()

# database.insert("buku", "kurnia zulda", "jambi", "082")
# isi_table = database.select(table_name="buku")

# import json
# somedict = { "item" : [ x for x in isi_table ]}
# json_form = json.dumps(somedict)

# print(somedict['item'])
# print(json_form)

# print(database.select(table_name="buku"))

# database.update("buku", "alamat", "Malang")
# print(database.select(table_name="buku"))

# database.delete("buku", "kurnia zulda")
# print(database.select(table_name="buku"))

# print("----",database.search(table_name="buku", cari="ZUL"))
# print("----",database.detail(table_name="buku", cari="kurnia zulda matondang"))