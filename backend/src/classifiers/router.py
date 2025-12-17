from fastapi import APIRouter, HTTPException, Path
from .schemas import (
    ClassifierCreate,
    ClassifierRead,
    ClassifierUpdate
)
from .logic import ClassifierLogic

from .models import *

router = APIRouter(prefix="/classifiers", tags=["Классификаторы"])

MODEL_MAP = {
    "regions": Region,
    "enterprise-statuses": EnterpriseStatus,
    "enterprise-types": EnterpriseType,
    "deposit-statuses": DepositStatus,
    "well-statuses": WellStatus,
    "process-types": ProcessType,
    "process-statuses": ProcessStatus,
    "transports": Transport,
    "delivery-statuses": DeliveryStatus,
    "order-statuses": OrderStatus,
    "positions": Position,
    "qualifications": Qualification,
    "countries": Country,
    "cities": City,
    "streets": Street,
    "houses": House,
}

@router.post("/{classifier}", summary="Добавить запись в классификатор", response_model=ClassifierRead)
async def create_classifier_item(classifier: str, data: ClassifierCreate):
    model = MODEL_MAP[classifier]
    if not model:
        raise HTTPException(status_code=404, detail="Классификатор не найден")
    ClassifierLogic.model = model
    return await ClassifierLogic.create(**data.model_dump())

@router.get("", summary="Получить список доступных классификаторов")
async def get_classifiers():
    return [
        {
            "title": key,
            "model": value.__name__
        }
        for key, value in MODEL_MAP.items()
    ]

@router.get("/{classifier}", response_model=list[ClassifierRead])
async def get_all(classifier: str):
    model = MODEL_MAP[classifier]
    if not model:
        raise HTTPException(status_code=404, detail="Классификатор не найден")
    ClassifierLogic.model = model
    return await ClassifierLogic.get()

@router.get("/{classifier}/{id}", response_model=ClassifierRead)
async def get_one(classifier: str, id: int = Path(..., gt=0)):
    ClassifierLogic.model = MODEL_MAP[classifier]
    return await ClassifierLogic.get_one_or_none_by_id(id=id)

@router.put("/{classifier}/{id}", response_model=ClassifierUpdate)
async def update(classifier: str, id: int = Path(..., gt=0), data: ClassifierUpdate = ...):
    ClassifierLogic.model = MODEL_MAP[classifier]
    values = data.model_dump(exclude_unset=True)
    await ClassifierLogic.update_classifier(id=id, **values)
    return values