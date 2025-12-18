class RBProdMetrics:
    def __init__(
        self,
        id: int | None = None,
        gas_volume: float | None = None,
        pressure: float | None = None,
        temperature: float | None = None,
        well_id: int | None = None,
    ):
        self.id = id
        self.gas_volume = gas_volume
        self.pressure = pressure
        self.temperature = temperature
        self.well_id = well_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "gas_volume": self.gas_volume,
            "pressure": self.pressure,
            "temperature": self.temperature,
            "well_id": self.well_id,
        }
        return {k: v for k, v in data.items() if v is not None}