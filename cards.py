import random
import time

deck = [] 
hand = []
end_condition = []

def shuffle (source, times):
    for x in range(0, times):
        random.shuffle(source)

def generate_new_deck():
    clear_deck()
    for x in range (0, 4):
        for y in range (1, 14):
            tup = (y, x)
            deck.append(tup)
    shuffle(deck, 7)

def clear_deck():
    while len(deck) != 0:
        del deck[0]
    
def clear_hand():
    while len(hand) != 0:
        del hand[0]
    
def add_card_to_hand():
    if len(deck) > 0:
        hand.insert(0, deck[0])
        del deck[0]

def fill_hand():
    while len(hand) < 4 and len(deck) > 0:
        add_card_to_hand()

def value_test(): # test if the first and last card in the 4 visible cards have the same rank.  Remove all 4 cards if true and return boolean indicating pass/fail
    test = False
    if len(hand) < 4:
        return test
    elif hand[0][0] == hand[3][0]:
        del hand[0]
        del hand[0]
        del hand[0]
        del hand[0]
        test = True
    return test
    
def suit_test(): # test if the first and last card in the 4 visible cards have the same suit.  Remove card 2 and 3 if true and return boolean indicating pass/fail
    test = False
    if len(hand) < 4:
        return test
    elif hand[0][1] == hand[3][1]:
        del hand[1]
        del hand[1]
        test = True
    return test

def fill_end_condition(): #initialize a list with 0 for each number of cards left.  Since the number of cards left is always even there are 52/2 + 1 end scenarios
    for x in range(0, 27):
        end_condition.append(0)

def main():
    start = time.time()
    fill_end_condition()
    for y in range (0, 10000): #this is two nested loops for debug purposes.  I shows intermediate results every x loops.  total iteerations = y range * x range = 100,000,000 as coded
        for x in range(0, 10000):
            clear_hand()
            generate_new_deck()
            while len(deck) > 0:
                fill_hand()
                if not value_test() and not suit_test(): # test value first since it will remove all four cards
                    add_card_to_hand()
            end_condition[int(len(hand)/2)] += 1 # add to the end_condition list based on the number of cards left when the deck is cleared
        print(y)
        print(end_condition)
    print (time.time()-start)
    print(end_condition)
           
main()   