from flask import request, session,redirect,render_template
from datetime import datetime
from model import *
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
from appConfig import config

def getRequet(diResult):  # Función para obtener los datos de la solicitud y almacenarlos en un diccionario
    if request.method=='POST':                    # Si el método de la solicitud es POST
        for name in request.form.to_dict().keys():  # Itera sobre las claves del formulario
            li=request.form.getlist(name)           # Obtiene la lista de valores para cada clave
            if len(li)>1:                           # Si hay más de un valor
                diResult[name]=request.form.getlist(name)  # Almacena la lista de valores en el diccionario
            elif len(li)==1:                        # Si hay un solo valor
                diResult[name]=li[0]                # Almacena el valor en el diccionario
            else:                                   # Si no hay valores
                diResult[name]=""                   # Almacena una cadena vacía en el diccionario
    elif request.method=='GET':                   # Si el método de la solicitud es GET
        for name in request.args.to_dict().keys():  # Itera sobre las claves de los argumentos
            li=request.args.getlist(name)           # Obtiene la lista de valores para cada clave
            if len(li)>1:                           # Si hay más de un valor
                diResult[name]=request.args.getlist(name)  # Almacena la lista de valores en el diccionario
            elif len(li)==1:                        # Si hay un solo valor
                diResult[name]=li[0]                # Almacena el valor en el diccionario
            else:                                   # Si no hay valores
                diResult[name]=""                   # Almacena una cadena vacía en el diccionario

 
def upload_file (diResult) :
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.pdf']
    MAX_CONTENT_LENGTH = 1024 * 1024     
    if request.method == 'POST' :         
        for key in request.files.keys():  
            diResult[key]={} 
            diResult[key]['file_error']=False            
            
            f = request.files[key] 
            if f.filename!="":     
                #filename_secure = secure_filename(f.filename)
                file_extension=str(os.path.splitext(f.filename)[1])
                filename_unique = uuid4().__str__() + file_extension
                path_filename=os.path.join( config['upload_folder'] , filename_unique)
                # Validaciones
                if file_extension not in UPLOAD_EXTENSIONS:
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: No se admite subir archivos con extension '+file_extension
                if os.path.exists(path_filename):
                    diResult[key]['file_error']=True
                    diResult[key]['file_msg']='Error: el archivo ya existe.'
                    diResult[key]['file_name']=f.filename
                try:
                    if not diResult[key]['file_error']:
                        
                        f.save(path_filename)

                        diResult[key]['file_error'] = False
                        diResult[key]['file_name_new'] = filename_unique
                        diResult[key]['file_name'] = f.filename
                        diResult[key]['file_msg'] = 'OK. Archivo cargado exitosamente'
                except Exception as e:
                    diResult[key]['file_error'] = True
                    diResult[key]['file_msg'] = str(e)
            else:
                continue # viene vacio el input del file upload

    # si existe el archivo devuelve True
    # os.path.exists(os.path.join('G:\\directorio\\....\\uploads',"agua.png"))

    # borrar un archivo
    # os.remove(os.path.join('G:\\directorio\\.....\\uploads',"agua.png"))


def obtenerDatosMenu(param):
    param["menu"]= [{"href":"/home","contenido":"Home"},
                    {"href":"/login","contenido":"Log In"},
                    {"href":"/logout","contenido":"Log Out"},
                    {"href":"/About","contenido":"About"},
                    {"href":"#","contenido":'&#128587'}#1F64B  # &#128587; #u'\u2630'
                   ]
   

def obtenerDatosTabla(param):
    param['titulo']="El titulo principal tabla"
    param['parrafo_01']="Esto es una prueba con una tabla"
    param['tabla']={"titulos":["NOMBRE","APELLIDO","DNI","EDAD"],
                      "datos":[["Juan","Perez",1234,23],
                              ["Laura","Lopez",9632,55],
                              ["Lucia","Marano",8775,28],
                              ["Pablo","Cuti",7744,63]
                        ]
                    }

    
def cargarSesion(dicUsuario):
    '''info:
        Realiza la carga de datos del usuario
        en la variable global dict 'session'.
        recibe 'dicUsuario' que es un diccionario con datos
               de un usuario.
        Comentario: Usted puede agregar en 'session' las claves que necesite
    '''
    session['id_perfil'] = dicUsuario['id_perfil']
    session['id_usuario'] = dicUsuario['id_usuario']
    session['Nombre'] = dicUsuario['nombre'] or ''
    session['Apellido'] = dicUsuario['apellido'] or ''
    session['Telefono'] = dicUsuario['telefono'] or ''
    session['FechaNacimiento'] = dicUsuario['fecha_nacimiento'] or ''
    session['Ciudad'] = dicUsuario['ciudad'] or ''
    session['Descripcion'] = dicUsuario['descripcion'] or ''
    session['Email']     = dicUsuario['email']
    session['Contraseña']   = dicUsuario['contraseña']
    session['Rol']   = dicUsuario['categoria']
    session['ImagenPerfil'] = dicUsuario['imagenPerfil'] or ''
    session["time"]       = datetime.now()  

def crearSesion(request):
    '''info:
        Crea una sesion. Consulta si los datos recibidos son validos.
        Si son validos carga una sesion con los datos del usuario
        recibe 'request' una solicitud htpp con los datos 'email' y 'pass' de 
        un usuario.
        retorna True si se logra un session, False caso contrario
    '''
    dicUsuario={}
    mirequest={}
    getRequet(mirequest)
    upload_file(mirequest)
    email = mirequest.get("Email")
    password = mirequest.get("Contraseña")
    if not validarUsuario(
        dicUsuario,
        email,
        password
    ):
        return False
    if not obtenerPerfilXEmailPass(dicUsuario, email, password):
        dicUsuario.update({
        'nombre': '',
        'apellido': '',
        'telefono': '',
        'fecha_nacimiento': '',
        'ciudad': '',
        'descripcion': '',
        'imagenPerfil': '',
        'email': email,
        'contraseña': password,
        'categoria': consultarCategoriaDeUsuarioXMail(email)
        })
    print("ID USUARIO:", dicUsuario['id_usuario'])
    print("ID PERFIL:", dicUsuario.get('id_perfil'))

    cargarSesion(dicUsuario)
    return True
def haySesion():  
    '''info:
        Determina si hay una sesion activa observando si en el dict
        session se encuentra la clave 'username'
        retorna True si hay sesión y False si no la hay.
    '''
    return session.get("Email") is not None

def cerrarSesion():
    '''info:
        Borra el contenido del dict 'session'
    '''
    try:    
        session.clear()
    except:
        pass