from uuid import UUID
from pydantic import BaseModel, ConfigDict

class Employee(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    Card: str
    CallName: str
