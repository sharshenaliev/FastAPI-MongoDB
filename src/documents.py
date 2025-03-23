from beanie import Document
from datetime import datetime


class Test(Document):
    title: str
    content: str
    date: datetime | None = None
    author: str | None = None
    array: dict | None = None


    class Settings:
        name = "test"
