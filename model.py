from _mysql_db import conectarDB, cerrarDB, ejecutar, ejecutarConsulta

def altaUsuario(mail,contraseña,categoria):
    sQuery = """
            INSERT INTO usuario
            (id,mail,contraseña,categoria)
            VALUES
            (NULL,"{}","{}",{})
    """.format(mail,contraseña,categoria)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery) #la respuesta de un insert son las filas afectadas (un entero)
    cerrarDB(connDB)
    return res

def bajaUsuario(_id):
    sQuery = """
        DELETE FROM usuario
        WHERE id = {}
        """.format(_id)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery)
    cerrarDB(connDB)
    return res



def modificarTabla(tabla,campo,valorNuevo,_id):
    sQuery="UPDATE {} SET {}={} WHERE id={}".format(tabla,campo,valorNuevo,_id)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery)
    cerrarDB(connDB)
    return res



def consultarTablaXId (tabla,id):
    sQuery="SELECT * FROM {} where id={}".format(tabla,id)
    connDB = conectarDB()
    res = ejecutarConsulta(connDB,sQuery)
    cerrarDB(connDB)
    return res

def consultarTablaXCampoYValor (tabla,campo,valor):
    sQuery="SELECT * FROM {} where {}='{}'".format(tabla,campo,valor)
    connDB = conectarDB()
    res = ejecutarConsulta(connDB,sQuery)
    cerrarDB(connDB)
    return res


