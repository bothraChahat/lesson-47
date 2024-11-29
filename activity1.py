#Write a program to create a parent class Person (attributes - name, idnumber) with a method display to display the attributes.

class person:
   def __init__(self,name,idnumber):
     self.name=name
     self.idnumber=idnumber
   def display(self):
      print("name of person is",self.name)
      print("idnumber of person is ",self.idnumber)

#child class
class employee(person):
     def __init__(self, name , idnumber, salary,post):
        self.salary=salary
        self.post=post
        super().__init__(name,idnumber)

emp=employee("anurag",1234,20000,"intern")
emp.display()
