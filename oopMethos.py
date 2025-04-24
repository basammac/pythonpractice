class Employee:
    def __init__(self,first_name,last_name,salary,skills):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
        self.skills=skills
        self.email=first_name + "." + last_name + "@company.com"
    def display_info(self):
        print("""
          
          first name  : {}
          
          last name : {}
          
          salary : {}
          
          skills : {}
          
          email : {}
          
            
       """.format(self.first_name,self.last_name,self.salary,self.skills,self.email) )

emp1= Employee("basamma","herundi",50000,["python","java","ruby"])
print(emp1)
print(emp1.display_info())

def increase_salary(self):
        self.salary = int(self.salary * 1.05)
print(emp1.salary)
emp1.increase_salary()
print(emp1.salary)
def add_skill(self,new_skill):
          print("new skill added")
          self.skills.append(new_skill)
