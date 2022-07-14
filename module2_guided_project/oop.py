
# Class to be inherited
class Animal:
    def __init__(self, my_name):
        self.name = my_name
    
    def say_hi(self):
        print(self.name + "says: " + self.sound)


class Cat(Animal):
    sound = 'meowmix!'

    # you can override the parent function by defining your own function within child class
    def say_hi(self):
        print('MEOWMEOW!!!!!')

    # REQUIRED NAME FOR CONSTRUCTOR FUNCTION 
    # def __init__(self, name):
    #     self.name = name

    # def say_hi(self):
    #     print(self.name + 'meow!')


class Dog(Animal):
    sound = 'woof!'
   
    # REQUIRED NAME FOR CONSTRUCTOR FUNCTION 
    # def __init__(self, name):
    #     self.name = name
    
    # def say_hi(self):
    #     print(self.name + 'woof!')
    
