import os
# Configuración Base de datos:

# Eliminar en un futuro próximo
# user_name = 'test'
# password = '*BfdGT!vX8XqEsd'
# cluster = 'app-web-database'

# MODO CORRECTO DE OBTENER LAS VARIABLES.
str_cnn = os.environ.get('MONGODB_CONNECTION_STRING')
db_name = os.environ.get('MONGODB_DATABASE_NAME')


# Configuración cifrado:
# SCHEME = "argon2"
# MIN_ROUNDS = 15
# MAX_ROUNDS = 25

SCHEME = os.environ.get('SCHEME_CRYPTO')
MIN_ROUNDS = os.environ.get('MIN_ROUNDS_CRYPTO')
MAX_ROUNDS = os.environ.get('MAX_ROUNDS_CRYPTO')

# variables necesarias para trabajar con JWT
TOKEN_VALIDATION_TIME = 14
