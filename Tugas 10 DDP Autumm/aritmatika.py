import math

# Fungsi untuk menambahkan dua angka
def tambah(a, b):
    return a + b

# Fungsi untuk mengurangi angka pertama dengan angka kedua
def kurang(a, b):
    return a - b

# Fungsi untuk mengalikan dua angka
def kali(a, b):
    return a * b

# Fungsi untuk membagi angka pertama dengan angka kedua
# Mengembalikan pesan error jika pembagian oleh nol
def bagi(a, b):
    if b == 0:
        return "Error: Pembagian oleh nol tidak diperbolehkan."
    else:
        return a / b

# Fungsi untuk menghitung pangkat dari angka pertama terhadap angka kedua
def pangkat(a, b):
    return math.pow(a, b)
