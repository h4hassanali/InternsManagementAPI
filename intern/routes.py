from fastapi import APIRouter, HTTPException
from intern.schemas import AddInternRequest, AddInternResponse
from intern.services import (
    add_intern_service,
    get_interns_service,
    delete_intern_service,
    update_intern_service
)
intern_router = APIRouter()


@intern_router.post("/", response_model = AddInternResponse)
async def add_intern(intern_data: AddInternRequest):
    await add_intern_service(intern_data)
    return AddInternResponse(name = intern_data.name, department = intern_data.department)


@intern_router.get("/", response_model = list[AddInternResponse])
async def get_all_interns():
    interns = await get_interns_service()
    return interns


@intern_router.delete("/{intern_id}", status_code = 204)
async def delete_intern(intern_id: str):
    deleted = await delete_intern_service(intern_id)
    if not deleted:
        raise HTTPException(status_code = 404, detail = "Intern not found")
    return


@intern_router.put("/{intern_id}", response_model = AddInternResponse)
async def update_intern(intern_id: str, intern_data: AddInternRequest):
    updated_intern = await update_intern_service(intern_id, intern_data)
    if not updated_intern:
        raise HTTPException(status_code = 404, detail = "Intern not found")
    return updated_intern