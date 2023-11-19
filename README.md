# buku_tamu
Implementasi restful untuk buku tamu.

## deskripsi
Buku tamu ini merupakan aplikasi sederhana yang menerapkan restful. database yang digunakan **SQLite** yang mana menggunakan 1 tabel berisi kolom nama, alamat dan no telepon.

## penggunaan
* Install library yang diperlukan
* Jalankan file main.py dengan perintah ```python main.py```

## dokumentasi
1. Halaman home akan menampilkan form untuk input data ('/')

![index](https://raw.githubusercontent.com/kazuma313/buku_tamu/main/gambar/index.png)

2. jika ingin melihat semua data terdapat pada endpoint ('/lihat_data')

![lihat data](https://raw.githubusercontent.com/kazuma313/buku_tamu/main/gambar/lihat_data.png)

4. Jika ingin mencari nama atau alamat, dapat menggunakan endpoint ('/search_data/<arg>')

![search data](https://raw.githubusercontent.com/kazuma313/buku_tamu/main/gambar/search_data.png)

6. Jika ingin melihat detail suatu nama, dapat menggunakan endpoint ('/detail_data/<nama>')

![detail data](https://raw.githubusercontent.com/kazuma313/buku_tamu/main/gambar/detail_data.png)

8. Jika ingin menghapus data, dapat menggunakan endpoint ('/hapus_data/<nama>')

![hapus data](https://raw.githubusercontent.com/kazuma313/buku_tamu/main/gambar/hapus_data.png)

9. Jika ingin update data, dapat menggunakan endpoint ('/update/<nama>')

![update data](https://raw.githubusercontent.com/kazuma313/buku_tamu/main/gambar/update_data.png)

