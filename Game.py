import random

class Game:
    def retrieveComputerMove(self):
        a = random.randint(0,3)
        if a == 1:
            return "Rock"
        if a ==2:
            return "Paper"
        if a == 3:
            return "Scissors"