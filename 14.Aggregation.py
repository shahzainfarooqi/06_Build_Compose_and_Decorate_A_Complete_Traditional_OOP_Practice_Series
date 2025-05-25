
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        print(f"[Employee] Created Employee: {self.name}, ID: {self.emp_id}")

    def display(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")



class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee 
        print(f"[Department] Department '{self.dept_name}' created with employee reference.")

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  



def main():
   
    emp = Employee("Alice", 101)

 
    dept = Department("Human Resources", emp)

   
    dept.show_details()

   
    print("\nAccessing employee directly:")
    emp.display()


if __name__ == "__main__":
    main()
