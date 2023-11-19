import sqlite3
import json

class Database_bukuTamu():
    def __init__(self, database_name:str) -> None:
        self.connect = sqlite3.connect(f"{database_name}.db")
        self.connect.row_factory = sqlite3.Row
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute(f"CREATE TABLE buku(nama, alamat, noTelepon)")
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
    
    def update(self, table_name:str, *column_value, nama):
        self.cursor.execute(f"""
                                UPDATE {table_name}
                                SET alamat = ?, noTelepon = ?
                                WHERE nama = ?;
                            """, (column_value[0], column_value[1], nama))
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
        
        