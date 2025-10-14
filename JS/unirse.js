const btnUnirse = document.querySelectorAll('.btn-unirse');
const CONTRASENA_CORRECTA = 'reserva123';

function agregarJugador(event) {
  const fila = event.target.closest('tr');
  const estado = fila.querySelector('.Estado');
  const estado_actual = estado ? estado.innerText.trim() : '';
  const cantidadElement = fila.querySelector('.cantJugadores');
  const tamaño_cancha = cantidadElement ? cantidadElement.innerText : '0/0';
  const [cantidad_inicial, maximo] = tamaño_cancha.split('/').map(s => s.trim());
  let cantidad = parseInt(cantidad_inicial) || 0;
  const max = parseInt(maximo) || 0;

  const errorSpan = fila.querySelector('.errorContraseña');
  if (errorSpan) errorSpan.textContent = '';

  if (estado_actual === 'Privada') {
    const input = fila.querySelector('.input-contraseña');
    const contraseña_ingresada = input ? input.value.trim() : '';

    if (!contraseña_ingresada) {
      if (errorSpan) errorSpan.textContent = "Ingresá la contraseña antes de unirte.";
      return;
    }

    if (contraseña_ingresada !== CONTRASENA_CORRECTA) {
      if (errorSpan) errorSpan.textContent = "Contraseña incorrecta. No puedes unirte.";
      return;
    }
  }


  if (cantidad < max) {
    cantidad++;
    if (cantidadElement) cantidadElement.innerText = `${cantidad}/${max}`;

    if (cantidad === max) {
      event.target.innerText = 'Cancha Llena';
      event.target.disabled = true;
    }
  } else {
    if (errorSpan) errorSpan.textContent = "La cancha ya está llena.";
  }
}


btnUnirse.forEach(button => {
  button.addEventListener('click', agregarJugador);
});
