const btnUnirse = document.querySelectorAll('.btn-unirse');
const btn_verjugadores = document.querySelectorAll('.btn-verjugadores');
const CONTRASEÑA_CORRECTA = 'reserva123'; 

function agregarJugador(event) {
    const fila = event.target.closest('tr');
    const estadoElement = fila.querySelector('.Estado');
    const estado_actual = estadoElement.innerText.trim();
    
    if (estado_actual === 'Privada') {
        const contrasena_ingresada = prompt("Esta cancha es privada. Ingresá la contraseña:");

        if (contrasena_ingresada !== CONTRASEÑA_CORRECTA) {
            alert("❌ Contraseña incorrecta. No podés unirte.");
            event.preventDefault(); 
            return;
        }
    }
    const cantidadElement = fila.querySelector('.cantJugadores');
    const [cantidad_inicial, maximo] = cantidadElement.innerText.split('/');
    const cantidad = parseInt(cantidad_inicial);
    const max = parseInt(maximo);

    
    if (cantidad >= max) {
        alert("❌ La cancha ya está llena.");
        event.preventDefault(); 
        return;
    }


}

for (const button of btnUnirse) {
    button.addEventListener('click', agregarJugador);
}

for (const button of btn_verjugadores) {
    button.addEventListener('click', agregarJugador);
}