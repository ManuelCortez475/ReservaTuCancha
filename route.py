from flask import Flask, render_template, request, redirect, session, flash, url_for
from werkzeug.utils import secure_filename    # Valida caracteres seguros en el nombre del un archivo
from appConfig import config                  # Archivo de configuracion de la aplicación
from uuid import uuid4                        # Crea Universally Unique IDentifier (UUID)  # https://docs.python.org/es/3/library/uuid.html#uuid.UUID
from controller import *
from model import *
import os                                   # Gestiona acceso al sistema operativo local

def route(app):
    @app.route("/")
    @app.route("/home")
    def home():
        return render_template('Pantalla_Inicial.html')
    

    @app.route('/registro',methods = ['POST', 'GET']) # 
    def formRegistro():
        if request.method == 'GET':
            return render_template('registro.html')
        
        else:
            categoria_str = request.form.get('categoria')
            if categoria_str == 'Usuario':
                categoria = True
            elif categoria_str == 'Admin':
                categoria = False            
            altaUsuario(request.form.get('email'), request.form.get('Contraseña'), categoria)
            return redirect(url_for('formLogin'))     # ruta perfil de admin
            

    @app.route('/login',methods = ['POST', 'GET']) # 
    def formLogin():
        if request.method == 'GET':
            return render_template('login.html')
        else:
            diRequestLogin={}            
            getRequet(diRequestLogin)    
            upload_file(diRequestLogin)  
            if diRequestLogin.get('Contraseña') == consultarContraseñaDeUsuarioExistenteXMail(diRequestLogin.get('Email')):
                session['email'] = diRequestLogin.get('Email')
                if consultarCategoriaDeUsuarioXMail(diRequestLogin.get('Email')) == True: 
                    redirect_route = 'formPerfil'
                elif consultarCategoriaDeUsuarioXMail(diRequestLogin.get('Email')) == False:
                    redirect_route = 'formPerfilAdmin'
            else:
                redirect_route = 'formLogin'
            return redirect(url_for(redirect_route))


    @app.route('/perfil',methods = ['POST', 'GET']) # 
    def formPerfil():
        
        email = session.get('email', '') 
        if request.method == 'GET':
            diRequestPerfil={}           
            getRequet(diRequestPerfil)   
            upload_file(diRequestPerfil)
            agregarInfoPerfil(diRequestPerfil)
            return render_template('perfil.html',
                                nombre= diRequestPerfil.get('Nombre'),
                                apellido = diRequestPerfil.get('Apellido'),
                                ciudad = diRequestPerfil.get('Ciudad'),
                                fechaNacimiento = diRequestPerfil.get('FechaNacimiento'),
                                email = email,
                                descripcion = diRequestPerfil.get('Descripcion'),
                                telefono = diRequestPerfil.get('Telefono'),
                                partidos = diRequestPerfil.get('PartidosJugados'),
                                goles = diRequestPerfil.get('Goles'),
                                partidosGanados = diRequestPerfil.get('PartidosGanados'))
        return render_template('perfil.html', email=email)
    

    @app.route('/perfilAdmin',methods = ['POST', 'GET']) # 
    def formPerfilAdmin():
        email = session.get('email', '') 
        if request.method == 'POST':
            diRequestPerfilAdmin={}           
            getRequet(diRequestPerfilAdmin)   
            upload_file(diRequestPerfilAdmin)
            agregarInfoPerfil(diRequestPerfilAdmin)
            return render_template('perfil_admin.html',
                                nombre= diRequestPerfilAdmin.get('Nombre'),
                                apellido = diRequestPerfilAdmin.get('Apellido'),
                                ciudad = diRequestPerfilAdmin.get('Ciudad'),
                                fechaNacimiento = diRequestPerfilAdmin.get('FechaNacimiento'),
                                email = email,
                                telefono = diRequestPerfilAdmin.get('Telefono'),
                                partidos = diRequestPerfilAdmin.get('PartidosJugados'),
                                goles = diRequestPerfilAdmin.get('Goles'),
                                partidosGanados = diRequestPerfilAdmin.get('PartidosGanados'))
        return render_template('perfil_admin.html', email=email)
    
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

    @app.route("/logout")
    def logout():  
        ''' Info: 
          Cierra la sesión.
          retorna la redirección a la pagina home   
        ''' 
        cerrarSesion()     
        return redirect('/')

