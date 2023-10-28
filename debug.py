import ipdb
from lib import *

# Test your code below...

r1 = Role('Sarabi')
r2 = Role('Simba')
r3 = Role('Cinderella')
r4 = Role('Prince Charming')
r5 = Role('Mrs.Potts')
r6 = Role('Chip')
r7 = Role('Ariel')
r8 = Role('Flounder')


a1 = Actor('Kassidy')
a2 = Actor('Shiloh')
a3 = Actor('Khloe')

audition1 = Audition('New York', True, r1, a1)
audition2 = Audition('New York', True, r2, a2)

audition3 = Audition('LA', False, r3, a1)
audition4 = Audition('LA', True, r4, a2)
audition5 = Audition('LA', True,r3, a3)

audition6 = Audition('Orlando', True, r5, a1)
audition7 = Audition('Orlando', True, r6, a2)

audition8 = Audition('London', True, r7, a1)
audition9 = Audition('London', False, r8, a2)
audition10 = Audition('London', True, r8, a3)


# the below line allows us to stop & try stuff!
ipdb.set_trace()