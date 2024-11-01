#Tugas No 1
kendaraan = ['mio karbu', 'motor', 200, 'pink', 2]
print(kendaraan)

kendaraan.append('10jt')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)

#Tugas No 2

hitung_luas = int(input("""Pilih salah satu:
1. Hitung luas persegi
2. Hitung luas lingkaran 
3. Hitung luas segitiga 
"""))

match hitung_luas:
    case 1:
        print('Menghitung Luas Persegi')
        sisi = int(input('Masukan nilai sisi: '))
        hitung_luas_persegi = sisi **2
        print(f'Luas persegi dengan sisi {sisi} cm, adalah {hitung_luas_persegi} cm^2')
    case 2:
        print('Menghitung Luas Lingkaran')
        jari_jari = int(input('Masukan nilai jari jari: '))
        phi = (22/7)
        hitung_luas_lingkaran = luas = phi * (jari_jari ** 2)
        print(f'Luas lingkaran dengan jari jari {jari_jari} cm, adalah {hitung_luas_lingkaran} cm^2')
    case 3:
        print('Menghitung Luas Segitiga')
        alas = int(input('Masukan nilai alas: '))
        tinggi = int(input('Masukan nilai tinggi: '))
        hitung_luas_segitiga = luas = 1/2 * alas * tinggi
        print(f'Luas lingkaran, adalah {hitung_luas_segitiga} cm^2')
        
    case _:
        print('Pilihan tidak valid')