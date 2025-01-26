from beanie import Document
from datetime import datetime


class Intern(Document):
    name: str
    age: int
    joining_date: datetime
    department: str
    cnic: str
    address: str

    class Settings:
        collection = "intern"
