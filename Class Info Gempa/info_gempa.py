# Memanggil File Gempa dan Import Semua Method/fungsi
from Gempa import *

# Membuat Objek Gempa dengan Argumen
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Cianjur', 5.6)
gempa4 = Gempa('Jayapura', 3.3)
gempa5 = Gempa('Garut', 4.0)

# Informasi gempa
print('## Info Gempa ##')
print()
gempa1.dampak()

print()
print('## Info Gempa ##')
print()
gempa2.dampak()

print()
print('## Info Gempa ##')
print()
gempa3.dampak()

print()
print('## Info Gempa ##')
print()
gempa4.dampak()

print()
print('## Info Gempa ##')
print()
gempa5.dampak()