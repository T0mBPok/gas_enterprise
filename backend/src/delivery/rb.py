from datetime import date

class RBDelivery:
    def __init__(
        self,
        id: int | None = None,
        delivery_date: date | None = None,
        volume: float | None = None,
        order_id: int | None = None,
        transport_id: int | None = None,
        status_id: int | None = None,
        enterprise_id: int | None = None,
    ):
        self.id = id
        self.delivery_date = delivery_date
        self.volume = volume
        self.order_id = order_id
        self.transport_id = transport_id
        self.status_id = status_id
        self.enterprise_id = enterprise_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "delivery_date": self.delivery_date,
            "volume": self.volume,
            "order_id": self.order_id,
            "transport_id": self.transport_id,
            "status_id": self.status_id,
            "enterprise_id": self.enterprise_id,
        }
        return {k: v for k, v in data.items() if v is not None}