from db.MySQLConnection import MySqlConnection
from Repositories.Dept_Repository_Imp import Dept_Repository_Imp
from Services.Department_Service import Department
from Models.Department import Department

def Department_CRUD_Operations():
    connection = MySqlConnection().get_connection()
    deptRepository = Dept_Repository_Imp(connection)
    deptService = Department_Service(deptRepository)

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
        deptValid = deptService.Get_department_by_deptNo(dept.deptNo)      
        if deptValid:
            print("Already Department with this DeptNo exists. Cannot insert duplicate DeptNo.")
        else:
            deptValid = deptService.Get_departments_by_dname(dept.dname)
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
    pass

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