import pyCardDeck
import sys
from typing import List
from pyCardDeck.cards import PokerCard

class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

class BlackJackGame:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck()
        self.players = players
        self.scores = {}
        print(f"Created a game with {self.players} players.")

    def blackjack(self)