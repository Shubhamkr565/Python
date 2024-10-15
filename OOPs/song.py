class song:
    """This is song class required data and behaviour"""

    def __init__(self,artist, title):
        print("Inside the constructor")
        self.artist = artist
        self.title = title

    def paly(self):
        print("{0} is singing {1} ".format(self.artist, self.title))

s1 = song("Lata", "Wanda Matram")
s1.paly()

s2 = song("Shukwindar", "Jai Ho")
s2.paly()