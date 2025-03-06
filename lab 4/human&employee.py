class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking.")

class Employee(Human):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def work(self):
        print(f"{self.name} is working as a {self.job}.")

# Example Usage
person = Human("mariam", 22)
person.speak()

employee = Employee("bebo", 27, "Engineer")
employee.speak()
employee.work()
