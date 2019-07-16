emotions = { 'happiness': 3, 'stress': 2, 'fear': 1, 'joy': 3, 'trust': 2, 'surprise': 1, 'ancitipation': 3, 'hope': 2, 'confusion': 1 } #A dictionary to store different human emotions and the value they are being felt.

class Person():
    def __init__(self, name):
        self.name = name
        self.emotions = emotions
        self.somenum = 9

    def describe(self):
        
        for emotion, rating in self.emotions.items():
            # print(emotion)
            # print(rating)

            if (rating == 3):
                print(f'e')

            print(f'I am feeling a {emotion} amount of {emotion}')

    
    def __add__(self, other):
        return other + self.somenum
            


matthew = Person('Matthew')

# print(matthew)
# matthew.describe()

print(matthew.__add__(5))


# I am feeling a high amount of happiness.
# I am feeling a medium amount of stress.
# I am feeling a low amount of fear.