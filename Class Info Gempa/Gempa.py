class Gempa:
    #konstruktor Inisialisasi atribut lokasi dan skala
    def __init__(self, lokasi, skala):

        #atribut
        self.lokasi = lokasi
        self.skala = skala

    #method menentukan dampak skala gempa
    def dampak(self):

        # Statement / Logika
        if self.skala < 2:
            print("Dampak gempa tidak berasa")
        elif self.skala >=2 and self.skala <= 4:
            print("Dampak gempa bangunan retak-retak")
        elif self.skala > 4 and self.skala <= 6:
            print("Maka dampak gempa bangunan runtuh")
        elif self.skala > 6:
            print("Dampak gempa berpotensi tsunami")

    #Menampilkan Lokasi dan Skala
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')
