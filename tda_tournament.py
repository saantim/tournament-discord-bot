from copy import copy
import random

from urllib3 import Retry

class Tournament_t():

    def __init__(self, players = []):
        self.players = players
        self.brackets = []
        self.bracket_winners = set()
        self.status = False

    def register(self, jugador):
        if self.status: raise Exception
        self.players.append(jugador)

    def valid_tournament(self):
        return len(self.players) > 1 and len(self.players) % 2 == 0 

    def get_players(self):
        return self.players

    def get_currently_bracket(self):
        if not self.status: return []
        return self.brackets[-1]

    def get_winner(self):
        if len(self.brackets[-1]) == 1:
            return self.brackets[0]

    def start(self):
        if self.status: raise Exception
        if not self.valid_tournament(): raise Exception
        bracket = self.players.copy()
        self.brackets.append(bracket)
        random.shuffle(self.brackets[0])
        self.status = True
    
    def reset(self, keep_players = True):
        if not keep_players:
            self.players = []
        self.brackets = []
        self.status = False

    def _is_even(self, n):
        return n % 2 == 0

    def _validate_bracket_winner(self, player):
        p_index = self.brackets[-1].index(player)
        if self._is_even(p_index) and (p_index + 1) in self.bracket_winners:
            return False
        if not self._is_even(p_index) and (p_index - 1) in self.bracket_winners:
            return False
        return True

    def _next_brackets(self):
        new_bracket = []
        for i in self.bracket_winners:
            new_bracket.append(self.brackets[-1][i])
        self.bracket_winners = set()
        self.brackets.append(new_bracket)

    def set_winner(self, player):
        if not self.status: raise Exception("Tournement is not started yet")
        if player in self.bracket_winners: raise Exception("Player is not in currently bracket")
        if not self._validate_bracket_winner(player): raise Exception("Both players can't be winners")
        winner_index = self.brackets[-1].index(player)
        self.bracket_winners.add(winner_index)
        
        if len(self.bracket_winners) * 2 == len(self.brackets[-1]):
            self._next_brackets()

    def next_bracket(self):
        brackets = self.brackets[-1]
        for i in range(0, len(brackets), 2):
            if not i in self.bracket_winners and not i + 1 in self.bracket_winners:
                return (brackets[i], brackets[i+1])
        return (None, None)

    def __repr__(self):
        txt = f'Players: {self.players}\nbrackets: {self.brackets}\nbracket Winners: {self.bracket_winners}\nStarted: {self.status}'
        return txt
