class Employee():
    def __init__(self, name, age, salary):
        self.name= name
        self.age= age
        self.salary= salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, val):
        if val < 10000:
            raise ValueError("❌ Salary cannot be below 10000!")
        self._salary = val
        return val
    
    @property
    def annual_salary(self):
        return self._salary * 12

class Teacher(Employee):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age, salary)
        self.subject = subject

    @classmethod
    def show(cls, data):
        name, age, salary, subject = data.split("-")
        age = int(age)
        return cls(name, age, salary, subject)
    
    def show_details(self):
        print(f"---Teacher Details---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary}")
        print(f"Subject: {self.subject}")

class Developer(Employee):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language

    @classmethod
    def from_string(cls, data):
        name, age, salary, language = data.split("-")
        age = int(age)
        salary = int(salary)
        return cls(name, age, salary, language)
    
    def show_details(self):
        print(f"---Developer Details---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary}")
        print(f"Annual Salary: ${self.annual_salary}")
        print(f"Programming Language: {self.language}")

class ContractMixin:
    def __init__(self, contract_years):
        self.contract_years = contract_years

    def contract_end_year(self, current_year):
        return current_year + self.contract_years

class ContractTeacher(ContractMixin, Teacher):
    def __init__(self, name, age, salary, subject, contract_years):
        ContractMixin.__init__(self, contract_years)
        Teacher.__init__(self, name, age, salary, subject)
               
    @classmethod
    def from_string(cls, data):
        name, age, salary, subject, contract_years = data.split("-")
        age = int(age)
        salary = int(salary)
        contract_years = int(contract_years)
        return cls(name, age, salary, subject, contract_years)
    
    def show_details(self):
        super().show_details() 
        print(f"Contract Years: {self.contract_years}")


t1 = ContractTeacher.from_string("Qumbar-17-15000-Math & Physics-5")
t1.show_details()
print(f"Annual Salary: ${t1.annual_salary}")
print(f"Contract End Year: {t1.contract_end_year(2025)}")
d1 = Developer.from_string("Tahir-18-25000-Python")
d1.show_details()


