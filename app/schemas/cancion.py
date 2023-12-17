from pydantic import BaseModel


class CancionSchema(BaseModel):
    id_cancion: str
    titulo: str
    artista: str
    idioma: str
    letra: str
    tematica: list[str]


class CancionDiapositivasSchema(CancionSchema):
    diapositivas: list[str]


class DiapositivasSchema(BaseModel):
    id_cancion: str
    diapositivas: list[str]
    titulo: str
    artista: str
