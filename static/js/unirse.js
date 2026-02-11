const btnUnirse = document.querySelectorAll('.btn-unirse');
// Separamos los botones: el de ver jugadores no debería sumar gente
const btn_verjugadores = document.querySelectorAll('.btn-verjugadores');

function agregarJugador(event) {
    const boton = event.target;
    const fila = boton.closest('tr');
    const privacidad = fila.querySelector('.Estado').innerText.trim();
    const claveReal = boton.getAttribute('data-pass'); //

    // 1. VALIDACIÓN DE CONTRASEÑA
    if (privacidad === 'Privada') {
        const claveIngresada = prompt("Cancha privada. Contraseña:");

        if (claveIngresada === null || claveIngresada !== claveReal) {
            alert("❌ Contraseña incorrecta o acción cancelada.");
            event.preventDefault(); // Frena el envío a Python
            return;
        }
    }

    // 2. VALIDACIÓN DE CUPO (Ahora adentro de la función)
    const cantidadElement = fila.querySelector('.cantJugadores');
    const [cantidad_inicial, maximo] = cantidadElement.innerText.split('/');
    const cantidad = parseInt(cantidad_inicial);
    const max = parseInt(maximo);

    if (cantidad >= max) {
        alert("❌ La cancha ya está llena.");
        event.preventDefault(); // Frena el envío a Python
        return;
    }
    
    // Si llegó acá, el JS no frena nada y el formulario viaja al POST de /unirse
}

// 3. ASIGNACIÓN CORRECTA
for (const button of btnUnirse) {
    button.addEventListener('click', agregarJugador);
}

// Para ver jugadores no usamos agregarJugador, porque sino te pediría clave para solo mirar
for (const button of btn_verjugadores) {
    button.addEventListener('click', function(e) {
        console.log("Abriendo lista de jugadores...");
    });
}