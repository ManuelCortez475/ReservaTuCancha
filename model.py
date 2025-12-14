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



def consultarContraseñaDeUsuarioExistenteXMail (mail):
    sQuery="SELECT contraseña FROM usuario where mail= %s"
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB, sQuery, (mail,))
    finally:
        cerrarDB(connDB)
    if res:
        return res[0][0]
    return None


def consultarCategoriaDeUsuarioXMail (mail):
    sQuery="SELECT categoria FROM usuario where mail= %s"
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB, sQuery, (mail,))
    finally:
        cerrarDB(connDB)
    if res:
        return bool(res[0][0])
    return None



