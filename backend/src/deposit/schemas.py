from pydantic import BaseModel, Field
from src.classifiers.schemas import ClassifierRead


class GetDeposit(BaseModel):
    id: int
    name: str
    region: ClassifierRead
    status: ClassifierRead


class AddDeposit(BaseModel):
    name: str = Field(..., min_length=2)
    region_id: int
    status_id: int

    @classmethod
    def as_form(
        cls,
        name: str = Field(...),
        region_id: int = Field(...),
        status_id: int = Field(...),
    ):
        return cls(
            name=name,
            region_id=region_id,
            status_id=status_id
        )


class UpdateDeposit(BaseModel):
    name: str | None = Field(None, min_length=2)
    region_id: int | None = None
    status_id: int | None = None
