from .audition import Audition

class Role:
    def __init__(self, character_name):
        self.character_name = character_name

    @property
    def auditions(self):
        return [ audition for audition in Audition.all if audition.role == self ]
    
    @property
    def actors(self):
        return [ audition.actor.name for audition in self.auditions ]
    
    @property
    def locations(self):
        return [ audition.location for audition in self.auditions ]
    
    @classmethod
    def silver_screen(cls):
        return list({ audition.role.character_name for audition in Audition.all if audition.hired })
    


    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name (self, new_character_name ):
        if type( new_character_name ) == str:
            self._character_name = new_character_name
        else : 
            print ('ERROR: name must be a string')