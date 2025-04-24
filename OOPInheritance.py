class Employee:
    increase_amount = 1.05
    def __init__(self,first_name,last_name,salary,department_name):
        print("Employee init method called")
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.department_name = department_name
    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)
    def display_info(self):
        print("------Type: {}-----".format(type(self).__name__))
        print("Full Name: {}\nSalary: {}\nDepartment: {}\n".format(self.full_name(),self.salary,self.department_name))
    def update_department(self,new_department):
        self.department_name = new_department
    def increase_salary(self,):
        self.salary = int(self.salary * self.increase_amount)
class Manager(Employee):
    increase_amount = 1.10

    def __init__(self, first_name, last_name, salary, department_name,emp_count):
        super().__init__(first_name, last_name, salary, department_name)
        self.emp_count = emp_count
    def display_info(self):
        super().display_info()
        print("Employee Count:",self.emp_count)
    def increase_emp(self,num_of_emps):
        self.emp_count += num_of_emps
    def decrease_emp(self,num_of_emps):
        self.emp_count -= num_of_emps
# emp1 = Employee("basu","herundi",50000,"human resource")
# emp2 = Employee("sharbu","hiremath",60000,"Information technology")

mgr1 = Manager("basu","herundi",50000,"human resource",100)
mgr2 = Manager("sharbu","hiremath",60000,"Information technology",150)

# mgr1.display_info()
# mgr2.display_info()
# mgr1.update_department("Marketing")
# mgr1.display_info()

# help(Manager)
# print(mgr1.salary)
# mgr1.increase_salary()
# print(mgr1.salary)

mgr1.display_info()
mgr2.display_info()
mgr1.increase_emp(100)
mgr1.display_info()
mgr1.decrease_emp(25)
mgr1.display_info()