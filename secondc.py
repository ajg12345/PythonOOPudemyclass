#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class Employee:
    name = "Ben"
    designation = "Sales Exec"
    salesMadeThisWeek = 6
    def hasAcheivedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print('Acheived')
        else:
            print('Not Acheived')

e1 = Employee()
e1.name = "Ben"
print(e1.name)
print(type(e1))
