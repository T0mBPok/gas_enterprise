class RBWell:
    def __init__(
        self,
        id: int | None = None,
        number: str | None = None,
        created_at: str | None = None,
        depth: float | None = None,
        enterprise_id: int | None = None,
        status_id: int | None = None,
    ):
        self.id = id
        self.number = number
        self.created_at = created_at
        self.depth = depth
        self.enterprise_id = enterprise_id
        self.status_id = status_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "number": self.number,
            "created_at": self.created_at,
            "depth": self.depth,
            "enterprise_id": self.enterprise_id,
            "status_id": self.status_id,
        }
        return {k: v for k, v in data.items() if v is not None}