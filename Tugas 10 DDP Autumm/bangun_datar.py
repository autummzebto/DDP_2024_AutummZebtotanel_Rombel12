import math

# Fungsi untuk menghitung luas lingkaran
# Rumus: π * jari_jari^2
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari**2

# Fungsi untuk menghitung luas persegi
# Rumus: sisi * sisi
def luas_persegi(sisi):
    return sisi * sisi

# Fungsi untuk menghitung luas segitiga
# Rumus: 0.5 * alas * tinggi
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Fungsi untuk menghitung luas persegi panjang
# Rumus: panjang * lebar
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Fungsi untuk menghitung luas jajar genjang
# Rumus: alas * tinggi
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi