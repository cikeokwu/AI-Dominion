import random
import threading

from card import Estate, Copper, cTypes
from enum import Enumerate

class Player:
    """The player object.

    Defines a player and wraps lists for deck, discard, hand, and in-play.
    Also defines several interaction methods, all of which should be True
    to allow for chaining inside of lambda expressions.
    """
    def __init__(self, supply=None):
        self.deck = [Estate] * 3 + [Copper] * 7
        self.discard = []
        self.hand = []
        self.play = []
        self.shuffle()
        self.draw(5)
        self.supply = supply
        self.selected = None

    def shuffle(self):
        random.shuffle(self.deck)
        random.shuffle(self.deck)
    
    def setPlayers(self, players):
        """Sets the other players in the game from a given list.

        Takes the list and rotates members until this player has the
        zero position in the list and then removes self."""
        self.players = players[:]
        while self.players[0] is not self:
            self.players.append(self.players.pop(0))
        self.players.pop(0)

    def draw(self, num=1):
        """Move a card from deck to hand. If there are no cards in deck,
        shuffle the discard into the deck and try again. If there are
        still no cards in deck, silently ignore"""
        for i in range(num):
            if len(self.deck) == 0 and len(self.discard) > 0:
                self.deck = self.discard
                self.discard = []
                random.shuffle(self.deck)
            if len(self.deck) > 0:
                self.hand.append(self.deck.pop())
        return True

    def addAction(self, num=1):
        self.actions += num
        return True

    def addBuys(self, num=1):
        self.buys += num
        return True

    def addMoneys(self, num=1):
        self.moneys += num
        return True

    def gainCard(self, card_):
        if self.supply is None:
            self.discard.append(card_)
        elif card_ in self.supply and self.supply[card_] > 0:
            self.supply[card_] -= 1
            self.discard.append(card_)
        return True

    def doAction(self, card_):
        pass

    def doBuy(self, card_):
        pass

    def startTurn(self):
        self.actions = 1
        self.buys = 1
        self.moneys = 0

    def countTreasure(self):
        for i in self.hand:
            self.moneys += i.treasureValue(self)

    def endTurn(self):
        self.discard.extend(self.hand)
        self.discard.extend(self.play)
        self.hand = []
        self.play = []
        self.draw(5)

turnState = Enumerate('FromSupply FromHand Waiting Exit')

class PlayerThread(threading.Thread):
    def __init__(self, who):
        self.who = who
        self.isRunning = threading.Event()
        self.isRunning.clear()
        threading.Thread.__init__(self)

    def run(self):
        self.state = turnState.Waiting
        while self.state is not turnState.Exit:
            self.isRunning.wait()
            if self.state is turnState.FromHand:
                pass
            if self.state is turnState.FromSupply:
                pass
