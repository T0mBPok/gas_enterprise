class RBDeposit:
    def __init__(
        self,
        id: int | None = None,
        name: str | None = None,
        region_id: int | None = None,
        status_id: int | None = None,
    ):
        self.id = id
        self.name = name
        self.region_id = region_id
        self.status_id = status_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "name": self.name,
            "region_id": self.region_id,
            "status_id": self.status_id,
        }
        return {k: v for k, v in data.items() if v is not None}
