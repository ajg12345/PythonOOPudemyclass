#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class OperatingSystem():
    multitasking = True
    name = 'MacOS'

class Apple:
    manufacturer = "Apple"
    contactWebsite = "www.doodooodoooooHAHA.com"
    name = "Apple Computer"

    def contactDetails(self):
        print('go to ' + self.contactWebsite + ' for a good time')

class Macbook(Apple, OperatingSystem):
    
    def __init__(self):
        self.yearOfManufacture = 1998
        if self.multitasking:
            print('you are ready to multitask visit {} for more'.format(self.contactWebsite))
        print(self.name)
    def manufactureDetails(self):
        print("This was built by {} in the year {}".format(self.manufacturer, self.yearOfManufacture))

compy = Macbook()

