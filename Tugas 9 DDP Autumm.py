print()
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    konversi=(celcius*9/5)+32
    return konversi

print(celcius_ke_fahrenheit(0)) #32
print(celcius_ke_fahrenheit(100))

print()
print('## Nomor 2 ##')
def ganjil_genap(bilangan):
    penentu=bilangan % 2 == 0
    return penentu

print(ganjil_genap(4)) #True
print(ganjil_genap(7))

print()
print('## Nomor 3 ##')
def nilai(keterangan):
    if keterangan >= 80:
        print("Lulus")
    elif keterangan <= 60:
        print("Gagal")
    else:
        print("Tidak Valid")
nilai(80)
nilai(60)

print()
print('## Nomor 4 ##')
def bilangan(n):
    return [i for i in range(1,n) if i % 2 != 0]
print(bilangan(20))