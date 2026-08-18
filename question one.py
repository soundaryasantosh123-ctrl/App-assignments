class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)
        print("Category    :", self.category())
        print("-" * 30)


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(employee_id, name, salary)
        self.employees.append(employee)

        print("Employee added successfully!\n")

    def display_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            print("\n--- Employee Information ---")
            for employee in self.employees:
                employee.display()



company = Company()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        company.add_employee()

    elif choice == "2":
        company.display_employees()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
