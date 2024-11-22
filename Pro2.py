class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

    def details(self):
        return f"Person [Name: {self.name}, Age: {self.age}]"


class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.employee_id = employee_id
        self.position = position

    def display(self):
        # Call the display method from the Person class
        person_info = super().display()
        return f"{person_info}, Employee ID: {self.employee_id}, Position: {self.position}"

    def details(self):
        # Override the details method to modify behavior
        return f"Employee [Name: {self.name}, Age: {self.age}, ID: {self.employee_id}, Position: {self.position}]"


# Example usage
if __name__ == "__main__":
    emp = Employee("Alice", 30, "E123", "Software Engineer")
    
    print(emp.display())  # Calls the display method from Employee
    print(emp.details())  # Calls the overridden details method from Employee
