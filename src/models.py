from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Categories(SQLModel, table=True):
    __tablename__ = "categories"  # type: ignore

    name: str = Field(..., primary_key=True)
    repr_name: str


class Transaction(SQLModel, table=True):
    __tablename__ = "transaction"  # type: ignore

    id: Optional[int] = Field(default=None, primary_key=True)
    amount: int = Field(..., gt=0)
    category: Categories = Relationship(back_populates="categories")
    username: str
    comment: Optional[str]
    transaction_type: TransactionType
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
