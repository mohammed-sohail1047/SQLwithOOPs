from db.MySQLConnection import MySQLConnection
from Repositories.Dept_Repository_Imp import DeptRepositoryImp
from Repositories.Emp_Repository_Imp import EmpRepositoryImp
from Services.Department_Service import DeptService
from Services.Employee_Service import EmpService
from Models.Department import Department
from Models.Employee import Employee

def Department_CRUD_Operations():
    connection = MySQLConnection().get_connection()
    deptRepository = DeptRepositoryImp(connection)
    deptService = DeptService(deptRepository)

    print("\nDepartment CRUD Operations : ")
    print("1. Insert Department Record")
    print("2. Update Department Record")
    print("3. Delete Department Record")
    print("4. Fetch All Department Records")
    print("5. Fetch Department Record by DeptNo")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:        
        dept_no = int(input("Enter DeptNo: "))
        dept_name = input("Enter Dname: ")
        dept_location = input("Enter Location: ")
        dept = Department(dept_no, dept_name, dept_location)
        #Validate DeptNo and Dname before insertion
        deptValid = deptService.Get_department_by_deptNo(dept.DeptNo)      
        if deptValid:
            print("Already Department with this DeptNo exists. Cannot insert duplicate DeptNo.")
        else:
            deptValid = deptService.Get_departments_by_dname(dept.Dname)
            if deptValid:
                print("Already Department with this Dname exists. Cannot insert duplicate Dname.")
            else:
                deptService.Insert_department(dept)
    elif choice == 2:        
        dept_no = int(input("Enter DeptNo to update: "))
        dept_name = input("Enter new Dname (leave blank to skip): ")
        dept_location = input("Enter new Location (leave blank to skip): ")
        dept = Department(dept_no, dept_name, dept_location)
        deptService.Update_department(dept)
    elif choice == 3:
        dept_no = int(input("Enter DeptNo to delete: "))
        deptService.Delete_department(dept_no)
    elif choice == 4:
        deptList = deptService.Get_all_departments()
        for dept in deptList:
            print(dept)
    elif choice == 5:
        dept_no = int(input("Enter DeptNo to fetch: "))
        dept = deptService.Get_department_by_deptNo(dept_no)
        if dept:
            print(dept)
        else:
            print("Department not found.")


    connection.close()

def Employee_CRUD_Operations():
    connection = MySQLConnection().get_connection()
    empRepository = EmpRepositoryImp(connection)
    empService = EmpService(empRepository)

    print("\nEmployee CRUD Operations : ")
    print("1. Insert Employee Record")
    print("2. Update Employee Record")
    print("3. Delete Employee Record")
    print("4. Fetch All Employee Records")
    print("5. Fetch Employee Record by EmpId")
    print("6. Fetch Employee Record by DeptNo")
    print("7. Fetch Employee Record by Gender")
    print("8. Fetch Employee Record by Salary in order (Ascending/Descending)")
    choice = int(input("Enter your choice (1-8): "))
    if choice == 1:        
        EmpId = int(input("Enter EmpId: "))
        Ename = input("Enter Ename: ")
        Password = input("Enter Password: ")
        Gender = input("Enter Gender: ")
        Dob = input("Enter Dob (YYYY-MM-DD): ")
        Phone = input("Enter Phone: ")
        Email = input("Enter Email: ")
        Salary = float(input("Enter Salary: "))
        Address = input("Enter Address: ")
        DeptNo = int(input("Enter DeptNo: "))   
        # Validate EmpId before insertion
        empValidate = empService.get_employee_by_EmpId(EmpId)
        if empValidate:
            print("Already Employee with this EmpId exists. Cannot insert duplicate EmpId.")
        else: 
            emp = Employee(EmpId, Ename, Password, Gender, Dob, Phone, Email, Salary, Address, DeptNo)
            empService.insert_employee(emp)
    elif choice == 2:
        EmpId = int(input("Enter EmpId to update: "))
        Ename = input("Enter new Ename (leave blank to skip): ")
        Password = input("Enter new Password (leave blank to skip): ")
        Gender = input("Enter new Gender (leave blank to skip): ")
        Dob = input("Enter new Dob (YYYY-MM-DD) (leave blank to skip): ")
        Phone = input("Enter new Phone (leave blank to skip): ")
        Email = input("Enter new Email (leave blank to skip): ")
        Salary_input = input("Enter new Salary (leave blank to skip): ")
        Salary = float(Salary_input) if Salary_input else None
        Address = input("Enter new Address (leave blank to skip): ")
        DeptNo_input = input("Enter new DeptNo (leave blank to skip): ")
        DeptNo = int(DeptNo_input) if DeptNo_input else None
        emp = Employee(EmpId, Ename if Ename else None, Password if Password else None, Gender if Gender else None, Dob if Dob else None, Phone if Phone else None, Email if Email else None, Salary if Salary else None, Address if Address else None, DeptNo if DeptNo else None)
        empService.update_employee(emp)
    elif choice == 3:
        EmpId = int(input("Enter EmpId to delete: "))
        empService.delete_employee(EmpId)
    elif choice == 4:
        empList = empService.get_all_employees()
        for emp in empList:
            print(emp)
    elif choice == 5:
        EmpId = int(input("Enter EmpId to fetch: "))
        emp = empService.get_employee_by_empId(EmpId)
        if emp:
            print(emp)
        else:
            print("Employee not found.")

    elif choice == 6:
        DeptNo = int(input("Enter DeptNo to fetch employees: "))
        empList = empService.get_employee_by_deptNo(DeptNo)
        for emp in empList:
            print(emp)  
    elif choice == 7:
        Gender = input("Enter Gender to fetch employees: ")
        empList = empService.get_employee_by_gender(Gender)
        for emp in empList:
            print(emp)  

    elif choice == 8:
        empList = empService.get_employee_ordered_by_salary()
        for emp in empList:
            print(emp)
    connection.close()


print("\n\nStart CRUD Operations Using OOPs : ")
ch = input("Which Table CRUD Operations do you want perform (Department - 'D' / Employee - 'E'): ")
if (ch.upper() == "D"):
    # Perform Department DRUD Operations
    Department_CRUD_Operations()
elif (ch.upper() == "E"):
    #Perform Employee CRUD Operations
    Employee_CRUD_Operations()
else:
    print("Invalid operations...!\nPlease enter proper operation...!")

# match(ch.upper()):
#     case 'D':
#         Perform Department DRUD Operations
#         Department_CRUD_Operations()
#     case 'E':
#         Perform Employee CRUD Operations
#         Employee_CRUD_Operations()
#     case _:
#         print("Invalid operations...!\nPlease enter proper operation...!")

print("End of CRUD Operations...!")
