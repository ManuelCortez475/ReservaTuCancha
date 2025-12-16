import mysql.connector

def conectarDB(miBase="usuario"):
    connDB = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=miBase)
    return connDB

def cerrarDB(connDB):
    if connDB!=None:
        connDB.close()

def ejecutarConsulta(connDB,sQuery, params=None):
    #SELECT
    base = connDB.cursor()   #es como un USE
    base.execute(sQuery,params)     #me deja la consulta en la variable base
    resultado = base.fetchall()      #con el fetchall extraemos el formato que tiene en el cursor la consulta y devuelve una lista
    return resultado

def ejecutar (connDB,sQuery,params=None):
    #INSERT, UPDATE, DELETE
    res=None
    base=connDB.cursor()
    try:
        base.execute(sQuery,params)  #prueba y ejecuta la operacion pero no cambia nada
        connDB.commit()       # se confirma el cambio en la base da datos
        res=base.rowcount
    except mysql.connector.Error as e:
        connDB.rollback()
        print(e,"Fallo, se hizo rollback")
    return res

def selectDB(configDB=None,sql="",val=None,title=False,dictionary=False):
    ''' ########## SELECT
        # recibe 'configDB' un 'dict' con los parámetros de conexion
        # recibe 'sql' una cadena con la consulta sql
        # recibe 'val' valores separados anti sql injection
        # recibe 'title' booleana
        # retorna una 'list' con el resultado de la consulta
        #     cada fila de la 'list' es una 'tuple'
        #     Si 'title' es True, entonces agrega a la lista
        #     los títulos de las columnas.
    '''
    resQuery=None
    if configDB!=None:
        mydb=conectarDB(configDB)
        resQuery=ejecutarConsulta(mydb,sQuery=sql,val=val,title=title,dictionary=dictionary)
        cerrarDB(mydb)
    return resQuery

BASE={ "host":"localhost",
        "user":"root",
        "pass":"",
        "dbname":"usuario"}