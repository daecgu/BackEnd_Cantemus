""" Este va a ser mi procesador de letras.
### Las canciones deben enviarse en formato .txt ejemplo del formato:
@@Título: Título de la Canción
@@Artista: Desconocido o Nombre Artista
@@Idioma: Idioma de la canción.
@@Temática: Eucarística / Liturgia  / Salmos / María / Jesús / Santos / Alabanza / Sanación / Petición / Penitencial / Adviento / Cuaresma / Navidad / Tiempo Ordinario / Pascua / Oración / Reino
----
Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
Curabitur in est ultrices,
tempus leo sit amet,
malesuada massa.

Etiam vitae convallis nulla,
eget sollicitudin magna.
Proin quis tellus eu libero
pretium efficitur vitae ut lorem.

Nam quis condimentum arcu,
sed facilisis nisi.
Duis dictum eros nunc,
eu sodales augue gravida at.
Nunc rutrum ligula et pretium vestibulum.

Donec pulvinar,
nisi id molestie malesuada,
purus purus semper elit,
a venenatis enim sem sed tellus.
"""
import re
from app.models import Cancion


class ProcesadorCanciones:
    """
    Este procesador se encarga de procesar las canciones.
    Primero obtiene el título, el autor y la letra completa.
    Luego separa en Diapositivas cada estrofa/estribillo de la canción.
    """
    def __init__(self, ruta_archivo: str, nombre_archivo: str) -> None:
        """
        Constructor # aquí me tocará definir cosas que vaya a necesitar.
        """
        self.ruta_completa = str(ruta_archivo + "/" + nombre_archivo)
        self.titulo: str = ""
        self.artista: str = ""
        self.idioma: str = ""
        self.letra: str = ""
        self.tematica: list = []
        self.diapositivas: list = []
        self.cargar_cancion()

    def cargar_cancion(self) -> None:
        archivo = open(self.ruta_completa, "r")
        texto = archivo.read()
        archivo.close()
        try:
            self.titulo = re.search(r"^@@Título:\s*(.*)", texto, re.MULTILINE).group(1)  # type: ignore
            if self.titulo is None:
                self.titulo = "Desconocido/Unknown"
        except AttributeError:
            self.titulo = "Desconocido/Unknown"
        try:
            self.artista = re.search(r"^@@Artista:\s*(.*)", texto, re.MULTILINE).group(1)  # type: ignore
        except AttributeError:
            self.artista = "Desconocido/Unknown"
        try:
            self.idioma = re.search(r"^@@Idioma:\s*(.*)", texto, re.MULTILINE).group(1)  # type: ignore
        except AttributeError:
            self.idioma = "Desconocido/Unknown"
        try:
            tematicas_str = re.search(r"^@@Temática:\s*(.*)", texto, re.MULTILINE).group(1)  # type: ignore
            self.tematica = [tematica.strip() for tematica in tematicas_str.split('/') if tematica.strip()]
        except AttributeError:
            self.tematica = []
        self.letra = texto.split("----\n")[1]
        self.diapositivas = self.letra.split('\n\n')

    def obtener_objeto_bbdd_cancion(self):
        return Cancion(
            titulo=self.titulo,
            artista=self.artista,
            idioma=self.idioma,
            letra=self.letra,
            tematica=self.tematica,
            diapositivas=self.diapositivas
        )

# p = ProcesadorCanciones("/home/decheverri/PycharmProjects/BackEnd-cantemus/Canciones/", "la_bendicion.txt")
# print(f'Este es el título: {p.titulo}.\nEste es el artista: {p.artista}.\nEste es el idioma: {p.idioma}.')
# print("\n--------")
# i = 0
# for each in p.diapositivas:
#     i += 1
#     print(f'Esta es la diapositiva número {i}:\n--------\n{each}\n--------')
