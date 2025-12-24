from src.dao.base import BaseDAO
from src.employee.models import Employee
from src.enterprise.dao import EnterpriseDAO
from src.classifiers.dao import ClassifierDAO


class EmployeeDAO(BaseDAO):
    model = Employee

    @classmethod
    async def get_one_with_relations(cls, id: int):
        emp = await cls.get_one_by_id(id, "position", "qualification",)
        
        if emp.enterprise_id:
            emp.enterprise = await EnterpriseDAO.get_one_with_deposit(emp.enterprise_id)

        return emp

    @classmethod
    async def get_all_with_relations(cls, **filter_by):
        employees = await cls.get_all("position", "qualification", **filter_by)

        for emp in employees:
            if emp.enterprise_id:
                emp.enterprise = await EnterpriseDAO.get_one_with_deposit(emp.enterprise_id)

        return employees