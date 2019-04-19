from types import InstanceType
import card

iscard = lambda e: isinstance(e, InstanceType) and e.__class__ is card.Card

li = [item for item in card.__dict__.values() if iscard(item)]

common = [item for item in li if item.expn == 0]
base = [item for item in li if item.expn == 1]
intrigue = [item for item in li if item.expn == 2]
