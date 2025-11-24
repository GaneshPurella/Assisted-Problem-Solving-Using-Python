class Employee:
    """
    A class to represent an employee and manage salary operations.
    """

    def __init__(self, name, salary):
        """
        Initialize employee with name and salary.

        Parameters
        ----------
        name : str
            Name of the employee.
        salary : float
            Current salary of the employee.
        """
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        """
        Increase the salary by a given percentage.

        Parameters
        ----------
        percent : float
            Percentage by which salary should be increased.
        """
        self.salary += self.salary * (percent / 100)

    def display_info(self):
        """
        Display employee details in formatted output.
        """
        print(f"\nEmployee Name: {self.name}")
        print(f"Current Salary: {self.salary}")


# ---------- USER INPUT ----------
name = input("Enter Employee Name: ")
salary = float(input("Enter Employee Salary: "))
percent = float(input("Enter Percentage Increase: "))

# Create object
emp = Employee(name, salary)

print("\nBefore Increment:")
emp.display_info()

# Apply salary increment
emp.increase_salary(percent)

print("\nAfter Increment:")
emp.display_info()