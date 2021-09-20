from pydantic import BaseModel


class User(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str


class ShowUser(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: str

    class Config():
        orm_mode = True


class Challenge(BaseModel):
    title: str
    description: str
    author_user_id: int


class ShowChallenge(Challenge):
    author: ShowUser

    class Config():
        orm_mode = True
