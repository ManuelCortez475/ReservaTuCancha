import os
from DataBase import conectarDB, cerrarDB, ejecutar, ejecutarConsulta
from Insertar import altaUsuario, bajaUsuario, modificarUsuario, consultarUsuarioXId
from flask import Flask


def main():
    app = Flask(__name__,template_folder='templates',static_folder='static')

    app.config['MAX_CONTENT_PATH']=1000 #clave para determinar la cantidad de subida de informacion de un upload de un archivo
    
    route(app)
    app.run('0.0.0.0',5000,debug=True)
main()