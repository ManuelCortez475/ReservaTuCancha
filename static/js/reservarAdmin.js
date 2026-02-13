const btnPublicar1 = document.getElementById('btnPublicar1');
const btnAgregar = document.getElementById('btnAgregar');
const form = document.getElementById('form')


function crearFilaNueva() {
    const tabla = document.getElementById('tableCanchas');
    const rowCount = tabla.querySelectorAll('tr').length + 1;
    const nuevaFila = document.createElement('tr');
    
    nuevaFila.innerHTML = `
        <td>
            <input name='NombreCancha${rowCount}' type="text" id="nombre${rowCount}" placeholder="Name">
        </td>
        <td><input name='UbicacionCancha${rowCount}' type="text" id="ubicacion${rowCount}" placeholder="Location"></td>
        <td><input name='CantidadJug${rowCount}' type="number" id="cantJug${rowCount}" placeholder="N°"></td>
        <td>
            <div class="grupo-fechas">
                <div class="fila">
                    <label>Desde</label>
                    <input type="date" name="fecha_desde${rowCount}">
                </div>

                <div class="fila">
                    <label>Hasta</label>
                    <input type="date" name="fecha_hasta${rowCount}">
                </div>

                <div class="fila">
                    <label>Inicio</label>
                    <select id="start${rowCount}" name="Inicio${rowCount}" required>
                        <option disabled selected>Seleccionar...</option>
                        <option value="9:00">9:00</option>
                        <option value="10:30">10:30</option>
                        <option value="12:00">12:00</option>
                        <option value="13:30">13:30</option>
                        <option value="15:00">15:00</option>
                        <option value="16:30">16:30</option>
                        <option value="18:00">18:00</option>
                        <option value="19:30">19:30</option>
                        <option value="21:00">21:00</option>
                    </select>
                </div>

                <div class="fila">
                    <label>Fin</label>
                    <select id="end${rowCount}" name="Fin${rowCount}" required>
                        <option disabled selected>Seleccionar...</option>
                        <option value="9:00">9:00</option>
                        <option value="10:30">10:30</option>
                        <option value="12:00">12:00</option>
                        <option value="13:30">13:30</option>
                        <option value="15:00">15:00</option>
                        <option value="16:30">16:30</option>
                        <option value="18:00">18:00</option>
                        <option value="19:30">19:30</option>
                        <option value="21:00">21:00</option>
                    </select>
                </div>
            </div>
        </td>
        <td>
            <div class="estado-grupo">
                <label><input class="estado" type="radio" name="Estado${rowCount}" value="reservada"> reservada</label><br>
                <label><input class="estado" type="radio" name="Estado${rowCount}" value="habilitada"> habilitada</label><br>
                <label><input class="estado" type="radio" name="Estado${rowCount}" value="inhabilitada"> inhabilitada</label>
            </div>
        </td>
        <td>
            <label><input type="number" placeholder='Precio' name="Precio${rowCount}"></label><br>
        </td>
        <td>
            <button type="submit" id="btnPublicar${rowCount}" name='btnPublicar${rowCount}' class="btnPublicar1">Publicar</button>
            <p class="errorCampos" id="errorCampos${rowCount}"></p>
        </td>
    `;
    const filaAgregar = btnAgregar.closest('tr');
    tabla.insertBefore(nuevaFila, filaAgregar);
    const btnPublicar= nuevaFila.querySelector('.btnPublicar1');
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