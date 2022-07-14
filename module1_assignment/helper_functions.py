import random


def random_phrases():
    adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
    nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

    phandom_rase = random.choice(adjectives) + " " + random.choice(nouns)

    return phandom_rase

print(random_phrases())