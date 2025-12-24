from Repositories.Dept_Repository import Dept_Repository

class Dept_Repository_Imp(Dept_Repository):
    def __init__(self, connection):
        self.connection = connection 
    def insert_department(self, Department):
        # Implementation for inserting a department
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO Department (DeptNo, Dname, Location) VALUES (%s, %s, %s)"
        try:
            cursor.execute(insert_query, (Department.deptNo, Department.dname, Department.location))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record inserted successfully.")
        except Exception as e:
            print(f"Error inserting record: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")
    def update_department(self, Department):
        # Implementation for updating a department
        cursor = self.connection.cursor()

        update_fields = []
        params = []

        if Department.dname:
            update_fields.append("Dname = %s")
            params.append(Department.dname)

        if Department.location:
            update_fields.append("Location = %s")   
            params.append(Department.location)

        if not update_fields:
            print("Nothing to update.")
            return

        params.append(Department.deptNo)

        update_query = f"UPDATE dept SET {', '.join(update_fields)} WHERE deptno = %s"

        try:
            cursor.execute(update_query, tuple(params))
            self.connection.commit()
            print("Department record updated successfully.")
        except Exception as e:
            print(f"Error updating department record: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")

    def delete_department(self, Dept_no):
        # Implementation for deleting a department
        cursor = self.connection.cursor()
        delete_query = "DELETE FROM Department WHERE DeptNo = %s"
        try:
            cursor.execute(delete_query, (Dept_no,))
            self.connection.commit() # Commit the transaction to save changes        
            print("Department record deleted successfully.")
        except Exception as e:
            print(f"Error deleting record: {e}")
        finally:
            cursor.close()
            self.connection.close()
    print("----------------------------------------------------------------------------------------------------------\n")

    def get_all_departments(self):
        # Implementation for retrieving all departments
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Department"
        try:
            cursor.execute(select_query)
            departments = cursor.fetchall()
            for dept in departments:
                print(f"DeptNo: {dept[0]}, Dname: {dept[1]}, Location: {dept[2]}")
        except Exception as e:
            print(f"Error retrieving records: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")
    def get_department_by_DeptNo(self, dept_no):
        # Implementation for retrieving a department by DeptNo
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Department WHERE DeptNo = %s"
        try:
            cursor.execute(select_query, (dept_no,))
            departments = cursor.fetchall()
            for dept in departments:
                print(f"DeptNo: {dept[0]}, Dname: {dept[1]}, Location: {dept[2]}")
        except Exception as e:
            print(f"Error retrieving records: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")

    def get_department_by_Dname(self, dname):
        # Implementation for retrieving a department by Dname
        cursor = self.connection.cursor()
        select_query = "SELECT * FROM Department WHERE Dname = %s"
        try:
            cursor.execute(select_query, (dname,))
            departments = cursor.fetchall()
            for dept in departments:
                print(f"DeptNo: {dept[0]}, Dname: {dept[1]}, Location: {dept[2]}")
        except Exception as e:
            print(f"Error retrieving records: {e}")
        finally:
            cursor.close()
            self.connection.close()
        print("----------------------------------------------------------------------------------------------------------\n")