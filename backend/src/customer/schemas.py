from pydantic import BaseModel, Field
from src.classifiers.schemas import ClassifierRead


class GetCustomer(BaseModel):
    id: int
    name: str
    phone_num: str
    contact_info: str
    created_at: str
    country: ClassifierRead
    city: ClassifierRead
    street: ClassifierRead
    house: ClassifierRead


class AddCustomer(BaseModel):
    name: str = Field(..., min_length=2)
    phone_num: str = Field(..., min_length=5)
    contact_info: str | None = Field(None, min_length=2)
    country_id: int
    city_id: int
    street_id: int
    house_id: int

    @classmethod
    def as_form(
        cls,
        name: str = Field(...),
        phone_num: str = Field(...),
        contact_info: str | None = Field(None),
        country_id: int = Field(...),
        city_id: int = Field(...),
        street_id: int = Field(...),
        house_id: int = Field(...),
    ):
        return cls(
            name=name,
            phone_num=phone_num,
            contact_info=contact_info,
            country_id=country_id,
            city_id=city_id,
            street_id=street_id,
            house_id=house_id,
        )


class UpdateCustomer(BaseModel):
    name: str | None = Field(None, min_length=2)
    phone_num: str | None = None
    contact_info: str | None = None
    country_id: int | None = None
    city_id: int | None = None
    street_id: int | None = None
    house_id: int | None = None