from Animal import Animal

class Bird(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama,makanan,hidup,berkembang_biak)
        self.warna = warna
        self.paruh = paruh
    
    def info_bird(self):
        super().info_animal()
        print('Warna\t\t:' ,self.warna,'\nJenis Paruh\t:', self.paruh)

print()
Bird = Bird('Elang','Dagimng','Ditebing','Menghasilkan Telur','Coklat','Bengkok dan Lancip')
print("## Info Bird")
Bird.info_bird()