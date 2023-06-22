class Cat:
    # class attribute
    scientific_name = "\x1B[3m" + "Felis Catus"+ "\x1B[0m"
    __age = 0

    # constructor
    def __init__(self, name="unamed"):
        self.name = name # instance attribute
        print(name + " is " + self.scientific_name)
    
    # method 
    def speak(self):
        print("meaw meaw")

    def eat(self):
        print("I am eating")

class Persian(Cat):
    breed = "Persian"
    diet = ["Rc Adult Persian", "Equilibrio"]

    def __init__(self, name="unamed"):
        super().__init__(name)
        print(name + " is " + self.breed + " cat")

    def eat(self, food):
        if food in self.diet:
            print("meaw meaw, I love this")
        else:
            print("grrr, I don't eat this")

class Sphynx(Cat):
    breed = "Sphynx"
    diet = ["soul", "donut"]
    def __init__(self, name="unamed"):
        super().__init__(name)
        print(f"{name} is {self.breed} cat")
    
    def eat(self, food):
        if food in self.diet:
            print("meaw meaw, I am a cow")
        else:
            print("hmmm, I don't eat this")

if __name__ == "__main__":
    kucing_kosan = Cat("bonbon")
    kucingsofirul = Persian("Erick")
    kucingradit = Sphynx("Kuki")
    print("="*10)
    kucing_kosan.eat()
    print()
    kucingsofirul.eat("Rc Adult Persian")
    kucingsofirul.speak()
    print()
    kucingradit.eat("Equilibrio")
    print()
    kucingradit.eat("soul")