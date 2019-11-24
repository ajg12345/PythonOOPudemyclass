#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class MusicalInstruments:
    keycount = 12

class StringInstruments(MusicalInstruments):
    wood = 'tonewood'

class Guitar(StringInstruments):
    
    def __init__(self):
        self.numberOfStrings = 6
        print("This has {} and is made of {} and can play {} keys.".format(self.numberOfStrings, self.wood, self.keycount))

strummy = Guitar()

