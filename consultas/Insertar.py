from DataBase import conectarDB, cerrarDB, ejecutar, ejecutarConsulta

def altaPerfil(nombre, apellido, telefono, fecha_nacimiento, ciudad, descripcion):
    sQuery = """
            INSERT INTO perfil
            (id, nombre, apellido, telefono, fecha_nacimiento, ciudad, descripcion)
            VALUES
            (NULL,"{}","{}","{}","{}","{}","{}")
    """.format(nombre, apellido, telefono, fecha_nacimiento, ciudad, descripcion)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery) #la respuesta de un insert son las filas afectadas (un entero)
    cerrarDB(connDB)
    return res

def bajaPerfil(_id):
    sQuery = """
        DELETE FROM perfil
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


