class RBOrder:
    def __init__(
        self,
        id: int | None = None,
        gas_volume: float | None = None,
        cost: float | None = None,
        status_id: int | None = None,
        customer_id: int | None = None,
    ):
        self.id = id
        self.gas_volume = gas_volume
        self.cost = cost
        self.status_id = status_id
        self.customer_id = customer_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "gas_volume": self.gas_volume,
            "cost": self.cost,
            "status_id": self.status_id,
            "customer_id": self.customer_id,
        }
        return {k: v for k, v in data.items() if v is not None}