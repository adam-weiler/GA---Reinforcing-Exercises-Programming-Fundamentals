emotions = { 'happiness': 3, 'stress': 2, 'fear': 1, 'joy': 3, 'trust': 2, 'surprise': 1, 'ancitipation': 3, 'hope': 2, 'confusion': 1 } #A dictionary to store different human emotions and the value they are being felt.

class Person(): #A Person class.
    def __init__(self, name): #Every person has properties name, and emotions.
        self.name = name
        self.emotions = emotions

    def evaluate_feeling(self, rating): #Takes a rating of 1, 2, or 3 and returns a string of 'low', 'medium', or 'high'. 
        if (rating == 3):
            return 'high'
        elif (rating == 2):
            return 'medium'
        else:
            return 'low'

    def describe(self): #Prints a string describing how the Person feels for each emotion in the dictionary.
        for emotion, rating in self.emotions.items(): #Iterates through the emotions dictionary.
            print(f'I am feeling a {self.evaluate_feeling(rating)} amount of {emotion}.')

matthew = Person('Matthew')
# print(matthew)
matthew.describe()
print()

john = Person('John')
# print(john)
john.describe()
print()

#These are extra things inside the john object.
# print (john.__dict__) #Dictionary containing the class's namespace: {'name': 'John', 'emotions': {'happiness': 3, 'stress': 2, 'fear': 1, 'joy': 3, 'trust': 2, 'surprise': 1, 'ancitipation': 3, 'hope': 2, 'confusion': 1}}
# print (john.__doc__) #Class documentation string: None
    # print (john.__name__) #Class name: There is no attribute __name__
# print (john.__module__) #Module name in which the class is defined: __main__
    # print (john.__bases__) #A possibly empty tuple containing the base classes, in the order of their occurance in the base class list: There is no attribute __bases__