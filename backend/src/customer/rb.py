class RBCustomer:
    def __init__(
        self,
        id: int | None = None,
        name: str | None = None,
        phone_num: str | None = None,
        contact_info: str | None = None,
        country_id: int | None = None,
        city_id: int | None = None,
        street_id: int | None = None,
        house_id: int | None = None,
    ):
        self.id = id
        self.name = name
        self.phone_num = phone_num
        self.contact_info = contact_info
        self.country_id = country_id
        self.city_id = city_id
        self.street_id = street_id
        self.house_id = house_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "name": self.name,
            "phone_num": self.phone_num,
            "contact_info": self.contact_info,
            "country_id": self.country_id,
            "city_id": self.city_id,
            "street_id": self.street_id,
            "house_id": self.house_id,
        }
        return {k: v for k, v in data.items() if v is not None}
