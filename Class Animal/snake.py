from Animal import Animal

class snake(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, panjang_tubuh, jenis_gigi):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.panjang_tubuh = panjang_tubuh
        self.jenis_gigi = jenis_gigi

    def info_snake(self):
        super().info_animal()
        print('Sedang melata dengan panjang tubuh :', self.panjang_tubuh,'\nJenis gigi \t:', self.jenis_gigi)
        
        #objek
print()
snake =  snake("Ular Piton","Daging","Daratan","Bertelur","6m","Tidak Tajam")
snake.info_snake()