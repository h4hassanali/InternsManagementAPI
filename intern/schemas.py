from datetime import datetime
from pydantic import BaseModel


class AddInternRequest(BaseModel):
    name: str
    age: int
    joining_date: datetime
    department: str
    cnic: str
    address: str


class AddInternResponse(BaseModel):
    name: str
    department: str
