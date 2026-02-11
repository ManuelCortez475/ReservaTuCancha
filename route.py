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
            altaUsuario(request.form.get('Email'), request.form.get('Contraseña'), categoria)
            return redirect(url_for('formLogin'))
            

    @app.route('/login',methods = ['POST', 'GET']) # 
    def formLogin():
        if request.method == 'GET':
            return render_template('login.html')
        else:  
            crearSesion(request)
            if crearSesion(request):
                email = session.get('Email')
                if email and consultarCategoriaDeUsuarioXMail(email): 
                    redirect_route = 'formPerfil'
                else:
                    redirect_route = 'formPerfilAdmin'
            else:
                redirect_route = 'formLogin'
            return redirect(url_for(redirect_route))


    @app.route('/perfil', methods=['GET', 'POST'])
    def formPerfil():
        if haySesion():
            email = session.get('Email', '')
            diRequestPerfil = {}
            id_usuario = session.get('id_usuario','')
            if request.method == 'POST':
                getRequet(diRequestPerfil)
                upload_file(diRequestPerfil)
                img = diRequestPerfil.get('ImagenPerfil')
                if isinstance(img, dict):
                    if img.get('file_error') is False:
                        diRequestPerfil['ImagenPerfil'] = img.get('file_name_new')
                    else:
                        diRequestPerfil.pop('ImagenPerfil', None)
                di={}
                existePerfil = obtenerPerfilPorUsuario(di,id_usuario)
                
                if existePerfil == {}:
                    
                    agregarInfoPerfil(diRequestPerfil,id_usuario)
                else:
                    updateInfoPerfil(diRequestPerfil, id_usuario)

            return render_template(
                'perfil.html',
                diRequestPerfil=obtenerPerfilPorUsuario(diRequestPerfil,id_usuario),
                email=email
            )
        return redirect('/login')


    @app.route('/perfilAdmin', methods=['GET', 'POST'])
    def formPerfilAdmin():
        if haySesion():
            email = session.get('Email', '')
            diRequestPerfilAdmin = {}
            id_usuario = session.get('id_usuario','')
            if request.method == 'POST':
                getRequet(diRequestPerfilAdmin)
                upload_file(diRequestPerfilAdmin)
                img = diRequestPerfilAdmin.get('ImagenPerfil')
                if isinstance(img, dict):
                    if img.get('file_error') is False:
                        diRequestPerfilAdmin['ImagenPerfil'] = img.get('file_name_new')
                    else:
                        diRequestPerfilAdmin.pop('ImagenPerfil', None)
                di={}
                existePerfil = obtenerPerfilPorUsuario(di,id_usuario)
                if existePerfil == {}:

                    agregarInfoPerfil(diRequestPerfilAdmin,id_usuario)
                else:
                    updateInfoPerfil(diRequestPerfilAdmin, id_usuario)

            return render_template(
                'perfil_admin.html',
                diRequestPerfilAdmin=obtenerPerfilPorUsuario(diRequestPerfilAdmin,id_usuario),
                email=email
            )
        return redirect('/login')

    
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
        if haySesion():
            id_usuario = session.get('id_usuario')
            reservas = buscarReservasXId(id_usuario)
            return render_template('misreservas.html', canchasreservadas = reservas)
        return redirect('/login')
    
    @app.route('/pagina_pago', methods = ['POST', 'GET']) # 
    def formPaginaPago():
        if haySesion():
            diRequestPago={}           
            getRequet(diRequestPago)   
            upload_file(diRequestPago)
            reserva = session.get('cancha_reservada')
            if not reserva:
                return redirect('/reservar')
            return render_template('pagina_pago.html', reserva=reserva)
        return redirect('/login')
    

    @app.route('/publicaciones')
    def publicaciones():
        if haySesion():
            id_usuario = session.get('id_usuario')
            publicaciones = canchasPublicadasXId(id_usuario)
            return render_template('publicaciones.html', mispublicaciones = publicaciones)
        return redirect('/login')
    
    
    @app.route('/reservaAdmin', methods = ['POST', 'GET'])
    def formReservaAdmin (): 
        if haySesion():
            if request.method == 'GET':
                return render_template('reservaAdmin.html')   
            
            id_usuario = session.get('id_usuario')
            diRequestReservaAdmin={}           
            getRequet(diRequestReservaAdmin)   
            upload_file(diRequestReservaAdmin)
            insertarCanchaEnBD(diRequestReservaAdmin,id_usuario)
            return redirect('/reservaAdmin')
        return redirect('/login')
                

    @app.route('/reservar',methods = ['POST', 'GET']) # 
    def formReservar():
        if haySesion():
            if request.method == "GET":
                canchas = consultarCanchasPublicadas()

                for cancha in canchas:
                    inicio = cancha.get("Inicio")
                    fin = cancha.get("Fin")

                    if inicio and fin:
                        inicio_min = hora_a_minutos(inicio)
                        fin_min = hora_a_minutos(fin)

                        cancha["horarios_validos"] = [
                            h for h in HORARIOS
                            if inicio_min <= hora_a_minutos(h) < fin_min
                        ]
                    else:
                        cancha["horarios_validos"] = []

                return render_template(
                    'reservar.html',
                    canchas=canchas
                )
            diRequestReservar={}           
            getRequet(diRequestReservar)   
            upload_file(diRequestReservar)
            session['cancha_reservada'] = diRequestReservar
            id_usuario = session.get('id_usuario','')
            session['id_cancha_reservada'] = IdCanchaxNombre(diRequestReservar.get('nombre_cancha'))
            insertarCanchaReservada(diRequestReservar,id_usuario,session.get('id_cancha_reservada'))
            return redirect('/pagina_pago')
        return redirect('/login')
    
    
    @app.route('/unirse', methods=['POST','GET'])
    def unirse():
        if haySesion():
            if 'reservas_unidas' not in session:
                session['reservas_unidas'] = []
            if request.method == 'GET':
                canchasReservadas = buscarCanchasReservadas()
                return render_template('unirse.html', canchasReservadas=canchasReservadas)
            diRequestUnirse = {}           
            getRequet(diRequestUnirse)   
            nombre_cancha = diRequestUnirse.get('NombreCancha')
            id_reserva_raw = diRequestUnirse.get('id_reserva')
            if id_reserva_raw:
                id_reserva = int(id_reserva_raw)
                if id_reserva in session['reservas_unidas']:
                    bajarUsuarioUnido(diRequestUnirse, nombre_cancha)
                    lista = session['reservas_unidas']
                    lista.remove(id_reserva)
                    session['reservas_unidas'] = lista
                else:
                    insertarUsuarioUnido(diRequestUnirse, nombre_cancha)
                    lista = session['reservas_unidas']
                    lista.append(id_reserva)
                    session['reservas_unidas'] = lista
                session.modified = True 
            return redirect('/unirse')
        return redirect('/login')

    @app.route("/logout")
    def logout():  
        ''' Info: 
        Cierra la sesión.
        retorna la redirección a la pagina home   
        ''' 
        cerrarSesion()     
        return redirect('/')
