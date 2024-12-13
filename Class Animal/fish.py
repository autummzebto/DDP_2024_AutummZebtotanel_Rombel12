from Animal import Animal

class fish(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.bernapas = bernapas
        self.habitat = habitat

    def info_fish(self):
        super().info_animal()
        print('Bernapas Menggunakan :', self.bernapas,'\nHabitat Di \t:', self.habitat)
        
        #objek
print()
fish =  fish("Hiu","Daging","Laut","Melahirkan","Insang","Air Asin")
fish.info_fish()