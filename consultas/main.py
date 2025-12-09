from DataBase import conectarDB, cerrarDB, ejecutar, ejecutarConsulta
from Insertar import altaUsuario, bajaUsuario, modificarUsuario, consultarUsuarioXId

def main():
    import mysql.connector
    connDB = conectarDB()
    
    
    cerrarDB(connDB)
main()