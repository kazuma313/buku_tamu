input_nama = input("Masukan nama : ")

while True:
    # tambahkan regex untuk cek bentuk nomor telepon
    input_no_telepon = input("Masukan no telepon : ")
    if len(input_no_telepon) == 12: # ini masih bisa di clean menjadi satu baris
        break
    print("coba cek lagi no telepon anda")
    
input_alamat = input("Masukan alamat : ")

json = dict(nama = input_nama, 
            no_telepon = input_no_telepon, 
            alamat = input_alamat)

print(json)
