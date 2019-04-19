from enum import Enumerate

cTypes = Enumerate('Treasure Victory Action Attack Reaction')

class Card:
    """The top-level class representing game cards.

    Has values for card name, purchase cost, text description, card
    type and what expansion it is from. The card type is a dict that
    keys on values from cTypes and has values that are functions
    with a single argument of the relevant player. For actions this
    means the player playing the card, for attacks, the player being
    attacked.
    """
    def __init__(self, name, cost, desc, ctyp, expn=0):
        self.name = name
        self.cost = cost
        self.desc = desc
        self.ctyp = ctyp
        self.expn = expn

    def __repr__(self):
        return repr(self.name)

    def victoryValue(self, who):
        return self.__do(cTypes.Victory, who) or 0

    def treasureValue(self, who):
        return self.__do(cTypes.Treasure, who) or 0

    def action(self, who):
        self.__do(cTypes.Action, who)

    def attack(self, who):
        self.__do(cTypes.Attack, who)

    def __do(self, cType, who):
        """Find the appropriate function and call it if it exists"""
        if cType in self.ctyp:
            return self.ctyp[cType](who)

Curse = Card("Curse", 0, "-1 V", {cTypes.Victory: lambda x: -1})
Estate = Card("Estate", 2, "1 V", {cTypes.Victory: lambda x: 1})
Duchy = Card("Duchy", 5, "3 V", {cTypes.Victory: lambda x: 3})
Province = Card("Province", 8, "6 V", {cTypes.Victory: lambda x: 6})

Copper = Card("Copper", 0, "$1", {cTypes.Treasure: lambda x: 1})
Silver = Card("Silver", 3, "$2", {cTypes.Treasure: lambda x: 2})
Gold = Card("Gold", 6, "$3", {cTypes.Treasure: lambda x: 3})

Adventurer = Card("Adventurer", 6,
        "Reveal from deck until 2 treas. Put in hand and discard rest.",
        {cTypes.Action: None}, 1)
Bureaucrat = Card("Bureaucrat", 4,
        "Gain Silver onto deck. Others put v card from hand onto deck.",
        {cTypes.Action: None, cTypes.Attack: None}, 1)
Cellar = Card("Cellar", 2,
        "+1 Action. Discard X cards. +1 Card per each discard.",
        {cTypes.Action: None}, 1)
Chancellor = Card("Chancellor", 3,
        "+$2. You may put your deck into your discard.",
        {cTypes.Action: None}, 1)
Chapel = Card("Chapel", 2, "Trash up to 4 cards from your hand.",
        {cTypes.Action: None}, 1)
CouncilRoom = Card("Council Room", 5,
        "+4 Cards. +1 Buy. +1 Card for each other player.",
        {cTypes.Action: None}, 1)
Feast = Card("Feast", 4, "Trash this card. Gain a card costing up to $5",
        {cTypes.Action: None}, 1)
Festival = Card("Festival", 5, "+2 Actions. +1 Buy. +$2", {cTypes.Action:
    lambda x: x.addAction(2) and x.addBuys() and x.addMoneys(2)}, 1)
Gardens = Card("Gardens", 4, "Worth 1 V per 10 cards in your deck.",
        {cTypes.Victory: lambda x: len(x.deck) / 10}, 1)
Laboratory = Card("Laboratory", 5, "+2 Cards. +1 Action.",
        {cTypes.Action: lambda x: x.draw(2) and x.addAction()}, 1)
Library = Card("Library", 5,
        "+1 Card, may skip Actions. Repeat until 7 cards in hand.",
        {cTypes.Action: None}, 1)
Market = Card("Market", 5, "+1 Card. +1 Action. +1 Buy. +$1.", {cTypes.Action:
    lambda x: x.draw() and x.addAction() and x.addBuys() and x.addMoneys()}, 1)
Militia = Card("Militia", 4,
        "+$2. Other players discard down to 3 cards in hand.",
        {cTypes.Action: lambda x: x.addMoneys(2), cTypes.Attack: None}, 1)
Mine = Card("Mine", 5,
        "Trade treasure card in your hand for one costing $3 more.",
        {cTypes.Action: None}, 1)
Moat = Card("Moat", 2,
        "+2 Cards. Reveal when attacked to be unaffected.",
        {cTypes.Action: lambda x: x.draw(2), cTypes.Reaction: None}, 1)
Moneylender = Card("Moneylender", 4,
        "Trash a Copper card from your hand. If you do, +$3.",
        {cTypes.Action: None}, 1)
Remodel = Card("Remodel", 4,
        "Trash a card from your hand. Gain a card for up to $2 more.",
        {cTypes.Action: None}, 1)
Smithy = Card("Smithy", 4, "+3 Cards.", 
        {cTypes.Action: lambda x: x.draw(3)}, 1)
Spy = Card("Spy", 4,
        "+1 Card/Action. Each player reveals top, you may discard it.",
        {cTypes.Action: lambda x: x.draw() and x.addAction(), cTypes.Attack: None}, 1)
Thief = Card("Thief", 4,
        "Others reveal top 2 cards, trash a Treasure. Gain any subset.",
        {cTypes.Action: lambda x: True, cTypes.Attack: None}, 1)
ThroneRoom = Card("Throne Room", 3, "Play another Action, doing it twice.",
        {cTypes.Action: None}, 1)
Village = Card("Village", 3, "+1 Card. +2 Actions.",
        {cTypes.Action: lambda x: x.draw() and x.addAction(2)}, 1)
Witch = Card("Witch", 5, "+2 Cards. Each other player gains a Curse card.",
        {cTypes.Action: lambda x: x.draw(2), cTypes.Attack: lambda x: x.gainCard(card.Curse)}, 1)
Woodcutter = Card("Woodcutter", 3, "+1 Buy. +$2",
        {cTypes.Action: lambda x: x.addBuys() and x.addMoneys(2)}, 1)
Workshop = Card("Workshop", 3, "Gain a card costing up to $4.",
        {cTypes.Action: None}, 1)
