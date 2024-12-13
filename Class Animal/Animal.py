class Animal:
    # konstruktor properti
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

        # METHOD
    def info_animal(self):
        print(f"Nama hewan\t:", self.nama,
            "\nMakanan\t\t:", self.makanan,
            "\nHidup\t\t:", self.hidup,
            "\nBerkembang Biak\t:",self.berkembang_biak)
        
#Objek
kucing = Animal("Kucing","Daging","Didarat","Melahirkan")

kucing.info_animal()