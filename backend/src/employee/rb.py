class RBEmployee:
    def __init__(
        self,
        id: int | None = None,
        name: str | None = None,
        hire_date: str | None = None,
        position_id: int | None = None,
        qualification_id: int | None = None,
        enterprise_id: int | None = None,
    ):
        self.id = id
        self.name = name
        self.hire_date = hire_date
        self.position_id = position_id
        self.qualification_id = qualification_id
        self.enterprise_id = enterprise_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "name": self.name,
            "hire_date": self.hire_date,
            "position_id": self.position_id,
            "qualification_id": self.qualification_id,
            "enterprise_id": self.enterprise_id,
        }

        return {k: v for k, v in data.items() if v is not None}