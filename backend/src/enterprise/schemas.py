from pydantic import BaseModel, Field
from src.classifiers.schemas import ClassifierRead
from src.deposit.schemas import GetDeposit


class GetEnterprise(BaseModel):
    id: int
    name: str
    contacts: str | None
    status: ClassifierRead
    type: ClassifierRead
    deposit: GetDeposit
    country: ClassifierRead
    city: ClassifierRead
    street: ClassifierRead
    house: ClassifierRead


class AddEnterprise(BaseModel):
    name: str = Field(..., min_length=2)
    contacts: str | None = None
    status_id: int
    type_id: int
    deposit_id: int
    country_id: int
    city_id: int
    street_id: int
    house_id: int

    @classmethod
    def as_form(
        cls,
        name: str = Field(...),
        contacts: str | None = None,
        status_id: int = Field(...),
        type_id: int = Field(...),
        deposit_id: int = Field(...),
        country_id: int = Field(...),
        city_id: int = Field(...),
        street_id: int = Field(...),
        house_id: int = Field(...),
    ):
        return cls(
            name=name,
            contacts=contacts,
            status_id=status_id,
            type_id=type_id,
            deposit_id=deposit_id,
            country_id=country_id,
            city_id=city_id,
            street_id=street_id,
            house_id=house_id,
        )


class UpdateEnterprise(BaseModel):
    name: str | None = Field(None, min_length=2)
    contacts: str | None = None
    status_id: int | None = None
    type_id: int | None = None
    deposit_id: int | None = None
    country_id: int | None = None
    city_id: int | None = None
    street_id: int | None = None
    house_id: int | None = None