#!/home/aaron4udemy/anaconda3/envs/udem/bin/python

class Furniture():
    ftype = 'Teakwood'

class Chair(Furniture):
    __numberOfLegs = 3
    def __init__(self):
        print('press 1 to furniture type?')
        response = input()
        if response == '1':
            print('whats the new furniture type, then big guy?')
            self.ftype = input()

myChair = Chair()
print(myChair.ftype)
