__author__ = 'Amine Banks'

class hola:
    name = 'Jordi'
    def __init__(self, name):
        self.name=name
    def setNomre(self):
        return self.name
    def function(self):
        for i in self.name:
            print(self.setNomre())


a = hola('name')
a.function()

