from uuid import UUID

from pydantic import BaseModel


class Account(BaseModel):
    id: UUID
    login: str
    first_name: str
    last_name: str
    email: str
    role: str
