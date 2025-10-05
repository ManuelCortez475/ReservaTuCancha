
const btnAgregar = document.getElementById('btnAgregar');
const tabla = document.getElementById('tableCanchas');


function crearFilaNueva() {
    const rowCount = tabla.querySelectorAll('tr').length + 1;
    const nuevaFila = document.createElement('tr');

    nuevaFila.innerHTML = `
        <td><input type="text" placeholder="Name"></td>
        <td><input type="text" placeholder="Location"></td>
        <td><input type="number" placeholder="N°"></td>
        <td>
            <input type="date" name="Fecha"><br>
            <label for="start${rowCount}">Desde:</label>
            <input type="time" id="start${rowCount}" name="start${rowCount}" required>
            <label for="end${rowCount}">Hasta:</label>
            <input type="time" id="end${rowCount}" name="end${rowCount}" required>
        </td>
        <td>
            <label><input type="radio" name="Estado${rowCount}" value="r"> Reservada</label><br>
            <label><input type="radio" name="Estado${rowCount}" value="h"> Habilitada</label><br>
            <label><input type="radio" name="Estado${rowCount}" value="i"> Inhabilitada</label>
        </td>
        <td><button class="btn-reservar">Publicar</button></td>
    `;
    tabla.insertBefore(nuevaFila, tabla.lastElementChild);
}

btnAgregar.addEventListener('click', crearFilaNueva);