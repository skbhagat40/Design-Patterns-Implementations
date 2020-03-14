class Duck:
    def __init__(self, name):
        self.name = name

    def quack(self):
        print('quack')

    def display(self):
        print('*' * 10)
        print('Duck {}'.format(self.name))
        print('*' * 10)

    def fly(self):
        pass


# Need to override fly method everywhere.
class RedDuck(Duck):
    def fly(self):
        print('Normal Fly')


class YellowDuck(Duck):
    def fly(self):
        print('Normal Fly')


class RubberDuck(Duck):
    def fly(self):
        raise Exception("Rubber Duck Can't Fly")  # This is bad and we don't want it. Also no code re-use.


class PaperDuck(Duck):
    def fly(self):
        raise Exception("Rubber Duck Can't Fly")  # This is bad and we don't want it


class PlasticDuck(Duck):
    def fly(self):
        raise Exception("Rubber Duck Can't Fly")  # This is bad and we don't want it
