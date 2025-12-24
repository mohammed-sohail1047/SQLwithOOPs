from Repositories.Emp_Repository import Emp_Repository  

class Emp_Repository_Imp(Emp_Repository):
    def __init__(self, connection):
        self.connection = connection
    def insert_employee(self, Employee):
        # Implementation for inserting an employee
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO Employee (EmpID, Ename, Password, Gender, DOB, Phone, Email, Salary, Address, DeptNo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(insert_query, (Employee.empID, Employee.ename, Employee.password, Employee.gender, Employee.dob, Employee.phone, Employee.email, Employee.salary, Employee.address, Employee.deptNo))
            self.connection.commit() # Commit the transaction to save changes        
            print("Employee record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")
    def update_employee(self, Employee):
        # Implementation for updating an employee
        cursor = self.connection.cursor()

        update_fields = []
        params = []

        if Employee.ename:
            update_fields.append("Ename = %s")
            params.append(Employee.ename)

        if Employee.password:
            update_fields.append("Password = %s")   
            params.append(Employee.password)

        if Employee.gender:
            update_fields.append("Gender = %s")
            params.append(Employee.gender)
        if Employee.dob:
            update_fields.append("DOB = %s")
            params.append(Employee.dob) 
        if Employee.phone:
            update_fields.append("Phone = %s")
            params.append(Employee.phone)
        if Employee.email:
            update_fields.append("Email = %s")
            params.append(Employee.email)
        if Employee.salary:
            update_fields.append("Salary = %s")
            params.append(Employee.salary)
        if Employee.address:
            update_fields.append("Address = %s")
            params.append(Employee.address)
        if Employee.deptNo:
            update_fields.append("DeptNo = %s")
            params.append(Employee.deptNo)
        if not update_fields:
            print("Nothing to update.")
            return
        params.append(Employee.empID)
        update_query = f"UPDATE Employee SET {', '.join(update_fields)} WHERE EmpID = %s"
        try:
            cursor.execute(update_query, tuple(params))
            self.connection.commit()
            print("Employee record updated successfully.")
        except Exception as e:
            print(f"Error updating employee record: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")
    def delete_employee(self, EmpID):
        # Implementation for deleting an employee
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM Employee WHERE EmpID = %s"
        try:
            cursor.execute(delete_query, (EmpID,))
            self.connection.commit() # Commit the transaction to save changes        
            print("Employee record deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")
    def get_all_employees(self):
        # Implementation for retrieving all employees
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employee"
        try:
            cursor.execute(select_query)
            employees = cursor.fetchall()
            return employees
        except Exception as e:
            print(f"Error retrieving records: {e}")
            return []
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")
    def get_employee_by_EmpId(self, EmpID):
        # Implementation for retrieving an employee by EmpID
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employee WHERE EmpID = %s"
        try:
            cursor.execute(select_query, (EmpID,))
            employees = cursor.fetchall()
            return employees
        except Exception as e:
            print(f"Error retrieving records: {e}")
            return []
        finally:
            cursor.close()
            self.connection.close()
    print("----------------------------------------------------------------------------------------------------------\n")   
    def get_employee_by_Ename(self, Ename):
        # Implementation for retrieving an employee by Ename
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Employee WHERE Ename = %s"
        try:
            cursor.execute(select_query, (Ename,))
            employees = cursor.fetchall()
            return employees
        except Exception as e:
            print(f"Error retrieving records: {e}")
            return []
        finally:
            cursor.close()
            self.connection.close()
    print("----------------------------------------------------------------------------------------------------------\n")
    