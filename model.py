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
    dic["id_usuario"] = consulta[0][0]
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


def insertarCanchaEnBD(di,id_usuario):
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
        "Fecha_Inicio": di.get(f"fecha_desde{fila_numero}"),
        "Fecha_Fin": di.get(f"fecha_hasta{fila_numero}"),
        "Inicio": di.get(f"Inicio{fila_numero}"),
        "Fin": di.get(f"Fin{fila_numero}"),
        "Estado": di.get(f"Estado{fila_numero}"),
        "Precio": di.get(f"Precio{fila_numero}")
    }
    print("Datos de la fila a publicar:", cancha_data)
    sQuery = """
    INSERT INTO cancha 
    (id, id_usuario, nombre, fecha_inicio, fecha_fin, inicio, fin, estado, ubicacion, cant_jugadores, precio)
    VALUES
    (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    val = (
        id_usuario,
        cancha_data.get('NombreCancha'),
        cancha_data.get('Fecha_Inicio'),
        cancha_data.get('Fecha_Fin'),
        cancha_data.get('Inicio'),
        cancha_data.get('Fin'),
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
            'id_usuario':fila[1],
            'NombreCancha': fila[2],
            'Fecha_Inicio': fila[3],
            'Fecha_Fin': fila[4],
            'Inicio': fila[5],
            'Fin': fila[6],
            'Estado': fila[7],
            'Ubicacion': fila[8],
            'CantJugadores': fila[9],
            'Precio': fila[10]
        }
        canchas.append(cancha)

    return canchas

def IdCanchaxNombre(nombre_cancha):
    sQuery = """
            SELECT id FROM cancha WHERE nombre = %s
            """
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB,sQuery,(nombre_cancha,))
    finally:
        cerrarDB(connDB)
    if res:
        return res[0][0]
    return None

def NombreJugadoresUbicacionCanchaxIdCancha(id_cancha):
    sQuery = """
            SELECT nombre,ubicacion,cant_jugadores FROM cancha WHERE id = %s
            """
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB,sQuery,(id_cancha,))
    finally:
        cerrarDB(connDB)
    if res:
        return res
    return None
def fechaHoraxIdCancha(id):
    sQuery = """
            SELECT fecha_reservada,hora FROM reserva_cancha WHERE id = %s
            """
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB,sQuery,(id,))
    finally:
        cerrarDB(connDB)
    if res:
        print('hola',res)
        return res
    return None

def insertarCanchaReservada(di, id_usuario, id_cancha):
    sQuery = """
            INSERT INTO reserva_cancha 
            (id, id_cancha, id_usuario, precio, fecha_reservada, hora, comprobante_pago, privacidad, Contraseña, JugadoresUnidos, Jugadores_Max)
            VALUES
            (NULL, %s, %s, %s, %s, %s, '', %s, %s, 0, %s)
            """
    val = (
        id_cancha,
        id_usuario,
        di.get("precio"),
        di.get("fecha_reservada"),
        di.get('hora'),
        di.get('privacidad'),
        di.get('clave_privada'), # Captura la clave del name="clave_privada" de tu HTML
        di.get('jugadores_cancha')
    )
    connDB = conectarDB()
    try:
        res = ejecutar(connDB, sQuery, val)
        return res
    except Exception as e:
        print(f"Error al guardar contraseña: {e}")
        return None
    finally:
        cerrarDB(connDB)


def buscarCanchasReservadas():
    sQuery="""
            SELECT * FROM reserva_cancha
            """
    connDB = conectarDB()
    res = ejecutarConsulta(connDB,sQuery)
    cerrarDB(connDB)
    canchasReservadas = []
    for fila in res:
        id_cancha = fila[1]
        info = NombreJugadoresUbicacionCanchaxIdCancha(id_cancha)
        cancha = {
            'id_cancha_reservada': fila[0],
            'id_cancha': id_cancha,
            'id_usuario': fila[2],
            'Nombre_Cancha': info[0][0],
            'Ubicacion': info[0][1],
            'Cant_Jugadores': info[0][2],
            'Precio': fila[3],
            'Fecha_Reservada': fila[4],
            'Hora': fila[5],
            'Comprobante_Pago': fila[6] or '',
            'Privacidad': fila[7],
            'Contraseña': fila[8],
            'JugadoresUnidos': fila[9],
            'Cant_Jugadores': fila[10]
        }
        canchasReservadas.append(cancha)
    return canchasReservadas
def idXIdCancha(id):
    sQuery="""
            SELECT id FROM reserva_cancha WHERE 
            id_cancha=%s
            AND 
            """
    connDB=conectarDB()
    res=ejecutarConsulta(connDB,sQuery,(id,))
    cerrarDB(connDB)
    return res[0][0]

def obtenerIdReserva(id_cancha, fecha, hora):
    sQuery = """
        SELECT id
        FROM reserva_cancha
        WHERE id_cancha = %s
        AND fecha_reservada = %s
        AND hora = %s
        LIMIT 1
    """
    connDB = conectarDB()
    try:
        res = ejecutarConsulta(connDB, sQuery, (id_cancha, fecha, hora))
    finally:
        cerrarDB(connDB)

    if res:
        return res[0][0]
    return None

def insertarUsuarioUnido (di,nombre_cancha):
    sQuery="""
            UPDATE reserva_cancha
            SET JugadoresUnidos = JugadoresUnidos + 1
            WHERE id = %s;
            """
    id_cancha=IdCanchaxNombre(nombre_cancha)
    id_reserva = obtenerIdReserva(id_cancha,di.get('fecha_reservada'),di.get('hora'))
    val = (
        id_reserva,
    )
    print(id_reserva)

    connDB=conectarDB()
    try:
        res = ejecutar(connDB, sQuery, val)
    finally:
        cerrarDB(connDB)
    return res

def buscarReservasXId(id):
    sQuery = """
            SELECT  
            reserva_cancha.fecha_reservada,
            reserva_cancha.hora,
            cancha.nombre,
            cancha.ubicacion
            FROM reserva_cancha
            INNER JOIN cancha ON reserva_cancha.id_cancha = cancha.id
            WHERE reserva_cancha.id_usuario = %s;
            """
    connDB = conectarDB()
    res = ejecutarConsulta(connDB,sQuery,(id,))
    cerrarDB(connDB)
    print(res)
    canchasReservadasXUsuario = []
    for cancha in res:
        reserva={
            'Fecha':cancha[0],
            'Hora':cancha[1],
            'Nombre':cancha[2],
            'Ubicacion':cancha[3]
        }
        canchasReservadasXUsuario.append(reserva)
    return canchasReservadasXUsuario

def canchasPublicadasXId (id):
    sQuery = """
            SELECT * FROM cancha
            WHERE id_usuario = %s;
            """
    connDB=conectarDB()
    res = ejecutarConsulta(connDB,sQuery,(id,))
    cerrarDB(connDB)
    canchasPublicadas=[]
    for fila in res:
        cancha={
            'Nombre':fila[2],
            'FechaI':fila[3],
            'FechaF':fila[4],
            'HoraI':fila[5],
            'HoraF':fila[6],
            'Ubicacion':fila[8],
            'Precio':fila[10]
        }
        canchasPublicadas.append(cancha)
    return canchasPublicadas

def bajarUsuarioUnido (di,nombre_cancha):
    sQuery="""
            UPDATE reserva_cancha
            SET JugadoresUnidos = JugadoresUnidos - 1
            WHERE id = %s;
            """
    id_cancha=IdCanchaxNombre(nombre_cancha)
    id_reserva = obtenerIdReserva(id_cancha,di.get('fecha_reservada'),di.get('hora'))
    val = (
        id_reserva,
    )
    print(id_reserva)

    connDB=conectarDB()
    try:
        res = ejecutar(connDB, sQuery, val)
    finally:
        cerrarDB(connDB)
    return res