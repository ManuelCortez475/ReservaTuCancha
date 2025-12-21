const btnPublicar1 = document.getElementById('btnPublicar1');
const btnAgregar = document.getElementById('btnAgregar');
const form = document.getElementById('form')


function crearFilaNueva() {
    const tabla = document.getElementById('tableCanchas');
    const rowCount = tabla.querySelectorAll('tr').length + 1;
    const nuevaFila = document.createElement('tr');
    
    nuevaFila.innerHTML = `
    <form id='form' method="post" action="/reservaAdmin">
    <table class="Tabla-Principal">
        <td>
        
            <input name='NombreCancha${rowCount}' type="text" id="nombre${rowCount}" placeholder="Name">
        </td>
        <td><input name='UbicacionCancha${rowCount}' type="text" id="ubicacion${rowCount}" placeholder="Location"></td>
        <td><input name='CantidadJug${rowCount}' type="number" id="cantJug${rowCount}" placeholder="N°"></td>
        <td>
            <input type="date" name="Fecha"><br>
            <label for="start${rowCount}">Desde:</label>
            <input type="time" id="start${rowCount}" name="start${rowCount}" required>
            <label for="end${rowCount}">Hasta:</label>
            <input type="time" id="end${rowCount}" name="end${rowCount}" required>
        </td>
        <td class="estado">
            <label><input class="estado" type="radio" name="Estado${rowCount}" value="r"> Reservada</label><br>
            <label><input class="estado" type="radio" name="Estado${rowCount}" value="h"> Habilitada</label><br>
            <label><input class="estado" type="radio" name="Estado${rowCount}" value="i"> Inhabilitada</label>
        </td>
        <td>
            <label><input type="number" name="Precio${rowCount}"></label><br>
        </td>
        <td>
            <button type="submit" id="btnPublicar${rowCount}" name='btnPublicar${rowCount}' class="btnPublicar1">Publicar</button>
            <p class="errorCampos" id="errorCampos${rowCount}"></p>
        </form>
        </td>
    `;
    const filaAgregar = btnAgregar.closest('tr');
    tabla.insertBefore(nuevaFila, filaAgregar);
    const btnPublicar= nuevaFila.querySelector('.btnPublicar1')
    btnPublicar.addEventListener('click', verificarCamposCompletos);
}

function estadosSeleccionados(radios) {
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            return true;
        }
    }
    return false;
}

function verificarCamposCompletos(e) {
    
    
    const boton = e.target;
    const fila = boton.closest('tr');
    const inputsTexto = fila.querySelectorAll('input[type="text"]');
    const nombre = fila.querySelector('input[type="text"]').value.trim();
    const ubicacion = fila.querySelector('input[placeholder="Location"]').value.trim();
    const cantJug = fila.querySelector('input[type="number"]').value.trim();
    const fecha = fila.querySelector('input[type="date"]').value;
    const horaInicio = fila.querySelector('input[name^="start"]').value;
    const horaFin = fila.querySelector('input[name^="end"]').value;
    const radios = fila.querySelectorAll('input[type="radio"]');
    const error = fila.querySelector('.errorCampos');

    const radiosOK = estadosSeleccionados(radios);

    if (nombre === "" || ubicacion === "" || cantJug === "" || fecha === "" || horaInicio === "" || horaFin === "" || !radiosOK) {
        e.preventDefault();
        error.textContent = "Todos los campos deben estar completos";
        error.style.color = "red";
    } else {
        error.textContent = "Cancha agregada con éxito";
        error.style.color = "green";
    }
}

btnAgregar.addEventListener('click', crearFilaNueva);
form.addEventListener('submit', verificarCamposCompletos);