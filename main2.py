# This is A DUMB DRINKING GAME
# @author: Y Zhang 10/07/2020

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

class Dui:
    def __init__(self):
        self.cards = 0
        self.surface = 0 # this just a meaningless default number
        self.have = True

    def changeSurface(self,num):
        self.cards += 1
        self.surface = num

    #input is a string whether B or S; number is the compared new card
    # return true false or 0 otherwise
    def compareCards(self,input,num):
        if input == "B":
            return num > self.surface
        elif input == "S":
            return num < self.surface
        else:
            return 0

    def getSurface(self):
        return self.surface

    def cardsleft(self):
        return self.cards

    def haveOrNot(self):
        return self.have

    def emptyOne(self):
        self.cards +=1
        self.surface = 0  # this just a meaningless default number
        self.have = False

class YiDaDui:

    def __init__(self,D):
        self.D = Deck()
        self.D.shuffleCard()
        self.yidadui = []
        self.dui1 = Dui()
        card = D.getCard()
        self.dui1.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui1)
        #print(card)
        self.dui2 = Dui()
        card = D.getCard()
        self.dui2.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui2)
        #print(card)
        self.dui3 = Dui()
        card = D.getCard()
        self.dui3.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui3)
        #print(card)
        self.dui4 = Dui()
        card = D.getCard()
        self.dui4.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui4)
        # print(card)
        self.dui5 = Dui()
        card = D.getCard()
        self.dui5.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui5)
        # print(card)
        self.dui6 = Dui()
        card = D.getCard()
        self.dui6.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui6)
        # print(card)
        self.dui7 = Dui()
        card = D.getCard()
        self.dui7.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui7)
        # print(card)
        self.dui8 = Dui()
        card = D.getCard()
        self.dui8.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui8)
        # print(card)
        self.dui9 = Dui()
        card = D.getCard()
        self.dui9.changeSurface(D.getNum(card))
        self.yidadui.append(self.dui9)
        # print(card)

    def getSurface(self,num):
        if num> 1 and num <10:
            return self.yidadui[num].getSurface()
        else:
            return 0

    def emptyOne(self,num):
        self.yidadui[num].emptyOne()
        return self.yidadui[num].cardsleft()

    def addCard(self,num,num1): #num is which dui to access num1 is the new surface
        return self.yidadui[num].changeSurface(num1)

    def printydd(self):
        print( "|" + self.helper(self.yidadui[0].getSurface())*" " + str(self.yidadui[0].getSurface()) + " |"+
                          self.helper(self.yidadui[1].getSurface())*" " + str(self.yidadui[1].getSurface()) + " |" +
                            self.helper(self.yidadui[2].getSurface())*" " + str(self.yidadui[2].getSurface()) + " |")
        print("|" + self.helper(self.yidadui[3].getSurface())*" "+ str(self.yidadui[3].getSurface()) + " |" +
              self.helper(self.yidadui[4].getSurface())*" "+ str(self.yidadui[4].getSurface()) + " |" +
              self.helper(self.yidadui[5].getSurface())*" "+ str(self.yidadui[5].getSurface()) + " |")
        print("|" + self.helper(self.yidadui[6].getSurface())*" "+ str(self.yidadui[6].getSurface()) + " |" +
              self.helper(self.yidadui[7].getSurface())*" "+ str(self.yidadui[7].getSurface()) + " |" +
              self.helper(self.yidadui[8].getSurface())*" "+ str(self.yidadui[8].getSurface()) + " |")
        # for item in self.yidadui:
        #     print(item.getSurface())

    def helper(self,num):
        if num > 9:
            return 1
        else:
            return 2

    def getDui(self,num):
        return self.yidadui[num]

def main():
    #print(D.getCard())
    #D.printDeck()
    # dui = Dui()
    # card = D.getCard()
    # dui.changeSurface(D.getNum(card))
    # print(card)
    # card2 = D.getCard()
    # print(card2)
    # print(dui.compareCards("B",D.getNum(card2)))
    D = Deck()
    D.shuffleCard()
    user = input("Press A Key To Start (you can always press X to exit the game)")
    ydd= YiDaDui(D)
    ydd.printydd()
    while D.notEmpty():
        user = input("put into which dui (please enter number)")
        if user == "X":
            break
        user =int(user)-1
        if user >0 and user<10:
            dui = ydd.getDui(user)
            usera = input("Guess: next dealt card would be bigger or smaller(enter B or S)")
            card = D.getCard()
            num = D.getNum(card)
            result = dui.compareCards(usera,num)
            if result:
                dui.changeSurface(num)
            elif not result:
                print("you have "+ str(ydd.emptyOne(user)) +" to go")
                #print(num)
            else:
                print("Enter a wrong key! Drink!")
            ydd.printydd()
        else:
            print("Wrong Input, get a shot")

if __name__ == '__main__':
    main()