from DataBase import conectarDB, cerrarDB, ejecutar, ejecutarConsulta

def altaUsuario(mail,contraseña,categoria):
    sQuery = """
            INSERT INTO usuario
            (id, mail, contraseña, categoria)
            VALUES
            (NULL,"{}","{}","{}")
    """.format(mail,contraseña,categoria)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery) #la respuesta de un insert son las filas afectadas (un entero)
    cerrarDB(connDB)
    return res

def bajaUsuario(_id):
    sQuery = """"
        DELETE FROM usuario
        WHERE id = {}
        """.format(_id)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery)
    cerrarDB(connDB)
    return res

def modificarUsuario(_id,campo,valorNuevo):
    sQuery="UPDATE usuario SET {}={} WHERE id={}".format(campo,valorNuevo,_id)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery)
    cerrarDB(connDB)
    return res

def consultarUsuarioXId (id):
    sQuery="SELECT * FROM usuario where id={}".format(id)
    connDB = conectarDB()
    res = ejecutarConsulta(connDB,sQuery)
    cerrarDB(connDB)
    return res
