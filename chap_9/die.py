
from random import randint

class Die():
    """Generate a random number for the dice gaame"""
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides"""
        number = randint(1, self.sides)
        print(f"The number is: {number}")


dice = Die(6)
for i in range(1, 11):
    dice.roll_die()
print("\n")


dice = Die(10)
for i in range(1, 21):
    print("The roll " + str(i))
    dice.roll_die()
   