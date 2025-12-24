# Employee Model Class / DB Entity Class:

class Employee:
    def __init__(self, EmpID, Ename, Password, Gender, DOB, Phone, Email, Salary, Address, DeptNo):
        self.empId = EmpID 
        self.ename = Ename
        self.password = Password
        self.gender = Gender
        self.dob = DOB
        self.phone = Phone
        self.email = Email
        self.salary = Salary
        self.address = Address
        self.deptNo = DeptNo