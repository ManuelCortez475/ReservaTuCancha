from _mysql_db import conectarDB, cerrarDB, ejecutar, ejecutarConsulta

def altaUsuario(mail,contraseña,categoria):
    sQuery = """
            INSERT INTO usuario
            (id,mail,contraseña,categoria)
            VALUES
            (NULL,%s,%s,%s)
    """
    val=(mail,contraseña,categoria)
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery, val) #la respuesta de un insert son las filas afectadas (un entero)
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
        (id,nombre,apellido,telefono,fecha_nacimiento,ciudad,descripcion,imagen,id_usuario)
        VALUES
        (NULL,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    id_usuario= consultarIdXMailPass(di.get('Email'),di.get('Contraseña'))
    val=(di.get('Nombre'),
         di.get('Apellido'),
         di.get('Telefono'),
         di.get('FechaNacimiento'),
         di.get('Ciudad'),
         di.get('Descripcion'),
         di.get('ImagenPerfil'),
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

def updateInfoPerfil(di,id_usuario):
    sQuery="""
        UPDATE perfil SET
        nombre = %s,
        apellido = %s,
        telefono = %s,
        fecha_nacimiento = %s,
        ciudad = %s,
        descripcion = %s
        imagen = %s
        WHERE id_usuario = %s
        """
    perfilActual = obtenerPerfilPorUsuario(id_usuario)
    nombre = di.get('Nombre') or perfilActual.get('Nombre')
    apellido = di.get('Apellido') or perfilActual.get('Apellido')
    telefono = di.get('Telefono') or perfilActual.get('Telefono')
    fecha = di.get('FechaNacimiento') or perfilActual.get('FechaNacimiento')
    ciudad = di.get('Ciudad') or perfilActual.get('Ciudad')
    descripcion = di.get('Descripcion') or perfilActual.get('Descripcion')
    imagenPerfil = di.get('ImagenPerfil') or perfilActual.get('ImagenPerfil')
    val=(nombre,
         apellido,
         telefono,
         fecha,
         ciudad,
         descripcion,
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

def validarUsuario(dic,email, password):
    sQuery = "SELECT id, categoria FROM usuario WHERE mail=%s AND contraseña=%s"
    connDB = conectarDB()
    try:
        consulta = ejecutarConsulta(connDB, sQuery, (email, password))
    finally:
        cerrarDB(connDB)
    if not consulta:
        return False
    dic["id"] = consulta[0][0]
    dic["email"] = email
    dic["categoria"]= consulta[0][1]
    return True


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

def consultarIdXMailPass(mail,Pass):
    sQuery='SELECT id FROM usuario WHERE mail=%s and contraseña=%s'
    connDB=conectarDB()
    try:
        res = ejecutarConsulta(connDB,sQuery,(mail,Pass))
    finally:
        cerrarDB(connDB)
    if res:
        return res[0][0]
    return None


def obtenerPerfilXEmailPass(result,email,Pass):
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
    connDB = conectarDB()
    res=False
    sSql="""SELECT id, nombre,apellido,telefono,fecha_nacimiento,ciudad,descripcion,imagen 
    FROM  perfil WHERE  id_usuario = %s;"""
    id_usuario = consultarIdXMailPass(email,Pass)
    val=(id_usuario,)
    fila= ejecutarConsulta(connDB,sSql,val)
    if fila!=[]:
        res=True
        result['id']=fila[0][0]
        result['nombre']=fila[0][1]
        result['apellido']=fila[0][2]
        result['telefono']=fila[0][3]
        result['fecha_nacimiento']=fila[0][4]
        result['ciudad']=fila[0][5]
        result['descripcion']=fila[0][6]
        result['email']=email
        result['contraseña']=Pass
        result['imagenPerfil']=fila[0][7]
        result['categoria']= consultarCategoriaDeUsuarioXMail(email)

    cerrarDB(connDB)
    return res    

def obtenerPerfilPorUsuario(id_usuario):
    sQuery = """
        SELECT nombre, apellido, telefono, fecha_nacimiento, ciudad, descripcion, imagen
        FROM perfil
        WHERE id_usuario = %s
    """
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB, sQuery, (id_usuario,))
    finally:
        cerrarDB(connDB)

    if res:
        return {
            "Nombre": res[0][0],
            "Apellido": res[0][1],
            "Telefono": res[0][2],
            "FechaNacimiento": res[0][3],
            "Ciudad": res[0][4],
            "Descripcion": res[0][5],
            'ImagenPerfil': res[0][6]
        }
    return {}

BASE={ "host":"localhost",
        "user":"root",
        "pass":"",
        "dbname":"usuario"}

def actualizarImagenPerfil(email, imagen):
    sQuery = """
        UPDATE usuario
        SET ImagenPerfil = %s
        WHERE Email = %s
    """
    connDB = conectarDB()
    ejecutar(sQuery, (imagen, email))
    cerrarDB(connDB)


def consultarImagenPerfilPorEmail(email):
    sQuery = """
        SELECT ImagenPerfil
        FROM usuario
        WHERE Email = %s
    """
    connDB = conectarDB()
    res = ejecutarConsulta(sQuery, (email,))
    cerrarDB(connDB)
    return res[0]['ImagenPerfil'] if res else None
