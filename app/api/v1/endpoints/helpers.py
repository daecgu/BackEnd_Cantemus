from app.models import Contador
from fastapi import status, HTTPException


def crear_o_actualizar_contador(nombre_contador: str) -> int:
    contador = Contador.objects(nombre=nombre_contador).first()  # type: ignore
    if not contador:
        contador = Contador(nombre=nombre_contador)
    contador.cuenta += 1
    contador.save()
    return contador.cuenta

def consultar_contador(nombre_contador:str) -> int:
    contador = Contador.objects(nombre=nombre_contador).first()  # type: ignore
    if not contador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Counter not found")
    return contador.cuenta
