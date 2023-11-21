from fastapi import status, HTTPException
from app.models import Contador
import string


def generate_id(counter_value: int) -> str:
    """
    Esta función convierte un entero decimal a base 36 (valores entre 0-9A-Z).
    Genera los id de manera equivalen a la forma en que se generan las columnas
    en execel, es decir números en base 36. Lo único que hay que hacer es pasarle
    el valor en formato decimal que le corresponde.
    :param counter_value: Indica el número que tiene para cambiarlo de base.
    :return: String de número en base 36.
    """
    id_generado = ''
    caracteres = string.digits + string.ascii_uppercase

    while counter_value > 0:
        # Ajustar para el desbordamiento
        modulo = (counter_value - 1) % 36
        id_generado = caracteres[modulo] + id_generado
        counter_value = (counter_value - 1) // 36
    return id_generado


def crear_o_aumentar_contador(nombre_contador: str) -> int:
    contador = Contador.objects(nombre=nombre_contador).first()  # type: ignore
    if not contador:
        contador = Contador(nombre=nombre_contador)
    contador.cuenta += 1
    contador.save()
    return contador.cuenta


def consultar_contador(nombre_contador: str) -> int:
    contador = Contador.objects(nombre=nombre_contador).first()  # type: ignore
    if not contador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Counter not found")
    return contador.cuenta


def resetear_contador(nombre_contador: str) -> int:
    contador = Contador.objects(nombre=nombre_contador).first()  # type: ignore
    if not contador:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Counter not found")
    contador.cuenta = 0
    contador.save()
    return contador.cuenta
