from pydantic import BaseModel, Field

class ClassifierBase(BaseModel):
    code: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    description: str | None = None


class ClassifierCreate(ClassifierBase):
    pass


class ClassifierUpdate(BaseModel):
    code: str | None = None
    name: str | None = None
    description: str | None = None


class ClassifierRead(ClassifierBase):
    id: int
    
    model_config = {"from_attributes": True}