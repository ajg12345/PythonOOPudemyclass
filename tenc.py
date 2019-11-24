#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class Employee:

    def __init__(self,thename):
        self.name =  thename
    
    
    
    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee('jimbo')
employee.displayEmployeeDetails()

#notice we demonstrated the init special method (its special so it has two underscores)
#whats special about it is that its called automatically when the class instance is created
