from pydantic import BaseModel


class LoginSchema(BaseModel):

    username: str

    password: str


class TokenResponseSchema(BaseModel):

    access_token: str

    token_type: str
