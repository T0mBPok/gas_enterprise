from pydantic import BaseModel
from typing import List


class LayerParams(BaseModel):
    top_depth: float
    thickness: float
    amplitude: float
    frequency_x: float
    frequency_y: float
    layer_type: str
    color: str
    opacity: float


class DomainParams(BaseModel):
    x_min: float = 0
    x_max: float = 1000
    y_min: float = 0
    y_max: float = 1000
    nx: int = 200
    ny: int = 200


class ModelParams(BaseModel):
    domain: DomainParams
    layers: List[LayerParams]
    

class GetModel3D(BaseModel):
    id: int
    file_path: str
    format: str
    well_id: int

# Пример дефолтных данных
default_model_params = ModelParams(
    domain=DomainParams(),
    layers=[
        LayerParams(
            top_depth=-50,
            thickness=30,
            amplitude=10,
            frequency_x=150,
            frequency_y=200,
            layer_type="gas",
            color="orange",
            opacity=0.7
        ),
        LayerParams(
            top_depth=-100,
            thickness=40,
            amplitude=8,
            frequency_x=180,
            frequency_y=170,
            layer_type="water",
            color="blue",
            opacity=0.6
        )
    ]
)