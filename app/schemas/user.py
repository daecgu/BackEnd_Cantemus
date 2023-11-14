from pydantic import BaseModel, EmailStr, Field, model_validator


class UserCreate(BaseModel):
    username: str = Field(min_length=6, max_length=80)
    email: EmailStr = Field(max_length=320)
    password: str = Field(min_length=8, max_length=128)
    password_confirmation: str = Field(alias='passwordConfirmation')

    @model_validator(mode='before')
    @classmethod
    def passwords_match(cls, values):
        password = values.get('password')
        password_confirmation = values.get('passwordConfirmation')
        if password != password_confirmation:
            raise ValueError('Las contraseñas no coinciden')
        return values

    class Config:
        json_schema_extra = {
            "example": {
                "username": "usuario_ejemplo",
                "email": "ejemplo@correo.com",
                "password": "contraseña123",
                "passwordConfirmation": "contraseña123",
            }
        }


class UserDisplay(BaseModel):
    username: str = Field(min_length=6, max_length=80)
    email: EmailStr = Field(max_length=320)

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    actualpassword: str = Field(min_length=8, max_length=128)
    username: str = Field(min_length=6, max_length=80, default=None)
    email: EmailStr = Field(max_length=320, default=None)
    hashed_password: str = Field(min_length=8, max_length=128, default=None)
    newpasswordconfirmation: str = Field(default=None)

    @model_validator(mode='before')
    @classmethod
    def new_passwords_match(cls, values):
        hashed_password = values.get('hashed_password')
        newpasswordconfirmation = values.get('newpasswordconfirmation')
        if hashed_password and hashed_password != newpasswordconfirmation:
            raise ValueError('Las nuevas contraseñas no coinciden')
        return values

    class Config:
        json_schema_extra = {
            "example": {
                "actualpassword": "contraseña123",
                "username": "usuario_ejemplo_update",
                "email": "ejemplo_nuevo@correo.com",
                "hashed_password": "123contraseña",
                "newpasswordconfirmation": "123contraseña",
            }
        }
