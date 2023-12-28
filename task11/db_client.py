from sqlalchemy.exc import SQLAlchemyError

from db_setup import session, Employee


class EmployeeDBClient:
    @staticmethod
    def rollback_on_error(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except SQLAlchemyError as e:
                session.rollback()
                raise e

        return wrapper

    @rollback_on_error
    def create_employee(self, name, salary):
        new_employee = Employee(name=name, salary=salary)
        session.add(new_employee)
        session.commit()

    def read_employees(self):
        employees = session.query(Employee).all()
        return employees

    @rollback_on_error
    def update_employee(self, employee_id, new_name, new_salary):
        employee = session.query(Employee).get(employee_id)
        if employee:
            employee.name = new_name
            employee.salary = new_salary
            session.commit()
        else:
            raise ValueError(f"Employee with id {employee_id} not found")

    @rollback_on_error
    def delete_employee(self, employee_id):
        employee = session.query(Employee).get(employee_id)
        if employee:
            session.delete(employee)
            session.commit()
        else:
            raise ValueError(f"Employee with id {employee_id} not found")
