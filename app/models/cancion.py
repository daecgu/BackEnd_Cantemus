from mongoengine import Document, StringField, ListField


class Cancion(Document):
    id_cancion = StringField(required=True, unique=True)
    titulo = StringField(required=True)
    artista = StringField(required=True)
    idioma = StringField(required=True)
    letra = StringField(required=True)
    tematica = StringField(required=False)
    diapositivas = ListField(StringField(), default=list)
