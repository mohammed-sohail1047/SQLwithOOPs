class EmpService:
    def __init__(self, emp_Repository):
        self.emp_Repository = emp_Repository

    def insert_employee(self, employee):
        return self.emp_Repository.insert_employee(employee)
    
    def update_employee(self, employee):
        return self.emp_Repository.update_employee(employee)
    
    def delete_employee(self, emp_Id):
        return self.emp_Repository.delete_employee(emp_Id)
    
    def get_all_employees(self):
        return self.emp_Repository.get_all_employees()
    
    def get_employee_by_EmpId(self, emp_Id):
        return self.emp_Repository.get_employee_by_EmpId(emp_Id)
    
    def get_employee_by_deptNo(self, dept_No):
        return self.emp_Repository.get_employee_by_deptNo(dept_No)
    
    def get_employee_by_gender(self, gender):
        return self.emp_Repository.get_employee_by_gender(gender)   
    
    def get_employee_order_by_salary(self, ascending=True):
        return self.emp_Repository.get_employee_order_by_salary(ascending)
    
    