import random
from collections import namedtuple


class Card:
    def __init__(self, color=None) -> None:
        self.color = color
        if self.color is None:
            self.color = random.choices(['red', 'black'], [1/3, 2/3])[0]
        self.number = random.randint(1, 10)
        if self.color == 'red':
            self.score = -self.number
        else:
            self.score = self.number


class State:
    def __init__(self, dealer_first_card, player_sum):
        self.dealer_first_card = dealer_first_card
        self.player_sum = player_sum


class Env:

    action_space = {0, 1} # {0: hit, 1: stick}

    def __init__(self):
        self.dealer_first_card = None
        self.player_card_list = None
        self.state = None
        self.is_terminate = None    

    def reset(self):
        self.dealer_first_card = Card('black')
        self.player_card_list = [Card('black')]
        self.state = State(self.dealer_first_card.number, self.player_card_list[0].number)
        print(f'dealer first card: black {self.state.dealer_first_card}')
        print(f'player first card: black {self.state.player_sum}')
        self.is_terminate = False

    def step(self, action):
        if action == 0: # hit
            new_card = Card()
            self.player_card_list.append(new_card)
            self.state.player_sum += new_card.score
            if self.state.player_sum > 21 or self.state.player_sum < 1:
                self.is_terminate = True
                reward = -1
            else:
                reward = 0
            print(f'player new card: {new_card.color} {new_card.number}, player sum: {self.state.player_sum}')
            return self.state, reward, self.is_terminate
        elif action == 1: # stick
            dealer_sum = self.state.dealer_first_card
            while True:
                new_card = Card()
                dealer_sum += new_card.score
                print(f'dealer new card: {new_card.color} {new_card.number}, dealer sum: {dealer_sum}')
                if dealer_sum > 21 or dealer_sum < 1:
                    reward = 1
                    break
                elif dealer_sum >= 17:
                    if self.state.player_sum > dealer_sum:
                        reward = 1
                    elif self.state.player_sum == dealer_sum:
                        reward = 0
                    else:
                        reward = -1
                    break
            self.is_terminate = True
            return self.state, reward, self.is_terminate

