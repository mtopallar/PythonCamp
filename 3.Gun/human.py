class Human:
    #name = "Halit"
    #built-in
    def __init__(self,name): #ctor - initialize
        self.name = name
        print("Bir human instance ı üretildi.")
    def __str__(self) -> str: #seri dönüş tipi
        return f"STR fonksiyonundan dönen değer: {self.name}" #class direk print edilirse bu çalışıyor.
    def talk(self,sentence):
        print(f"{self.name}, {sentence}")        
        #class içindeki name değişkenine direk ulaşamıyoruz. method gövdesi içinde bir name varsa direk erişebiliriz ancak class içindekine erişmek için self.name dememiz lazım.
        # self.walk() aynı şekilde metod içinden metod çağırırken de self.metod adı şeklinde çağırmamız lazım.    
    def walk(self):
        print("Human is walking...")