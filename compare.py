class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __gt__(self, other):
        if isinstance(other, Employee):
            return self.salary > other.salary
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        return NotImplemented

e1 = Employee("Tarun", 50000)
e2 = Employee("Rahula", 60000)
# compar
print(e1 > e2)  
print(e1 < e2)
