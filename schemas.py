from pydantic import BaseModel


class Challenge(BaseModel):
    title = str
    body = str
