from flask import Flask, render_template, request, redirect, session, flash, url_for
from werkzeug.utils import secure_filename    # Valida caracteres seguros en el nombre del un archivo
from appConfig import config                  # Archivo de configuracion de la aplicación
from uuid import uuid4                        # Crea Universally Unique IDentifier (UUID)  # https://docs.python.org/es/3/library/uuid.html#uuid.UUID
from controller import *
import os                                   # Gestiona acceso al sistema operativo local

def route(app):
    @app.route("/")
    @app.route("/home")
    def home():
        return render_template('Pantalla_Inicial.html')
    

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/datosLogin',methods = ['POST', 'GET']) # 
    def formLogin():
        diRequestLogin={}            # Inicializa un diccionario vacío para almacenar los datos de la solicitud
        getRequet(diRequestLogin)    # Llena el diccionario con datos de la solicitud (ya sea POST o GET)
        upload_file(diRequestLogin)  # Maneja la carga de archivos y actualiza el diccionario con la información de la carga de archivos
        print(diRequestLogin)
        return diRequestLogin        # Devuelve el diccionario que contiene todos los datos de la solicitud y la información de la carga de archivos


    @app.route('/perfil',methods = ['POST', 'GET']) # 
    def formPerfil():
        diRequestPerfil={}           
        getRequet(diRequestPerfil)   
        upload_file(diRequestPerfil)
        return render_template('perfil.html',
                               nombre= diRequestPerfil.get('Nombre'),
                               apellido = diRequestPerfil.get('Apellido'),
                               ciudad = diRequestPerfil.get('Ciudad'),
                               fechaNacimiento = diRequestPerfil.get('FechaNacimiento'),
                               email = diRequestPerfil.get('Email'),
                               telefono = diRequestPerfil.get('Telefono'),
                               partidos = diRequestPerfil.get('PartidosJugados'),
                               goles = diRequestPerfil.get('Goles'),
                               partidosGanados = diRequestPerfil.get('PartidosGanados'))
    

    @app.route('/perfilAdmin',methods = ['POST', 'GET']) # 
    def formPerfilAdmin():
        diRequestPerfilAdmin={}           
        getRequet(diRequestPerfilAdmin)   
        upload_file(diRequestPerfilAdmin)
        print(diRequestPerfilAdmin)
        return render_template('perfil_admin.html',
                               nombre= diRequestPerfilAdmin.get('Nombre'),
                               apellido = diRequestPerfilAdmin.get('Apellido'),
                               ciudad = diRequestPerfilAdmin.get('Ciudad'),
                               fechaNacimiento = diRequestPerfilAdmin.get('FechaNacimiento'),
                               email = diRequestPerfilAdmin.get('Email'),
                               telefono = diRequestPerfilAdmin.get('Telefono'),
                               partidos = diRequestPerfilAdmin.get('PartidosJugados'),
                               goles = diRequestPerfilAdmin.get('Goles'),
                               partidosGanados = diRequestPerfilAdmin.get('PartidosGanados'))
    
    @app.route('/<name>') # dinámico
    def general(name):
        if name=="tabla":
            param={}
            obtenerDatosTabla(param)
            res= render_template('tabla.html', param=param)
        else:
            res='Pagina "{}" no encontrada'.format(name)
        return res
    
    @app.route('/misreservas')
    def misreservas():
        return render_template('misreservas.html')
    
    @app.route('/pagina_pago', methods = ['POST', 'GET']) # 
    def formPaginaPago():
        diRequestPago={}           
        getRequet(diRequestPago)   
        upload_file(diRequestPago)
        print(diRequestPago)
        return render_template('pagina_pago.html', 
                              )
    

    @app.route('/publicaciones')
    def publicaciones():
        return render_template('publicaciones.html')
    
    @app.route('/registro',methods = ['POST', 'GET']) # 
    def formRegistro():
        if request.method == 'POST':
            categoria = request.form.get('categoria')
            if categoria == "Usuario":
                return redirect(url_for('formPerfil'))       # ruta perfil de usuario
            elif categoria == "Admin":
                return redirect(url_for('perfil_admin'))     # ruta perfil de admin
            else:
                flash("Selecciona una categoría válida")
                return redirect(url_for('formRegistro'))

        return render_template('registro.html')
    
    
    @app.route('/reservaAdmin',methods = ['POST', 'GET']) # 
    def formReservaAdmin():
        if request.method == 'GET':
            return render_template('reservaAdmin.html', canchas=session.get('canchas_publicadas', []))
        else: 
            diRequestReservaAdmin={}           
            getRequet(diRequestReservaAdmin)   
            upload_file(diRequestReservaAdmin)
            print(diRequestReservaAdmin)
            
            boton_id = None

            for key in request.form.keys():
                if key.startswith('btnPublicar'):
                    boton_id = key  # ej: btnPublicar3
                    break
            numero = boton_id.replace('btnPublicar', '')
            if boton_id is None:
                flash('No se detectó botón de publicación')
                return redirect(url_for('formReservaAdmin'))
            cancha = {
                'numero': numero,
                'nombre': request.form.get(f'NombreCancha{numero}'),
                'ubicacion': request.form.get(f'UbicacionCancha{numero}'),
                'jugadores': request.form.get(f'CantidadJug{numero}'),
                'estado': request.form.get(f'Estado{numero}'),
                'fecha': request.form.get('Fecha'),
                'inicio': request.form.get(f'start{numero}'),
                'fin': request.form.get(f'end{numero}')
            }
            if 'canchas_publicadas' not in session:
                session['canchas_publicadas'] = []
            canchas = session.get('canchas_publicadas',[])
            canchas.append(cancha)
            session['canchas_publicadas'] = canchas
            return redirect(url_for('formReservaAdmin'))
        
    @app.route('/confirmarPublicaciones', methods=['POST'])
    def confirmar_publicaciones():

        canchas = session.get('canchas_publicadas', [])

        for cancha in canchas:
            # 👇 ACÁ VA LA DB (ejemplo)
            print("Guardando en DB:", cancha)

        # 🔥 limpiar session
        session.pop('canchas_publicadas', None)

        flash("Canchas publicadas con éxito")
        return redirect(url_for('formReservaAdmin'))

    @app.route('/reservar')
    def reserva():
        return render_template('reservar.html')
    
    @app.route('/datosReservar',methods = ['POST', 'GET']) # 
    def formReservar():
        diRequestReservar={}           
        getRequet(diRequestReservar)   
        upload_file(diRequestReservar)
        print(diRequestReservar)
        return diRequestReservar
    
    
    @app.route('/unirse')
    def unirse():
        return render_template('unirse.html')
    


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
                        diResult[key]['file_error']=True
                        diResult[key]['file_msg']='Se ha producido un error.'

                        f.save(path_filename)   
                        diResult[key]['file_error']=False
                        diResult[key]['file_name_new']=filename_unique
                        diResult[key]['file_name']=f.filename
                        diResult[key]['file_msg']='OK. Archivo cargado exitosamente'
 
                except:
                        pass
            else:
                diResult[key]={} # viene vacio el input del file upload

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

    