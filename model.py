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


def obtenerPerfilXEmailPass(result,email):
    '''### Información:
       Obtiene todos los campos de la tabla usuario a partir de la clave 'email'
         y del 'password'.
       Carga la información obtenida de la BD en el dict 'result'
       Recibe 'result' in diccionario donde se almacena la respuesta de la consulta
       Recibe 'email' que es el mail si se utiliza como clave en la búsqueda
       Recibe 'password' que se utiliza en la consulta. (Para validadar al usuario)
       Retorna:
        True cuando se obtiene un registro de u usuario a partir del 'email' y el 'pass.
        False caso contrario.
    '''
    res=False
    sSql="""SELECT id, nombre,apellido,telefono,fecha_nacimiento,ciudad,descripcion 
    FROM  perfil WHERE  id_usuario = %s;"""
    id_usuario = consultarIdXMail(email)
    val=(id_usuario)
    fila= ejecutarConsulta(BASE,sSql,val)
    if fila!=[]:
        res=True
        result['id']=fila[0][0]
        result['nombre']=fila[0][1]
        result['apellido']=fila[0][2]
        result['telefono']=fila[0][3]
        result['fecha_nacimiento']=fila[0][4]
        result['ciudad']=fila[0][5]
        result['descripcion']=fila[0][6]
        result['categoria']= consultarCategoriaDeUsuarioXMail(email)
    return res    

BASE={ "host":"localhost",
        "user":"root",
        "pass":"",
        "dbname":"usuario"}