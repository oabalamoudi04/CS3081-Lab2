import termcolor

from logic import *

alice = Symbol("AliceSuspect")
bob = Symbol("BobSuspect")
carol = Symbol("CarolSuspect")
characters = [alice, bob, carol]

office = Symbol("office")
garage = Symbol("garage")
basement = Symbol("basement")
rooms = [office, garage, basement]

poison = Symbol("poison")
rope = Symbol("rope")
candlestick = Symbol("candlestick")
weapons = [poison, rope, candlestick]

symbols = characters + rooms + weapons

def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(alice, bob, carol),
    Or(office, garage, basement),
    Or(poison, rope, candlestick)
)

# Cards in your hand
knowledge.add(And(
    Not(alice),
    Not(office),
    Not(poison)
))

# Opponent showed you one of these
knowledge.add(Or(
    Not(bob),
    Not(garage),
    Not(rope)
))

# Separately learned
knowledge.add(Not(candlestick))
knowledge.add(Not(basement))

check_knowledge(knowledge)
