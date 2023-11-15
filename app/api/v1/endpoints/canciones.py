from fastapi import APIRouter, status, HTTPException
from app.models.cancion import Cancion
from app.utils import ProcesadorCanciones
from app.schemas.cancion import CancionSchema, DiapositivasSchema
import random
import string

router = APIRouter(tags=["Gestión Canciones"])


def generate_id(lenght: int = 3) -> str:
    dictionary: str = string.ascii_uppercase + string.digits
    while True:
        new_id = ''
        for _ in range(lenght):
            new_id = new_id + (random.choice(dictionary))
        if not Cancion.objects(id_cancion=new_id).first(): # type: ignore
            return new_id


@router.post("/canciones/", status_code=status.HTTP_201_CREATED)
async def create_songs():
    p = ProcesadorCanciones("/home/decheverri/PycharmProjects/BackEnd-cantemus/Canciones/",
                            "mi_corazon_quiere_alabar.txt")
    cancion = p.obtener_objeto_bbdd_cancion()
    cancion.id_cancion = generate_id()
    cancion.save()
    return {"message": "Cancion Creada", "id_cancion": cancion.id_cancion}


@router.get("/canciones/", response_model=list[CancionSchema], status_code=status.HTTP_200_OK)
async def list_songs():
    """
    Devuelve la lista de todas las canciones sin las diapositivas.
    """
    canciones = Cancion.objects.all()  # Recuperar todas las canciones de la base de datos
    return [CancionSchema(**cancion.to_mongo().to_dict()) for cancion in canciones if cancion]


@router.get("/canciones/{id_cancion}/diapositivas", response_model=DiapositivasSchema)
async def get_song_diapositivas(id_cancion: str):
    cancion = Cancion.objects(id_cancion=id_cancion).first() # type: ignore
    if not cancion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Canción no encontrada")

    return DiapositivasSchema(
        id_cancion=cancion.id_cancion,
        diapositivas=cancion.diapositivas,
        titulo=cancion.titulo,
        artista=cancion.artista
    )