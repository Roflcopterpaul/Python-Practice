import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

class Bard(Character):
    musically_talented = True

    def lullaby(self):
        return self.musically_talented and bool(random.randint(0, 1))

    def soothe(self, ambiance):
        return self.musically_talented and ambiance > 7
