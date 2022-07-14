"""Imports"""
import random
import numpy as np
import pandas as pd

# Part 3 Functions =============================================================================

def random_phrase():
    """Generate random two word phrase"""
    nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']
    adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    return adjective + ' ' + noun 

def random_float(min_val, max_val):
    """Generate random float"""
    return random.uniform(min_val, max_val)
    
def random_bowling_score():
    """Generate random integer"""
    return random.randint(0, 301)

def silly_tuple():
    """Return a tuple"""
    return (random_phrase(), round(random_float(1,5),1), random_bowling_score())

def silly_tuple_list(num_tuples):
    """return a list"""
    list = []
    for items in range(num_tuples):
        list.append(silly_tuple())
    return list


# Part 3 Functions =============================================================================

test_df = pd.DataFrame(np.array([[1,np.nan,3,4], [5,6,7,8], [9,10,11,12]]))

def null_count(df):
    """count null values"""
    return df.isnull().sum().sum()

def train_test_split(df, frac=0.8):
    """Train test split fx"""
    train = df.sample(frac=frac)
    test = df.drop(train.index).sample(frac=1.0)
    return train, test

print(random_phrase())