from fastapi import APIRouter, HTTPException, Body, status
from app.models.user import Users as UserModel
from app.schemas.user import UserCreate, UserDisplay, UserUpdate
from app.core.conf import SCHEME, MIN_ROUNDS, MAX_ROUNDS
from passlib.context import CryptContext


crypt = CryptContext(schemes=[SCHEME],
                     argon2__min_rounds=MIN_ROUNDS,
                     argon2__max_rounds=MAX_ROUNDS,
                     deprecated="auto")

router = APIRouter(tags=["Gestión Usuarios"])


@router.post("/users/", response_model=UserDisplay, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate = Body(...)):
    if UserModel.objects(username=user.username).first(): # type: ignore
        raise HTTPException(
            status_code=400,
            detail=f"El usuario con el nombre {user.username} ya existe."
        )
    hashed_password = crypt.hash(user.password)
    user_obj = UserModel(username=user.username, email=user.email, hashed_password=hashed_password)
    user_obj.save()
    return user_obj


@router.get("/users/{user_id}", response_model=UserDisplay)
async def read_user(user_id: str):
    # Busca el usuario por ID
    user_obj = UserModel.objects(id=user_id).first() # type: ignore
    if user_obj is None:
        # Si no se encuentra el usuario, lanza una excepción
        raise HTTPException(status_code=404, detail="User not found")

    # Convierte el objeto de usuario MongoEngine a un diccionario
    user_dict = user_obj.to_mongo().to_dict()
    # Retira los campos que no quieres exponer, como la contraseña
    user_dict.pop('password', None)

    # Devuelve el usuario en el formato del esquema Pydantic UserDisplay
    return UserDisplay(**user_dict)


@router.put("/users/{user_id}", response_model=UserDisplay)
async def update_user(user_id: str, user_update: UserUpdate = Body(...)):
    # Busca el usuario por ID
    user_obj = UserModel.objects(id=user_id).first() # type: ignore
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Verifica la contraseña actual
    if not crypt.verify(user_update.actualpassword, user_obj.hashed_password):
        raise HTTPException(status_code=400, detail="Contraseña actual incorrecta")

    # Comprobación de usuario y email únicos
    if user_update.username and UserModel.objects(username=user_update.username, id__ne=user_id).first(): # type: ignore
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está en uso")
    if user_update.email and UserModel.objects(email=user_update.email, id__ne=user_id).first(): # type: ignore
        raise HTTPException(status_code=400, detail="El correo electrónico ya está en uso")

    # Actualiza los campos proporcionados
    update_data = user_update.model_dump(exclude_unset=True)

    # Eliminar campos que no se deben actualizar
    update_data.pop('actualpassword', None)
    update_data.pop('newpasswordconfirmation', None)

    if 'hashed_password' in update_data:
        update_data['hashed_password'] = crypt.hash(update_data['hashed_password'])
    else:
        update_data.pop('hashed_password', None)

    # Realiza la actualización
    user_obj.update(**update_data)
    return user_obj.reload()


@router.delete("/users/{user_id}", response_model=UserDisplay)
async def delete_user(user_id: str):
    # Busca el usuario por ID
    user_obj = UserModel.objects(id=user_id).first() # type: ignore
    if user_obj:
        # Si el usuario existe, elimínalo
        deleted_user = user_obj.to_mongo().to_dict()  # Convertir a diccionario antes de eliminar
        user_obj.delete()
        return UserDisplay(**deleted_user)  # Devuelve la representación del usuario eliminado
    else:
        # Si el usuario no se encuentra, lanza una excepción
        raise HTTPException(status_code=404, detail="User not found")

# Otros endpoints como autenticación, reseteo de contraseña, etc.
