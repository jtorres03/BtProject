"""Imports"""

import pandas as pd

df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})

#object variable(more common to use the term/s attribute/property)
# df.columns

#object fucntion(more common to use the term methods)
# df.describe()

class Wallet:
    """This is a docstring. Which is comments for others to view who do not have acces to
    the source code. Will be seen when someone requests 'help' for a function or class."""
    #constructor method/function
    def __init__(self, amount):
        print('building a wallet')
        self.balance = amount

    def spend(self, amount):
        """Spend amount"""
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Not enough cash!")

    def add_money(self, amount):
        """Deposit"""
        self.balance = self.balance + amount        
if __name__ == '__main__':
    w = Wallet(25)
    w.add_money(100)
    print(w.balance)
    w.spend(50)
    print(w.balance)
    w.spend(10000)
    print(w.balance)
