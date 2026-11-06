from pydantic import BaseModel


class Category(BaseModel):
    id: int = 1
    name: str = "cats"


class Tag(BaseModel):
    id: int
    name: str


class Pet(BaseModel):
    id: int
    category: Category = Category()
    name: str
    photoUrls: list[str] = []
    tags: list[Tag] = []
    status: str = "available"


class Order(BaseModel):
    id: int
    petId: int
    quantity: int = 1
    shipDate: str | None = None
    status: str = "placed"
    complete: bool = False


class ApiResponse(BaseModel):
    code: int
    type: str
    message: str
