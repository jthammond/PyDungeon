from random import randrange

def diceRoll(max, min=1):
    return randrange(min, max)

def d4():
    return randrange(1, 4)

def d6():
    return randrange(1, 6)

def d8():
    return randrange(1, 8)

def d10():
    return randrange(1, 10)

def d12():
    return randrange(1, 12)

def d20():
    return randrange(1, 20)

def d100():
    return randrange(1, 100)
