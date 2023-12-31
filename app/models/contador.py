# Necesario para Id único ordenado en MongoDB

from mongoengine import Document, StringField, IntField


class Contador(Document):
    nombre = StringField(required=True, unique=True)
    cuenta = IntField(default=0)
