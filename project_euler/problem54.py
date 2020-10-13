'''
https://projecteuler.net/problem=54


The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid
(no invalid characters or repeated cards),
each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
import os
import time
start = time.time()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p054_poker.txt')) as poker_file:
    poker_hands = [hand.replace('\n', '') for hand in poker_file.readlines()]


def evaluateHand(hand):
    player_one = hand[0:14]
    player_two = hand[15:]
    if handValue(player_one) > handValue(player_two):
        return True
    else:
        return False


def handValue(cards):
    value = 0
    hand = cards.split(' ')
    suits = set()
    facevalue = []
    for card in hand:
        suits.add(card[1])
        if card[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            facevalue.append(int(card[0]))
        elif card[0] == 'T':
            facevalue.append(10)
        elif card[0] == 'J':
            facevalue.append(11)
        elif card[0] == 'Q':
            facevalue.append(12)
        elif card[0] == 'K':
            facevalue.append(13)
        else:
            facevalue.append(14)
    value = sorted(facevalue)[4]
    if len(suits) == 1:
        value += 100000
    for c in facevalue:
        if facevalue.count(c) == 2:
            value += c * 100
        elif facevalue.count(c) == 3:
            value += c * 1000
        elif facevalue.count(c) == 4:
            value += c * 1000000
    low_card = sorted(facevalue)[0]
    if [low_card, low_card + 1, low_card + 2, low_card + 3, low_card + 4] == \
            sorted(facevalue):
        value += 10000
        if low_card == 10:
            value += 1000000000
    return value


count = 0
for hand in poker_hands:
    if evaluateHand(hand):
        count += 1
print(count)

end = time.time()
print("Time", end - start)
