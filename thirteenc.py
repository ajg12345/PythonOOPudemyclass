#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class Apple:
    manufacturer = "Apple"
    contactWebsite = "www.doodooodoooooHAHA.com"

    def contactDetails(self):
        print('go to ' + self.contactWebsite + ' for a good time')

class Macbook(Apple):
    
    def __init__(self):
        self.yearOfManufacture = 1998


    def manufactureDetails(self):
        print("This was built by {} in the year {}".format(self.manufacturer, self.yearOfManufacture))

compy = Macbook()
compy.manufactureDetails()
compy.contactDetails()

