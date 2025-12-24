from abc import ABC, abstractmethod

# Abstract class for Department Repository:

class Dept_Repository(ABC):
    @abstractmethod
    def insert_department(self, department):
        pass

    @abstractmethod
    def update_department(self, department):
        pass

    @abstractmethod
    def delete_department(self, dept_no):
        pass

    @abstractmethod
    def get_all_departments(self):
        pass

    @abstractmethod
    def get_department_by_DeptNo(self, dept_no):
        pass

    @abstractmethod
    def get_department_by_Dname(self, dname):
        pass

    