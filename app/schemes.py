from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class User(BaseModel):
    id: int
    name: Annotated[str, Field(min_length=2)]
    email: EmailStr
    avatar: Optional[bytes] = None
    password: Annotated[str, Field(min_length=8)]

    model_config = ConfigDict(from_attributes=True)

class Anime(BaseModel):
    id: int
    name: Annotated[str, Field(min_length=2)]
    timeStop: Annotated[int, Field(alias="time_stop")]
    numbersEpisode : Annotated[int, Field(alias="number_episode")]

    model_config = ConfigDict(from_attributes=True)
