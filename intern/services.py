from intern.schemas import Intern
from intern.schemas import AddInternRequest, AddInternResponse
from beanie import PydanticObjectId


async def add_intern_service(intern_data: AddInternRequest):
    intern = Intern(**intern_data.dict())
    await intern.insert()
    return True


async def get_interns_service():
    interns = await Intern.find_all().to_list()
    return [AddInternResponse(name=i.name, department=i.department) for i in interns]


async def delete_intern_service(intern_id: str):
    intern = await Intern.get(PydanticObjectId(intern_id))
    if intern:
        await intern.delete()
        return True
    return False


async def update_intern_service(intern_id: str, intern_data: AddInternRequest):
    intern = await Intern.get(PydanticObjectId(intern_id))
    if intern:
        intern.name = intern_data.name
        intern.department = intern_data.department
        await intern.save()
        return AddInternResponse(name=intern.name, department=intern.department)
    return None
