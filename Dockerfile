#Construir la imagen: docker build -t mi-backend-fastapi .
#Ejecutar el contenedor: docker run -d --name mi-backend -p 8000:8000 mi-backend-fastapi
FROM python:3.11-alpine

WORKDIR /app

copy requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
