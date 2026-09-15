import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print("Ruta del archivo .env encontrada:", find_dotenv())
print("Valor leido en la terminal:", os.getenv("BIENVENIDA_MSG"))

app = Flask(__name__)

MENSAJE_BIENVENIDA = os.getenv("BIENVENIDA_MSG", "Hola Mundo por defecto")

@app.route('/')
def home():
    return f"<h1>{MENSAJE_BIENVENIDA}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
