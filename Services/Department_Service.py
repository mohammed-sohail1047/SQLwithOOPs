# class DeptService:
#     def __init__(self, dept_Repository):
#     self.dept_repository = dept_Repository

#     def Insert_department(self, department):
#         return self.dept_repository.insert_department(department)

#     def Update_department_department(self, department):
#         return self.dept_repository.update_department(department)

#     def Delete_department_department(self, department):
#         return self.dept_repository.delete_department(department)

#     def Get_all_departments(self):
#         return self.dept_repository.get_all_departments()

#     def Get_department_by_DeptNo(self, deptNo):
#         return self.dept_repository.get_department_by_deptNo(deptNo)

#     def Get_department_by_Dname(self, dname):
#         return self.dept_repository.get_department_by_dname(dname)



class DeptService:
    def __init__(self, dept_repository):
        self.dept_repository = dept_repository

    def Insert_department(self, department):
        return self.dept_repository.insert_department(department)
    
    def Update_department(self, department):
        return self.dept_repository.update_department(department)
    
    def Delete_department(self, deptNo):
        return self.dept_repository.delete_department(deptNo)
    
    def Get_all_departments(self):
        return self.dept_repository.get_all_departments()
    
    def Get_department_by_deptNo(self, deptNo):
        return self.dept_repository.get_department_by_deptNo(deptNo)
    
    def Get_departments_by_dname(self, Dname):
        return self.dept_repository.get_departments_by_dname(Dname)
