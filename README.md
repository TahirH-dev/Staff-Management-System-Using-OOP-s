# Staff Management System (OOP in Python)

A simple Python project demonstrating Object-Oriented Programming (OOP) concepts such as inheritance, multiple inheritance, encapsulation, and class methods.  
The system manages different types of employees — Teachers, Developers, and Contract Teachers — with salary validation and contract duration features.

## Features
- **Employee Base Class** with salary validation and annual salary calculation.
- **Teacher Class** with subject specialization.
- **Developer Class** with programming language specialization.
- **Contract Teacher Class** combining teaching and contract management.
- Uses **property decorators**, **class methods**, and **multiple inheritance**.

## Example Usage
```python
t1 = ContractTeacher.from_string("Qumbar-17-15000-Math & Physics-5")
t1.show_details()
print(f"Annual Salary: ${t1.annual_salary}")
print(f"Contract End Year: {t1.contract_end_year(2025)}")

d1 = Developer.from_string("Tahir-18-25000-Python")
d1.show_details()



