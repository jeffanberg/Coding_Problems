''' Project Euler Problem 84.
Monopoly Problem.
Statistically it can be shown that the three most popular squares, in order,
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24,
and GO (3.09%) = Square 00. So these three most popular squares can be listed
with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used,
find the six-digit modal string.
'''
import random


class Dice:

    def __init__(self, num_of_dice, sides):
        self.num_of_dice = num_of_dice
        self.sides = sides

    def roll(self):
        total = 0
        previous = 0
        for each in range(self.num_of_dice):
            roll = random.randint(1, self.sides)
            if previous == roll:
                doubles = True
            else:
                doubles = False
            total += roll
            previous = roll
        return total, doubles


class Position:

    def __init__(self, square):
        self.square = square

    def __repr__(self) -> str:
        return f'Current square: {self.square}'

    def __eq__(self, other) -> bool:
        return self.square == other.square

    def __lt__(self, other):
        return 0

    def update(self, square):
        self.square = square

    def get_square(self):
        return self.square


class Monopoly:

    def __init__(self, board, dice):
        self.board = board
        self.dice = dice
        self.position = Position('GO')

    def get_square_number(self, square):
        try:
            return board.index(square)
        except ValueError:
            return Exception('No such square on board.')

    def shuffle(self):  # Shuffle the community cards before each game.
        community = ['GO', 'JAIL', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        chance = ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'nextR', 'nextR',
                  'nextU', 'back3', 0, 0, 0, 0, 0, 0]
        random.shuffle(community)
        random.shuffle(chance)
        return community, chance

    def run(self, turns):
        community_cards, chance_cards = self.shuffle()
        moves = dict()
        three_doubles = [False, False]
        for turn in range(turns):
            throw, doubles = self.dice.roll()
            if doubles is True:
                if three_doubles[0] is False:
                    three_doubles[0] = True
                elif three_doubles[1] is False:
                    three_doubles[1] = True
                else:
                    three_doubles = [False, False]
                    self.position.update('JAIL')
                    # print('Rolled three doubles and went to jail.')
                    if 'JAIL' not in moves.keys():
                        moves.update({'JAIL': 1})
                        continue
                    else:
                        count_moves = moves.pop('JAIL') + 1
                        moves.update({'JAIL': count_moves})
                        continue
            else:
                three_doubles = [False, False]

            current_move = self.get_square_number(self.position.get_square()) \
                + throw
            if current_move > len(board) - 1:
                current_move = current_move - len(board)
            self.position.update(board[current_move])
            current_position = self.position.get_square()
            ''' print(f'Rolled a {throw} and ' +
                  f'moved to square {current_position}')
            '''
            if current_position == 'G2J':
                self.position.update('JAIL')
                current_position = 'JAIL'
            if current_position in ['CC1', 'CC2', 'CC3']:
                card = community_cards.pop(0)
                community_cards.append(card)
                if card == 'GO' or card == 'JAIL':
                    self.position.update(card)
                    current_position = card
            if current_position in ['CH1', 'CH2', 'CH3']:
                card = chance_cards.pop(0)
                chance_cards.append(card)
                if card in ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1']:
                    self.position.update(card)
                    current_position = card
                if card == 'back3':
                    current_move -= 3
                    self.position.update(board[current_move])
                    current_position = self.position.get_square()
                if card == 'nextR':
                    if current_position == 'CH1':
                        self.position.update('R2')
                        current_position = 'R2'
                    elif current_position == 'CH2':
                        self.position.update('R3')
                        current_position = 'R3'
                    elif current_position == 'CH3':
                        self.position.update('R1')
                        current_position = 'R1'
                if card == 'nextU':
                    if current_position == 'CH1' or current_position == 'CH3':
                        self.position.update('U1')
                        current_position = 'U1'
                    else:
                        self.position.update('U2')
                        current_position = 'U2'

            if current_position not in moves.keys():
                moves.update({current_position: 1})
            else:
                count_moves = moves.pop(current_position) + 1
                moves.update({current_position: count_moves})
        return moves

    def find_top_three(self, turns):
        moves = self.run(turns)
        first_highest, second_highest, third_highest = 0, 0, 0
        top_three = ['', '', '']
        answer = ''
        for square, times in moves.items():
            if times > first_highest:
                top_three[2] = top_three[1]
                top_three[1] = top_three[0]
                top_three[0] = square
                first_highest = times
            elif times > second_highest:
                top_three[2] = top_three[1]
                top_three[1] = square
                second_highest = times
            elif times > third_highest:
                top_three[2] = square
                third_highest = times
            else:
                continue
        print(top_three)
        for each in top_three:
            temp = self.get_square_number(each)
            if temp < 10:
                temp = '0' + str(temp)
            answer += str(temp)
        return answer


board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL',
         'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1',
         'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2',
         'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']


six_sided_dice = Dice(2, 6)
four_sided_dice = Dice(2, 4)
MONOPOLY = Monopoly(board, four_sided_dice)
print(MONOPOLY.find_top_three(10 ** 6))
