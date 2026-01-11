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

def agregarInfoPerfil (di,id_usuario):
    sQuery="""
        INSERT INTO perfil
        (id,nombre,apellido,telefono,fecha_nacimiento,ciudad,descripcion,imagen,partidosJugados,goles,partidosGanados,id_usuario)
        VALUES
        (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    img = di.get('ImagenPerfil')
    if isinstance(img, dict) and img.get('file_name_new'):
        imagenPerfil = img['file_name_new']
    else:
        imagenPerfil = None
    val=(di.get('Nombre'),
         di.get('Apellido'),
         di.get('Telefono'),
         di.get('FechaNacimiento'),
         di.get('Ciudad'),
         di.get('Descripcion'),
         imagenPerfil,
         di.get('PartidosJugados'),
         di.get('Goles'),
         di.get('PartidosGanados'),
         id_usuario
         )
    connDB = conectarDB()
    try:
        res = ejecutar(connDB, sQuery, val)
        print("ROWCOUNT:", res)
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
        descripcion = %s,
        imagen = %s,
        partidosJugados = %s,
        goles = %s,
        partidosGanados = %s
        WHERE id_usuario = %s
        """
    perfil={}
    perfilActual = obtenerPerfilPorUsuario(perfil,id_usuario)
    imagenPerfil = di.get('ImagenPerfil')
    if not imagenPerfil:
        imagenPerfil = perfilActual.get('ImagenPerfil')


    val=(di.get('Nombre') or perfilActual.get('Nombre'),
         di.get('Apellido') or perfilActual.get('Apellido'),
         di.get('Telefono') or perfilActual.get('Telefono'),
         di.get('FechaNacimiento') or perfilActual.get('FechaNacimiento'),
         di.get('Ciudad') or perfilActual.get('Ciudad'),
         di.get('Descripcion') or perfilActual.get('Descripcion'),
         imagenPerfil,
         di.get('PartidosJugados') or perfilActual.get('PartidosJugados'),
         di.get('Goles') or perfilActual.get('Goles'),
         di.get('PartidosGanados') or perfilActual.get('PartidosGanados'),
         id_usuario
         )
    connDB = conectarDB()
    try:
        res = ejecutar(connDB, sQuery, val)
        print("QUERY:", sQuery)
        print("VALORES:", val)
        print("ROWCOUNT:", res)
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
        connDB.commit()
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
    sSql="""SELECT id, nombre,apellido,telefono,fecha_nacimiento,ciudad,descripcion,imagen, partidosJugados, goles, partidosGanados 
    FROM  perfil WHERE  id_usuario = %s;"""
    id_usuario = consultarIdXMailPass(email,Pass)
    val=(id_usuario,)
    fila= ejecutarConsulta(connDB,sSql,val)
    if fila!=[]:
        res=True
        result['id_perfil']=fila[0][0]
        result['id_usuario'] = id_usuario
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
        result['partidosJugados'] = fila[0][8]
        result['goles'] = fila[0][9]
        result['partidosGanados'] = fila[0][10]

    cerrarDB(connDB)
    return res    

def obtenerPerfilPorUsuario(di,id_usuario):
    sQuery = """
        SELECT nombre, apellido, telefono, fecha_nacimiento, ciudad, descripcion, imagen, partidosJugados, goles, partidosGanados
        FROM perfil
        WHERE id_usuario = %s
    """
    print('Id usuario:',id_usuario)
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB, sQuery, (id_usuario,))
    finally:
        cerrarDB(connDB)

    if res:
            di["Nombre"] =  res[0][0]
            di["Apellido"] = res[0][1]
            di["Telefono"] = res[0][2]
            di["FechaNacimiento"] = res[0][3]
            di["Ciudad"] = res[0][4]
            di["Descripcion"] = res[0][5]
            di['ImagenPerfil'] = res[0][6]
            di['PartidosJugados'] = res[0][7]
            di['Goles'] = res[0][8]
            di['PartidosGanados'] = res[0][9]
    return di

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


def insertarCanchaEnBD(di):
    fila_numero = None
    for key in di.keys():
        if key.startswith("btnPublicar"):
            fila_numero = key.replace("btnPublicar", "")
            break
    if fila_numero is None:
        return "No se detectó ninguna fila para publicar"
    cancha_data = {
        "NombreCancha": di.get(f"NombreCancha{fila_numero}"),
        "UbicacionCancha": di.get(f"UbicacionCancha{fila_numero}"),
        "CantidadJug": di.get(f"CantidadJug{fila_numero}"),
        "Fecha": di.get(f"Fecha{fila_numero}"),
        "Inicio": di.get(f"start{fila_numero}"),
        "Fin": di.get(f"end{fila_numero}"),
        "Estado": di.get(f"Estado{fila_numero}"),
        "Precio": di.get(f"Precio{fila_numero}")
    }
    print("Datos de la fila a publicar:", cancha_data)
    sQuery = """
    INSERT INTO cancha 
    (id,nombre, estado, ubicacion, cant_jugadores, precio)
    VALUES
    (NULL,%s,%s,%s,%s,%s)
    """
    val = (
        cancha_data.get('NombreCancha'),
        cancha_data.get('Estado'),
        cancha_data.get('UbicacionCancha'),
        cancha_data.get('CantidadJug'),
        cancha_data.get('Precio')
        
    )
    connDB = conectarDB()
    res = ejecutar(connDB,sQuery, val)
    cerrarDB(connDB)
    print ("Filas afectadas: ", res)
    return res

def consultarCanchasPublicadas():
    sQuery = """
        SELECT * FROM cancha
    """
    connDB = conectarDB()
    res = ejecutarConsulta(connDB, sQuery)
    cerrarDB(connDB)
    canchas = []
    for fila in res:
        cancha = {
            'id_cancha': fila[0],
            'NombreCancha': fila[1],
            'Fecha': fila[2],
            'Estado': fila[3],
            'Ubicacion': fila[4],
            'CantJugadores': fila[5],
            'Precio': fila[6]
        }
        canchas.append(cancha)

    return canchas