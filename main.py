# This is A DUMB DRINKING GAME
# @author: Y Zhang 10/07/2020

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from random import shuffle
CARDS = 14
SUIT_LIST = ["DIAMOND", "CLUB", "SPADES","HEART"]
class Deck:
    def __init__(self):
        self.card_list = []
        self.current_card = 0
        for i in range(4):
            for j in range(1,CARDS):
                suit = SUIT_LIST[i]
                card = [suit,j]
                self.card_list.append(card)

    def notEmpty(self):

        return self.current_card < 52
    def shuffleCard(self):
        self.current_card = 0
        shuffle(self.card_list)
    def getCard(self):
        if self.notEmpty():
            carrd = self.card_list[self.current_card]
            self.current_card += 1
            return carrd
    def getSuit(self,card):
        return(card[0])
    def getNum(self,card):
        return(card[1])
    def printDeck(self):
        for item in self.card_list:
            print(item)

def main():
    D = Deck()
    D.shuffleCard()
    #print(D.getCard())
    #D.printDeck()
    user = input("Press A Key To Start (you can always press X to exit the game)")
    PLAY = True
    while PLAY:
        if not D.notEmpty():
            print("yes")
            D.shuffleCard()
        color = input("Guess Color(Enter B for black and R for red):")
        card = D.getCard()
        print(card)
        if color == "R":
            print(D.getSuit((card)) == "DIAMOND" or D.getSuit((card)) == "HEART")
        elif color == "B":
            print(D.getSuit((card)) != "DIAMOND" and D.getSuit((card)) != "HEART")
        elif color == "X":
            break
        else:
            printWrong()

        eo = input("Guess Even or Odd(Enter E for even and O for odd):")
        card = D.getCard()
        print(card)
        if eo == "E":
            print(D.getNum((card)) % 2 == 0)
        elif eo == "O":
            print(D.getNum((card)) % 2 == 1)
        elif eo == "X":
            break
        else:
            #PLAY = False
            printWrong()

        bs = input("Guess Big or Small(Enter B for number no less than 8 and S for number less than 8):")
        card = D.getCard()
        print(card)
        if bs == "B":
            print(D.getNum(card) > 8 or D.getNum(card) == 8)
        elif bs == "S":
            print(D.getNum((card)) < 8)
        elif bs == "X":
            break
        else:
            #PLAY = False
            printWrong()

        s = input("Guess Suit(Enter D for Diamond; H for Heart; S for Spades; C for Club):")
        card = D.getCard()
        print(card)
        if s == "D":
            print(D.getSuit(card) == "DIAMOND")
        elif s == "H":
            print(D.getSuit(card) == "HEART")
        elif s == "S":
            print(D.getSuit(card) == "SPADES")
        elif s == "C":
            print(D.getSuit(card) == "CLUB")
        elif s == "X":
            break
        else:
            printWrong()

def printWrong():
    print("you press the wrong key")
    print("D R I N K")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
