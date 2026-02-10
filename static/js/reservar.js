const tbody = document.querySelector('.Table-Body');

function cambioPrivacidad(event) {
const target = event.target;
if (target.classList.contains('tipo-reserva')) {
    const fila = target.closest('tr');
    const claveBox = fila.querySelector('.clave'); 
    if (target.value === 'Privada') {
        claveBox.style.display = 'inline-block';
    } else {
        claveBox.style.display = 'none';
    }
}
}

function manejarReserva(event) {
const target = event.target;
const boton = target.closest('button');
if (!boton || boton.classList.contains('btnConfirmarClave')) return;
const fila = target.closest('tr');
const nombre = fila.querySelector('.NombreCancha').innerText.trim();
const precio = fila.querySelector('.PrecioCancha').innerText.trim();
const fechaInput = fila.querySelector('.fechaInput');
const horaSelect = fila.querySelector('.horaSelect');
const privacidadSelect = fila.querySelector('.tipo-reserva');
const inputClave = fila.querySelector('.inputClave');
const estado = fila.querySelector('.EstadoLabel').innerText.trim().toLowerCase();
const errorSpan = fila.querySelector('.error-text');

if (estado !== 'habilitada') {
    event.preventDefault();
    return;
}

if (!fechaInput.value || horaSelect.selectedIndex === 0) {
    event.preventDefault();
    if (errorSpan) {
        errorSpan.innerText = `⚠️ Elegí fecha y hora para ${nombre}.`;
        errorSpan.style.color = "red";
    }
    return;
}

let clavePrivada = "";
if (privacidadSelect.value === 'Privada') {
if (!inputClave.value.trim()) {
        event.preventDefault();
        if (errorSpan) {
            errorSpan.innerText = "⚠️ La reserva privada necesita una contraseña.";
            errorSpan.style.color = "orange";
        }
        return;
    }
    clavePrivada = inputClave.value.trim();
}
}
if (tbody) {
tbody.addEventListener('click', manejarReserva);
tbody.addEventListener('change', cambioPrivacidad);
}