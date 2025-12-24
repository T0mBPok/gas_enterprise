from datetime import date
from pydantic import BaseModel
from src.enterprise.schemas import GetEnterprise
from src.classifiers.schemas import ClassifierRead


class GetEmployee(BaseModel):
    id: int
    name: str
    hire_date: date | None
    position: ClassifierRead
    qualification: ClassifierRead
    enterprise: GetEnterprise


class AddEmployee(BaseModel):
    name: str
    hire_date: date | None
    position_id: int
    qualification_id: int
    enterprise_id: int


class UpdateEmployee(BaseModel):
    name: str | None = None
    hire_date: date | None = None
    position_id: int | None = None
    qualification_id: int | None = None
    enterprise_id: int | None = None