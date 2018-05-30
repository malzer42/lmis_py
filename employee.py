"""employee.py."""


# Author(s): Pierre Abraham Mulamba
# Date of creation (modification): 20180525 (20180525)


import sys
print(sys.executable)
print(sys.version)


class Employee:
    """docstring for Employee."""

    nEmployees = 0

    def __init__(self, name, age, salary):
        """Ctor"""
        self.name_ = name
        self.age_ = age
        self.salary_ = salary
        Employee.nEmployees += 1

    def __repr__(self):
        """Return the representation of an Employee--for developer."""
        return f"Employee({self.name_}, {self.age_}, ${self.salary_})"

    def __str__(self):
        """Method to tells Python how it wants this function represented."""
        return f'({self.name_}, {self.age_}, ${self.salary_})'

    def test_method(self):
        pass

    @property
    def email(self):
        """docstring"""
        return '{}.{}@email.com'.format(self.first_, self.last_)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_, self.last_)


def employee_sort(employee):
    """Return a value used for sorting a list of employees."""
    return employee.name_
