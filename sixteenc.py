#!/home/aaron4udemy/anaconda3/envs/udem/bin/python

# public syntax is exampleName
#   available for use anywhere
# protected syntax is _exampleName
#   only for class and derived classes
# private syntax is __exampleName
#   only for the class

class StringInstrument():
    wood = 'tonewood'
    _lowstring = 'E'
    __owner = 'Aaron'

class Guitar(StringInstrument):
    
    def __init__(self):
        print("protected attribute inside inherited function {} .".format(self._lowstring))

strummy = StringInstrument()
print('public attribute wood: ', strummy.wood )

axe = Guitar()
print('Protected attribute lowsstring: ', axe._lowstring)
#this next commented out line will not work
#this is because of a characteristic of python called mangling, avoided later below
#print('Private attribute owner: ', axe.__owner)
#however, this next line would work because technically thats what the name becomes:
print('Private atribute owner: ', axe._StringInstrument__owner)
