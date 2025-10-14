const btnUnirse = document.getElementById('btn-unirse');
function agregarJugador (event){
    const fila = event.target.closest('tr');
    const cantidad = fila.querySelector('.cantJugadores');
    const valor = parseInt(cantidad.innerText);
    let cantidadJugadores = valor;
    const unirse = getElementById('btn-unirse');

    if (0 <= cantidadJugadores <= valor){
    valor ++;
    cantidad.innerText = `${valor}/22`;
    }
}

btnUnirse.addEventListener('click', agregarJugador);
