class Cat:
    # class attribute
    scientific_name = "\x1B[3m" + "Felis Catus"+ "\x1B[0m"

    # constructor
    def __init__(self, name="unamed"):
        self.name = name # instance attribute
        print(name + " is " + self.scientific_name)
    
    # method 
    def speak(self):
        print("meaw meaw")

    def eat(self):
        print("I am eating")

if __name__ == "__main__":
    kucingkosan = Cat()
    kucingrumah = Cat("Erick")

    kucingkosan.speak()
    kucingrumah.speak()