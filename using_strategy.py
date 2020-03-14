class FlyMeta(type):
    def __new__(cls, name, bases, body):
        if name != 'FlyInterface' and 'fly' not in body:
            raise Exception("Please Implement 'fly' method in your subclass")
        return super().__new__(cls, name, bases, body)


class FlyInterface(metaclass=FlyMeta):
    pass


class FlyNormalWay(FlyInterface):
    def fly(self):
        print('Flying Normally')


class FlyWithPlane(FlyInterface):
    def fly(self):
        print('Flying with plane!!')


class Duck:
    def __init__(self, name, flyBehavior=None):
        self.name = name
        self.flyBehavior = flyBehavior

    def makeDuckFly(self):
        if self.flyBehavior:
            self.flyBehavior.fly()

    def changeFlyBehavior(self, flyBehavior):
        self.flyBehavior = flyBehavior

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


redDuck = RedDuck('sam', FlyNormalWay())
redDuck.makeDuckFly()
redDuck.changeFlyBehavior(FlyWithPlane())
redDuck.makeDuckFly()

rubberDuck = RubberDuck('foo', FlyWithPlane())
rubberDuck.display()
rubberDuck.makeDuckFly()
