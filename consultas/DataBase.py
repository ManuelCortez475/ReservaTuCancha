import mysql.connector

def conectarDB(miBase="usario"):
    connDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=miBase)
    return connDB

def cerrarDB(connDB):
    if connDB!=None:
        connDB.close()

def ejecutarConsulta(connDB,sQuery):
    #SELECT
    base = connDB.cursor()   #es como un USE
    base.execute(sQuery)     #me deja la consulta en la variable base
    resultado = base.fetchall()      #con el fetchall extraemos el formato que tiene en el cursos la consulta y devuelve una lista
    return resultado

def ejecutar (connDB,sQuery):
    #INSERT, UPDATE, DELETE
    res=None
    base=connDB.cursor()
    try:
        base.execute(sQuery)  #prueba y ejecuta la operacion pero no cambia nada
        connDB.commit()       # se confirma el cambio en la base da datos
        res=base.rowcount
    except mysql.connector.Error as e:
        connDB.rollback()
        print(e,"Fallo, se hizo rollback")
    return res