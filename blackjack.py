import random

cardByName = {
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A'
}     

hand = [random.randint(1,14), random.randint(1, 14)]

print("Rules: You start out with two cards in your hands. It is Random if you go first or second. When it is your turn you can either draw(d) or sit(s). The game ends when both players sit. Whoever is closest to 21 when the game ends is the winner. If you go over 21 you lose.")

print ("Your hand: " + cardByName.get(hand[0], str(hand[0])) + " and " + cardByName.get(hand[1], str(hand[1])))

your_move = input("What is your move? ")

if your_move == "draw" or your_move == "d":
    print ("Your hand is now ")
 
#  TODO: Drawing mechanism, Sitting Mechanism, Talk Logistics(rules/how to play)