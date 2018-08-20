class Infix():
    def __init__(self, function):
        self.function = function

    def __ror__(self, x):
        return Infix(lambda y: self.function(x, y))

    def __or__(self, y):
        return self.function(y)

    def __rlshift__(self, x):
        return Infix(lambda y: self.function(x, y))

    def __rshift__(self, y):
        return self.function(y)
