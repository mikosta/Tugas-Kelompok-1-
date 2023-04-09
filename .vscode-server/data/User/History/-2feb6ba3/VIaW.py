# Program Pembayaran Sederhanagit

# Input Nama Pembeli
nama_pembeli = input("Masukkan Nama Pembeli: ")

# Input Nama Pembeli
nama_barang = input("Masukkan Nama barang: ")

# Input Jumlah Barang dan Harga Satuan
jumlah_barang = int(input("Masukkan Jumlah Barang: "))
harga_satuan = float(input("Masukkan Harga Satuan: "))

# Hitung Total Harga
total_harga = jumlah_barang * harga_satuan

# Tampilkan Total Harga
print("Total Harga:", total_harga)

# Input Pembayaran
bayar = float(input("Masukkan Jumlah Pembayaran: "))

# Hitung Kembalian
kembalian = bayar - total_harga

# Tampilkan Kembalian
print("Kembalian:", kembalian)

# Tampilkan Struk Pembayaran
print("===========================")
print("       Struk Pembayaran     ")
print("===========================")
print("Nama Pembeli:", nama_pembeli)
print("Jumlah Barang:", jumlah_barang)
print("Harga Satuan:", harga_satuan)
print("Total Harga:", total_harga)
print("Bayar:", bayar)
print("Kembalian:", kembalian)
print("===========================")