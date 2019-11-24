#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class Employee:
    def employeeDetails(self):
        self.name = "Ben"
    @staticmethod
    def welcomeMessage():
        print('hey there')

employee = Employee()
employee.employeeDetails()

print(employee.name)
employee.welcomeMessage()

#how about this static method, it doesn't need a "self" parameter
#we indicate that its a static method because it uses the @staticmethod decorator
