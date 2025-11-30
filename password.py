print("=== SISTEM PEBUATAN AKUN ===")

nama_lengkap = input("Masukkan nama lengkap anda: ")
tahun_lahir = input("Masukkan tanggal lahir anda:")

tiga_huruf = nama_lengkap[0:3]
dua_angka = tahun_lahir[-2]

password = tiga_huruf + dua_angka

print("Username:", nama_lengkap)
print("Password Sementara:", password)