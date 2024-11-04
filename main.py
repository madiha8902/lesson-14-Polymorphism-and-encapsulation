class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print("my name is ",self.name , " and my age is ",self.age)

    def sounds(self):
        print("all cats meow",)

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print("my name is ",self.name , " and my age is ",self.age)

    def sounds(self):
        print("all dogs bark",)

cat1=Cat("dodo",4)
dog1=Dog("puppy",5)

for animal in (cat1,dog1):
    animal.info()
    animal.sounds()
