class FlyMeta(type):
    def __new__(cls, name, bases, body):
        if name != 'FlyInterface' and 'fly' not in body:
            raise Exception("Please Implement 'fly' method in your subclass")
        return super().__new__(cls, name, bases, body)


class FlyInterface(metaclass=FlyMeta):
    pass


class Duck:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print('quack')

    def display(self):
        print('*' * 10)
        print('Duck {}'.format(self.name))
        print('*' * 10)


class RedDuck(Duck, FlyInterface):
    # prevents code re-use.
    def fly(self):
        print('Normal fly')


class YellowDuck(Duck, FlyInterface):
    def fly(self):
        print('Normal fly')


# Need to override fly method everywhere.
class RubberDuck(Duck):
    pass


class PaperDuck(Duck):
    pass


class PlasticDuck(Duck):
    pass
