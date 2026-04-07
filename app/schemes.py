from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserBase(BaseModel):
    name: Annotated[str, Field(min_length=2)]
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]

class UserLogin(BaseModel):
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]

class User(UserBase):
    id: int
    avatar: Optional[bytes] = None

    model_config = ConfigDict(from_attributes=True)

class Anime(BaseModel):
    id: int
    name: Annotated[str, Field(min_length=2)]
    timeStop: Annotated[int, Field(alias="time_stop")]
    numbersEpisode : Annotated[int, Field(alias="number_episode")]

    model_config = ConfigDict(from_attributes=True)
