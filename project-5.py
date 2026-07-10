class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age!")

    def display(self):
        print("\nPerson Details:")
        print("Name :", self.__name)
        print("Age  :", self.__age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.__emp_id = emp_id
        self.__salary = salary

    
    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name :", self.get_name())
        print("Age :", self.get_age())
        print("Employee ID :", self.__emp_id)
        print("Salary : ₹", self.__salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.__department = department

        def display(self):
          print("\nManager Details:")
          print("Name :", self.get_name())
          print("Age :", self.get_age())
          print("Employee ID :", self.get_emp_id())
          print("Salary : ₹", self.get_salary())
          print("Department :", self.__department)


person = None
employee = None
manager = None

print("\n--- Python OOP Project: Employee Management System ---")

while True:

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))

            person = Person(name, age)

            print(f"\nPerson created with name: {name} and age: {age}.")

        elif choice == 2:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))

            employee = Employee(name, age, emp_id, salary)

            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ₹{salary}.")

        elif choice == 3:

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            department = input("Enter Department: ")

            manager = Manager(name, age, emp_id, salary, department)

            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ₹{salary}, and department: {department}.")

        elif choice == 4:

            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")

            show = int(input("Enter your choice: "))

            if show == 1:
                if person:
                    person.display()
                else:
                    print("Person not created!")

            elif show == 2:
                if employee:
                    employee.display()
                else:
                    print("Employee not created!")

            elif show == 3:
                if manager:
                    manager.display()
                else:
                    print("Manager not created!")

            else:
                print("Invalid Choice!")

        elif choice == 5:

            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            break

        else:
            print("Invalid Choice!")

        print("\n--- Choose another operation ---")

    except ValueError:
        print("Please enter valid numeric input!")