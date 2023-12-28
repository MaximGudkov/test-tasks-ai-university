from db_setup import session, Employee
from db_client import EmployeeDBClient

client = EmployeeDBClient()

try:
    session.query(Employee).delete()
    session.commit()

    client.create_employee('John Doe', 50000.0)
    client.create_employee('Jane Doe', 60000.0)

    employees = client.read_employees()
    print("Employees:", employees)

    client.update_employee(1, 'John Smith', 55000.0)

    employees = client.read_employees()
    print("Updated Employees:", employees)

    client.delete_employee(2)

    employees = client.read_employees()
    print("Final Employees:", employees)

finally:
    session.close()
