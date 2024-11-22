
from datetime import datetime

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
    
    def calculate_age(self):
        today = datetime.now()
        age = today.year - self.date_of_birth.year
        
        # Check if the birthday has occurred this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        
        return age

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.date_of_birth.strftime('%Y-%m-%d')}, Age: {self.calculate_age()}"

# Example usage
if __name__ == "__main__":
    person1 = Person("Alice", "USA", "1990-05-15")
    person2 = Person("Bob", "Canada", "1985-11-30")

    print(person1)
    print(person2)
