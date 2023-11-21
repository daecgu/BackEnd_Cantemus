from app.models import Contador


def crear_o_actualizar_contador(nombre_contador: str) -> int:
    contador = Contador.objects(nombre=nombre_contador).first()  # type: ignore
    if not contador:
        contador = Contador(nombre=nombre_contador)
    contador.cuenta += 1
    contador.save()
    return contador.cuenta
