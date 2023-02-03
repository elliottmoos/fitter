import re
from typing import Optional
from pydantic import EmailStr, validator
from sqlmodel import Field, SQLModel

from .base import IDModelMixin


class CustomerBase(SQLModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address_id: Optional[int] = Field(default=None, foreign_key="address.id")

    @validator("phone")
    def validate_phone_number(cls, v):
        patterns = (r"\(\w{3}\) \w{3}\-\w{4}", r"^\w{3}\-\w{4}$")
        if not [re.search(pattern, v) for pattern in patterns]:
            raise ValueError("Invalid phone number format.")
        return v


class Customer(CustomerBase, IDModelMixin, table=True):
    pass


class CustomerRead(CustomerBase):
    id: int


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(SQLModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address_id: Optional[int]
