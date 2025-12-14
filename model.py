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

def agregarInfoPerfil (di):
    sQuery="""
        INSERT INTO perfil
        (id,nombre,apellido,telefono,fecha_nacimiento,ciudad,descripcion,id_usuario)
        VALUES
        (NULL,%s,%s,%s,%s,%s,%s,%s)
        """
    id_usuario= consultarIdXMail(di.get('Email'))
    val=(di.get('Nombre'),
         di.get('Apellido'),
         di.get('Telefono'),
         di.get('FechaNacimiento'),
         di.get('Ciudad'),
         di.get('Descripcion'),
         id_usuario
         )
    connDB = conectarDB()
    try:
        res = ejecutar(connDB, sQuery, val)
    finally:
        cerrarDB(connDB)
    if res:
        return res
    return None


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

def consultarIdXMail(mail):
    sQuery='SELECT id FROM usuario WHERE mail=%s'
    connDB=conectarDB()
    try:
        res = ejecutarConsulta(connDB,sQuery,(mail,))
    finally:
        cerrarDB(connDB)
    if res:
        return res[0][0]
    return None

