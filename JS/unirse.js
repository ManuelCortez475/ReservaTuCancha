const btnUnirse = document.querySelectorAll('.btn-unirse');
const CONTRASENA_CORRECTA = 'reserva123'; 

function agregarJugador (event){
    const fila = event.target.closest('tr');
    const estado = fila.querySelector('.Estado');
    const estado_actual = estado.innerText.trim();
    const cantidadElement = fila.querySelector('.cantJugadores');
    const tamaño_cancha = cantidadElement.innerText;
    const [cantidad_inicial, maximo] = tamaño_cancha.split('/');
    let cantidad = parseInt(cantidad_inicial);
    const max = parseInt(maximo);
    
    if (estado_actual === 'Privada'){
        const contrasena_ingresada = prompt("Esta cancha es privada. Por favor, ingresa la contraseña:");

        if (contrasena_ingresada !== CONTRASENA_CORRECTA) {
            alert("Contraseña incorrecta o acción cancelada. No puedes unirte.");
            return;
        }
    }
    if (cantidad < max){
        cantidad++;
        cantidadElement.innerText = `${cantidad}/${max}`;
        
        if (cantidad === max) {
            event.target.innerText = 'Cancha Llena';
            event.target.disabled = true; 
        }
    }
}

btnUnirse.forEach(button => {
    button.addEventListener('click', agregarJugador);
});