class Student():
    def __init__ (self,section,roll_no):
        self.section = section
        self.roll_no = roll_no
        print(section)
    def college(self):
        print('GLA University') 
s1=Student('A',23) 
s1.college()        