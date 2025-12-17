class RBEnterprise:
    def __init__(
        self,
        id: int | None = None,
        name: str | None = None,
        contacts: str | None = None,
        status_id: int | None = None,
        type_id: int | None = None,
        deposit_id: int | None = None,
        country_id: int | None = None,
        city_id: int | None = None,
        street_id: int | None = None,
        house_id: int | None = None,
    ):
        self.id = id
        self.name = name
        self.contacts = contacts
        self.status_id = status_id
        self.type_id = type_id
        self.deposit_id = deposit_id
        self.country_id = country_id
        self.city_id = city_id
        self.street_id = street_id
        self.house_id = house_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "name": self.name,
            "contacts": self.contacts,
            "status_id": self.status_id,
            "type_id": self.type_id,
            "deposit_id": self.deposit_id,
            "country_id": self.country_id,
            "city_id": self.city_id,
            "street_id": self.street_id,
            "house_id": self.house_id,
        }
        return {k: v for k, v in data.items() if v is not None}