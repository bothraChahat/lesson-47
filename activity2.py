class person:
    def __init__(self,fname,lname):
     self.fname=fname
     self.lname=lname
    def display(self):
       print("name of person is {} {}".format(self.fname,self.lname))

class student(person):
   def __init__(self,fname,lname, year):
     self.graduationyear=year
     super().__init__(fname,lname)

stud=student("chahat","bothra",2011)
stud.display()
print("graduation year is",stud.graduationyear)

   