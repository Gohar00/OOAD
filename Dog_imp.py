class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " is now sitting.")

    def stand(self):
        print(self.name + " is now standing.")

    def bark(self):
        print("Woof!")

    def birthday(self):
        print("Happy birthday " + self.name + "!")
        print(f'{self.name} is now {self.age} years old')
        self.age += 1

def main():

    name = input('Enter the name for dog: ')
    age = int(input('How old is dog: '))

    dog = Dog(name, age)
    dog.sit()
    dog.stand()
    dog.bark()
    dog.birthday()
    dog.birthday()

main()


