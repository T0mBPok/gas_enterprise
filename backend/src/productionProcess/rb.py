class RBProductionProcess:
    def __init__(
        self,
        id: int | None = None,
        name: str | None = None,
        date_start: str | None = None,
        date_end: str | None = None,
        enterprise_id: int | None = None,
        well_id: int | None = None,
        type_id: int | None = None,
        status_id: int | None = None,
    ):
        self.id = id
        self.name = name
        self.date_start = date_start
        self.date_end = date_end
        self.enterprise_id = enterprise_id
        self.well_id = well_id
        self.type_id = type_id
        self.status_id = status_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "name": self.name,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "enterprise_id": self.enterprise_id,
            "well_id": self.well_id,
            "type_id": self.type_id,
            "status_id": self.status_id,
        }

        return {k: v for k, v in data.items() if v is not None}