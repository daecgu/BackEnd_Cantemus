from mongoengine import connect
from ..core.conf import str_cnn, db_name


def get_database():
    connect(db=db_name, host=str_cnn)
