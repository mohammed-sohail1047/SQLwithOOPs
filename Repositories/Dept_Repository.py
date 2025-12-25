from abc import ABC, abstractmethod

# Abstract class for Department Repository:

class Dept_Repository(ABC):
    @abstractmethod
    def I(self, department):
        pass

    @abstractmethod
    def Update_department(self, department):
        pass

    @abstractmethod
    def Delete_department(self, dept_no):
        pass

    @abstractmethod
    def Get_all_departments(self):
        pass

    @abstractmethod
    def Get_department_by_DeptNo(self, dept_no):
        pass

    @abstractmethod
    def Get_department_by_Dname(self, dname):
        pass

    