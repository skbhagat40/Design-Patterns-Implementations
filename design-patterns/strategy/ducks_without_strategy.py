class Duck:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print('quack')

    def display(self):
        print('*' * 10)
        print('Duck {}'.format(self.name))
        print('*' * 10)


class RedDuck(Duck):
    pass


class YellowDuck(Duck):
    pass


class RubberDuck(Duck):
    pass


class PaperDuck(Duck):
    pass


class PlasticDuck(Duck):
    pass


rd = RubberDuck('foo')
rd.display()
rd.quack()

# Requirement to add fly behavior.
