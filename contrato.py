from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr

class Vendas(BaseModel):
    email: EmailStr 
    data: datetime
    valor: float
    quantidade: int
    produto: str 