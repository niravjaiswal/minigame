import random
import sys

# This is gives the random numbers a card value
cardByName = {
    1: 'A',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
}     

cardActualValue = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 10,
    12: 10,
    13: 10
}     

# This is your hand.
your_hand = [random.randint(1,13), random.randint(1, 13), random.randint(1, 13), random.randint(1, 13), random.randint(1, 13)]

# This is the dealer's hand
dealer_hand = [random.randint(1,13), random.randint(1, 13)]

# This is the play boolean. This becomes flase when you decide to sit.
play = True

# These are the rules.
print("Rules: You start out with two cards in your your_hands, if you start out with two cards that equal 21 you automatically win. You always go first. When it is your turn you can either draw(d) or sit(s). The game ends when both players sit. Whoever is closest to 21 when the game ends is the winner. If you go over 21 you lose.")

# This variable states the amount of cards in your hand.
handIndex = -1

def IncrementHandIndex():
    global handIndex 
    handIndex += 1
    return handIndex

def CardTotal():
    cardTotal = 0
    hasAce = False
    for c in range(handIndex + 1):
        cardValue = cardActualValue.get(your_hand[c])
        if cardValue == 1:
            hasAce = True
        cardTotal += cardValue
    if hasAce and cardTotal + 10 <= 21:
        cardTotal += 10
    return cardTotal

# This print statment prints your your_hand at the beggining of the game.
hand_output = "Your hand: " + cardByName.get(your_hand[IncrementHandIndex()]) + " and " + cardByName.get(your_hand[IncrementHandIndex()])
print(hand_output)



# This while statment will only let you have a turn when the play boolean is true. It becomes false once you decide to sit. It remains true if you draw.
while play == True:

    if CardTotal() > 21:
        sys.exit("You busted! You lose!")

    if CardTotal() == 21:
        sys.exit("You got a blackjack! You win!")

    if handIndex == 4:
        sys.exit("You got a Charlie 5! You win!")

# This is the imput for your move, either draw(d) or sit(s)
    your_move = input("What is your move? ")

# This if statment will run the draw function if you draw or it will change the play boolean to false if you sit.
    if your_move == "draw" or your_move == "d":
        drawCard = cardByName.get(your_hand[IncrementHandIndex()])
        print("Your card is " + drawCard)
        hand_output += " and " + drawCard
        print(hand_output)

    elif your_move == "sit" or your_move == "s":
        play = False

#  TODO: Make the dealer, Talk Logistics(rules/how to play)