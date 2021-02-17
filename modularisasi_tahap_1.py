'''
Program menghitung luas segitiga = alas * tinggi / 2
'''
print('Menghitung luas segitiga 1 dengan copas')
alas = 6
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} luasnya adalah = {luas_segitiga}')
print('Menghitung luas segitiga 2 dengan copas')
alas = 12
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} luasnya adalah = {luas_segitiga}')
print('\nMenghitung luas segitiga dengan Fungsi')


def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Luas segitiga 1 dengan fungsi, hasilnya = {hitung_luas_segitiga(6, 2)}')
print(f'Luas segitigas 2 dengan fungsi, hasilnya = {hitung_luas_segitiga(12, 6)}')
print('\nMenghitung luas segitiga dengan fungsi jika alas dan tinggi sudah ditentukan')
alas = 100
tinggi = 20
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} luasnya adalah = {hitung_luas_segitiga(alas, tinggi)}')
# Memanggil fungsi cara kedua
print('\nMemanggil fungsi cara kedua')
def hitung_luas_segitiga2(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi}, Luas segitiga adalah : {luas_segitiga}')
hitung_luas_segitiga2(4, 2)
hitung_luas_segitiga2(8, 2)
print('\nMembuat Output Halo nama, selamat datang! menggunakan fungsi')
# Membuat fungsi dengan output :
# Halo Nurul, selamat datang!
# Halo Lendis, selamat datang!
# Halo Fabri, selamat datang!
# Halo Isa, selamat datang!
def sapa (nama):
    print(f'Halo {nama}, selamat datang!')
sapa('Nurul')
sapa('Lendis')
sapa('Fabri')
sapa('Isa')

