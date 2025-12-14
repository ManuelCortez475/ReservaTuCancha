SHOW DATABASES;

USE usuario;

SHOW TABLES;

DESCRIBE perfil;

SELECT * FROM perfil ;
ALTER TABLE perfil AUTO_INCREMENT = 1;

INSERT INTO perfil (id, nombre, apellido, telefono, fecha_nacimiento, ciudad, descripcion, id_usuario) VALUES 
(NULL, "Sofía", "Rodríguez Fernández", 5491130000002, "2001-09-03", "Córdoba", "Extremo derecho — velocidad para desbordar, centros precisos y tirar diagonales al área.",1),
(NULL, "Joaquín", "Pérez Morales", 5491130000003, "1995-06-20", "Rosario", "Mediocampista defensivo — cortocircuito las jugadas, juego simple y salidas limpias.",2),
(NULL, "Valentina", "Gómez Castillo", 5491130000004, "2003-01-14", "Mar del Plata", "Interior izquierda — combinación en corto, llegada al área y buen remate desde afuera.",3),
(NULL, "Lucas", "Martínez Herrera", 5491130000005, "1992-11-30", "Mendoza", "Lateral derecho — subir por la banda, centros ofensivos y cubrir al defensor rival.",4),
(NULL, "Camila", "Núñez Silva", 5491130000006, "2000-07-08", "Salta", "Volante creativa — dirijo el ritmo, busco pases entre líneas y tiro pases filtrados.",5),
(NULL, "Mateo", "Ruiz Blanco", 5491130000007, "1999-02-25", "La Plata", "Segundo volante — enlace entre mediocampo y ataque, llegada al área y asistencia.",6),
(NULL, "Florencia", "Díaz Ortega", 5491130000008, "2004-12-05", "Tucumán", "Extremo izquierdo — regate corto, cambiar de ritmo y tirar centros al segundo palo.",7),
(NULL, "Nicolás", "Fernández Rojas", 5491130000009, "1996-08-17", "Neuquén", "Mediocentro — distribución, control del tempo y recuperación de balones.",8),
(NULL, "Agustina", "Méndez Paredes", 5491130000010, "2002-05-29", "Ushuaia", "Defensa central — liderazgo atrás, juego aéreo y salir jugando desde el fondo.",9);

SELECT FROM perfil WHERE id = 20;

UPDATE perfil SET ciudad = "Córdoba Capital" WHERE id = 5;

DELETE FROM reserva_cancha;  






DESCRIBE usuario;
SELECT * FROM usuario;
ALTER TABLE usuario AUTO_INCREMENT = 10;
INSERT INTO usuario (id,mail,contraseña,categoria) VALUES 
(NULL, "sofia.rodriguez@example.com", "DemoPwd#22", true),
(NULL, "joaquin.perez@example.com", "Sample123!A", true),
(NULL, "valentina.gomez@example.com", "PassDemo@33", true),
(NULL, "lucas.martinez@example.com", "Example!45aa", true),
(NULL, "camila.nunez@example.com", "MyTestPwd#6", true),
(NULL, "mateo.ruiz@example.com", "FakePass_77", true),
(NULL, "florencia.diaz@example.com", "Placeholder!8", true),
(NULL, "nicolas.fernandez@example.com", "Demo!Pass909", true),
(NULL, "agustina.mendez@example.com", "TempPwd*10", false);

DELETE FROM usuario WHERE id BETWEEN 18 AND 24;
INSERT INTO usuario (id,mail,contraseña,categoria) VALUES 
(NULL, "carlos.rodriguez@example.com", "DemoPwd#22", True);

SELECT
    perfil.nombre AS Nombre,
    perfil.apellido AS Apellido,
    usuario.mail AS Mail,
    usuario.contraseña AS Contraseña,
    usuario.categoria AS Rol,
    cancha.nombre AS Cancha_reservada,
    reserva_cancha.estado AS Estado_Reserva
    FROM usuario
    INNER JOIN perfil ON perfil.id = usuario.id_perfil 
    INNER JOIN reserva_cancha ON reserva_cancha.id_usuario = usuario.id
    INNER JOIN cancha ON cancha.id = reserva_cancha.id_cancha
    WHERE reserva_cancha.estado = "reservada";

 


DESCRIBE cancha

SELECT * FROM cancha;

ALTER TABLE cancha AUTO_INCREMENT = 1;

INSERT INTO cancha (id,nombre, estado, ubicacion, cant_jugadores, precio) VALUES
(NULL, "Cancha La Bombonera", "habilitada", "Buenos Aires", 11, 15000),
(NULL, "Cancha El Monumental", "inhabilitada", "Buenos Aires", 11, 18000),
(NULL, "Cancha Parque Norte", "habilitada", "Palermo", 11, 12000),
(NULL, "Cancha San Martín FC", "inhabilitada", "Rosario", 8, 10000),
(NULL, "Cancha El Campito", "habilitada", "Córdoba", 8, 8000),
(NULL, "Cancha Rivera Park", "habilitada", "Mar del Plata", 11, 11000),
(NULL, "Cancha Fútbol Total", "inhabilitada", "Mendoza", 11, 13000),
(NULL, "Cancha Los Halcones", "habilitada", "La Plata", 8, 9500),
(NULL, "Cancha Urban Soccer", "habilitada", "Recoleta", 11, 16000),
(NULL, "Cancha Deportivo Sur", "inhabilitada", "Lomas de Zamora", 11, 14000),
(NULL, "Cancha El Predio", "habilitada", "Villa Urquiza", 8, 9000),
(NULL, "Cancha Club Oeste", "inhabilitada", "Caballito", 11, 12500),
(NULL, "Cancha La 10", "habilitada", "San Justo", 11, 11000),
(NULL, "Cancha SportCenter", "habilitada", "Vicente López", 11, 17500),
(NULL, "Cancha FútbolManía", "inhabilitada", "Tigre", 11, 13000),
(NULL, "Cancha Los Amigos", "habilitada", "San Isidro", 8, 9500),
(NULL, "Cancha El Potrero", "habilitada", "Morón", 11, 10000),
(NULL, "Cancha Norte F5", "inhabilitada", "Belgrano", 5, 8500),
(NULL, "Cancha Sur F7", "habilitada", "Quilmes", 5, 9500),
(NULL, "Cancha Central Park", "inhabilitada", "Neuquén", 11, 12000),
(NULL, "Cancha Los Tigres", "habilitada", "Santa Fe", 11, 11000),
(NULL, "Cancha Barrio Unido", "habilitada", "Ramos Mejía", 11, 9000),
(NULL, "Cancha Club Este", "inhabilitada", "Avellaneda", 8, 9500),
(NULL, "Cancha Norte Soccer", "habilitada", "Saavedra", 11, 13000),
(NULL, "Cancha Deportivo Centro", "habilitada", "Lanús", 11, 14000),
(NULL, "Cancha 5 Estrellas", "inhabilitada", "CABA", 5, 10000),
(NULL, "Cancha Las Palmeras", "habilitada", "Bahía Blanca", 8, 11500),
(NULL, "Cancha Olímpica", "inhabilitada", "Tucumán", 11, 16000),
(NULL, "Cancha Los Leones", "habilitada", "Salta", 11, 12500),
(NULL, "Cancha San Pedro", "habilitada", "Posadas", 8, 9500);

ALTER TABLE cancha
ADD COLUMN fecha date AFTER nombre;
UPDATE cancha SET fecha = "2024-07-01" WHERE id BETWEEN 1 AND 15;
UPDATE cancha SET fecha = "2024-07-02" WHERE id BETWEEN 16 AND 30;
DELETE FROM cancha WHERE id BETWEEN 31 AND 60;

UPDATE cancha SET estado = "fuera de servicio" WHERE id IN (2,8);

SELECT 
    cancha.nombre AS Nombre_Cancha,
    cancha.ubicacion AS Ubicacion,
    cancha.cant_jugadores AS Cantidad_Jugadores,
    reserva_cancha.hora AS hora_reservada
    FROM cancha
    INNER JOIN reserva_cancha ON cancha.id = reserva_cancha.id_cancha
    WHERE reserva_cancha.estado = "reservada";

SELECT 
    usuario.id AS Usuario_que_reservo,
    perfil.telefono AS telefono_usuario,
    cancha.nombre AS Nombre_Cancha,
    cancha.precio AS Precio_Cancha,
    reserva_cancha.estado AS Estado_Reserva
    FROM cancha
    INNER JOIN reserva_cancha ON cancha.id = reserva_cancha.id_cancha
    INNER JOIN usuario ON reserva_cancha.id_usuario = usuario.id
    INNER JOIN perfil ON perfil.id = usuario.id_perfil;

SELECT * FROM cancha
order by cancha.precio asc;


DESCRIBE reserva_cancha;

SELECT * FROM reserva_cancha;

ALTER TABLE reserva_cancha AUTO_INCREMENT = 1;

INSERT INTO reserva_cancha (id, id_cancha,id_perfil,hora,comprobante_pago,estado ) VALUES
(NULL, 1, 1, "9:00 am", "comprobante1.jpg", ""),
(NULL, 2, 1, "10:30 am", "comprobante2.jpg", "reservada"),
(NULL, 3, 7, "12:00 pm", "comprobante3.jpg", "cancelada"),
(NULL, 4, 5, "1:30 pm", "comprobante4.jpg", "reservada"),
(NULL, 5, 3, "3:00 pm", "comprobante5.jpg", "");

UPDATE reserva_cancha SET estado = "pendiente" WHERE id IN (1,5)

UPDATE reserva_cancha SET id_cancha = 17 WHERE id = 3;

UPDATE reserva_cancha
INNER JOIN cancha ON reserva_cancha.id_cancha = cancha.id
SET reserva_cancha.fecha_reservada = cancha.fecha;

UPDATE reserva_cancha
INNER JOIN cancha ON reserva_cancha.id_cancha = cancha.id
SET reserva_cancha.precio = cancha.precio;

SELECT 
  reserva_cancha.id AS id_reserva,
  reserva_cancha.id_cancha,
  cancha.precio AS precio_cancha,
  reserva_cancha.estado AS estado_reserva
FROM reserva_cancha
INNER JOIN cancha ON reserva_cancha.id_cancha = cancha.id
WHERE reserva_cancha.estado = "reservada";




DESCRIBE cancha_para_unirse;

SELECT * FROM cancha_para_unirse;

ALTER TABLE cancha_para_unirse AUTO_INCREMENT = 1;

INSERT INTO cancha_para_unirse (id,id_perfil, id_reservar_cancha) VALUES
(NULL, 1, 1),
(NULL, 6, 3),
(NULL, 4, 4),
(NULL, 5, 1),
(NULL, 8, 5),
(NULL, 9, 3);


