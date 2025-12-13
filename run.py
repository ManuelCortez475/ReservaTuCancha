import os
from _mysql_db import conectarDB, cerrarDB, ejecutar, ejecutarConsulta
from model import altaPerfil, bajaPerfil, modificarTabla, consultarTablaXId, consultarTablaXCampoYValor
from flask import Flask, session
from route import route


def main():
    app = Flask(__name__,template_folder='templates',static_folder='static')

    app.config['SECRET_KEY']='inicializar de session'
    
    route(app)
    app.run('0.0.0.0',5000,debug=True)
main()
