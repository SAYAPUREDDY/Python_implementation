class Person:
    '''docstring: a basic person class'''
    nPerson = 0  # class variable

    # special constructor method __init__
    def __init__(self, kg, cm):
        self.kg = kg  # instance variable
        self.cm = cm
        Person.nPerson = Person.nPerson + 1
        self._calls = 0

    def getWeight(self):  # instance method
        return self.kg

    def eat(self, amount):
        self.kg = self.kg + amount

    def run(self, distance):
        print(f'Running {distance} kilometers...')
        self.kg = self.kg - distance * 0.1
        self._privateMeth(distance)

    def _privateMeth(self, msg):
        print('Private method called with', msg)
        self._calls = self._calls + 1

if __name__ == '__main__':
    # check if running this file itself
    print('ok')