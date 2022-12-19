class Helicopter:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def presentation(self):
        print(f"Helicopter's model is {self.model}\nit's {self.color}, his speed is {self.speed} ")

    def change_color(self):
        print(f"Helicopter now is {self.color}")

def main():

    model = input('Enter the model of the helicopter: ')
    color = input('Enter the color of the helicopter: ')
    speed = int(input('Enter the speed: '))

    helicopter = Helicopter(model, color, speed)
    helicopter.presentation()
    ans = input("Do you want change the color? y/n ")
    if ans == "y":
        new_color = input("What color do you want? ")
        helicopter = Helicopter(model, new_color, speed)
        helicopter.change_color()
        helicopter.presentation()
    else:
        print("Ok, thank you")
main()

