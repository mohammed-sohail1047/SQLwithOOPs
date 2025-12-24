from abc import ABC, abstractmethod

# Abstract class for Employee Repository:

class Emp_Repository(ABC):
    @abstractmethod
    def insert_employee(self, Employee):
        pass

    @abstractmethod
    def update_employee(self, Employee):
        pass

    @abstractmethod
    def delete_employee(self, EmpID):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def get_employee_by_EmpId(self, EmpID):
        pass

    @abstractmethod
    def get_employee_by_Ename(self, Ename):
        pass

    