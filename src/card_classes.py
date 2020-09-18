
#class definition for pokemon and trainer cards.
class pokemon:
    def _init_(self, name,):
        self.name = name
        self.attacks = {}
        self.type = ''
        self.series = ''
        self.num = 0

class trainer:
    def _init_(self, name):
        self.name = name
        self.effects = ''
        self.series = ''

