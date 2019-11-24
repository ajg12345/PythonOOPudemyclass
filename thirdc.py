#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class Employee:
    def employeeDetails():
        pass

employee = Employee()
#this generates an error because it was defined with no (self) reference
employee.employeeDetails()
#technically, internally python calls the function like this:
#Employee.employeeDetails(employee)
