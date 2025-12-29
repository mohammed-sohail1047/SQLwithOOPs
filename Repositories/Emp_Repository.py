from abc import ABC, abstractmethod

# Abstract class for Employee Repository:

class EmpRepository(ABC):
    @abstractmethod
    def insert_employee(self, employee):
        pass

    @abstractmethod
    def update_employee(self, employee):
        pass

    @abstractmethod
    def delete_employee(self, empId):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def get_employee_by_EmpId(self, empId):
        pass

    @abstractmethod
    def get_employee_by_deptNo(self, deptNo):
        pass

    @abstractmethod
    def get_employee_by_gender(self, gender):
        pass

    @abstractmethod
    def get_employee_order_by_salary(self, acsending=True):
        pass

    