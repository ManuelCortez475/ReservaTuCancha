const btnUnirse = document.querySelectorAll('.btn-unirse');
const btncancelar = document.querySelectorAll('.btn-cancelar');

function agregarJugador(event) {
    const boton = event.target;
    const fila = boton.closest('tr');
    const privacidad = fila.querySelector('.Estado').innerText.trim();
    const claveReal = boton.getAttribute('data-pass'); 
    

    if (privacidad === 'Privada') {
        const claveIngresada = prompt("Cancha privada. Contraseña:");

        if (claveIngresada === null || claveIngresada !== claveReal) {
            alert("❌ Contraseña incorrecta o acción cancelada.");
            event.preventDefault();
            return;
        }
    }
    
    const cantidadJug = fila.querySelector('.cantJugadores');
    const [cantidad_inicial, maximo] = cantidadJug.innerText.split('/');
    const cantidad = parseInt(cantidad_inicial);
    const max = parseInt(maximo);

    if (cantidad >= max) {
        alert("❌ La cancha ya está llena.");
        event.preventDefault(); 
        return;
    }
    
}

function bajarJugador(event) {
    const boton = event.target;
    const fila = boton.closest('tr'); 

    const cantidadElement = fila.querySelector('.cantJugadores');
    const [cantidad_inicial, maximo] = cantidadElement.innerText.split('/');

}

for (const button of btnUnirse) {
    button.addEventListener('click', agregarJugador);
}

for (const button of btncancelar) {
    button.addEventListener('click', bajarJugador);
}