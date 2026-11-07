from pydantic import BaseModel, Field, RootModel

from fakers import random_number, random_string


class Category(BaseModel):
    id: int = Field(default_factory=random_number)
    name: str = "cats"


class Tag(BaseModel):
    id: int = Field(default_factory=random_number)
    name: str = Field(default_factory=random_string)


class Pet(BaseModel):
    id: int = Field(default_factory=random_number)
    category: Category = Field(default_factory=Category)
    name: str = "Муртузик"
    photo_urls: list[str] = Field(alias="photoUrls", default_factory=list)
    tags: list[Tag] = Field(default_factory=list)
    status: str = "available"


class Order(BaseModel):
    id: int = Field(default_factory=random_number)
    pet_id: int = Field(alias="petId", default_factory=random_number)
    quantity: int = Field(default_factory=lambda: random_number(1, 10))
    status: str = "placed"
    complete: bool = False


class Inventory(RootModel):
    root: dict[str, int]


class ApiResponse(BaseModel):
    code: int
    type: str
    message: str
