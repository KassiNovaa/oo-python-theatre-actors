from .audition import Audition

class Actor:
    def __init__(self, name ):
        self.name = name

    @property
    def auditions(self):
        return [ audition for audition in Audition.all if audition.actor == self ]
    
    @property
    def roles(self):
        return [ audition.role for audition in self.auditions ]
    
    @property
    def characters(self):
        return list({ audition.role.character_name for audition in self.auditions })
    
    @property
    def paychecks(self):
        return list({ audition.role.character_name for audition in self.auditions if audition.hired })

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            print('ERROR: name must be a string')

