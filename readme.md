Implementar HTTP3 para mejor conexión en teléfonos móviles :) https://medium.com/@vamsikrishnabhuvanam/enhancing-fastapi-performance-with-http-2-and-quic-http-3-for-efficient-machine-learning-189cd054846e

/api: Contiene las rutas/endpoints de tu API, organizados por versiones para facilitar el mantenimiento y la escalabilidad a medida que tu API crece.

/core: Aloja la configuración central de tu aplicación, junto con cualquier lógica relacionada con la seguridad.

/crud: Encargado de las operaciones de base de datos (crear, leer, actualizar, eliminar), manteniendo esta lógica separada de tus rutas/endpoints.

/db: Maneja la configuración de la base de datos, incluyendo la conexión a MongoDB Atlas.

/models: Define los modelos de datos utilizando MongoEngine, que se traducirán directamente a documentos en tu base de datos MongoDB.

/schemas: Define los esquemas Pydantic que se utilizarán para la validación de la entrada y salida de datos en tus endpoints.

/tests: Incluye pruebas automatizadas para tu aplicación.

main.py: Es el archivo de entrada para ejecutar tu aplicación FastAPI.

requirements.txt: Lista todas las dependencias de Python necesarias para tu proyecto
