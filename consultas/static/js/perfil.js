
const btnEditar = document.getElementById('btnEditar');
const partidos = document.getElementById('partidosJugados');
const goles = document.getElementById('goles');
const palos = document.getElementById('Palos');
const ganados = document.getElementById('partidosGanados');

let editandoStats = false;
let editandoInfoPersonal = false;

function editarStats() {
    if (!editandoStats) {
        partidos.innerHTML = '<strong>Partidos Jugados:</strong> <input type="number" id="inputPartidos" value="125">';
        goles.innerHTML = '<strong>Goles:</strong> <input type="number" id="inputGoles" value="13">';
        palos.innerHTML = '<strong>Palos:</strong> <input type="number" id="inputPalos" value="37">';
        ganados.innerHTML = '<strong>Partidos Ganados:</strong> <input type="number" id="inputGanados" value="78">';
        btnEditar.textContent = 'Guardar';
        editandoStats = true;
    } else {
        const inputPartidos = document.getElementById('inputPartidos').value;
        const inputGoles = document.getElementById('inputGoles').value;
        const inputPalos = document.getElementById('inputPalos').value;
        const inputGanados = document.getElementById('inputGanados').value;
        partidos.innerHTML = `<strong>Partidos Jugados:</strong> ${inputPartidos}`;
        goles.innerHTML = `<strong>Goles:</strong> ${inputGoles}`;
        palos.innerHTML = `<strong>Palos:</strong> ${inputPalos}`;
        ganados.innerHTML = `<strong>Partidos Ganados:</strong> ${inputGanados}`;
        btnEditar.textContent = 'Editar';
        editandoStats = false;
}}  

function editarInfoPersonal() {
    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const telefono = document.getElementById('telefono');
    const email = document.getElementById('email');
    const edad = document.getElementById('edad');
    const ciudad = document.getElementById('ciudad');
    if (!editandoInfoPersonal) {
        nombre.innerHTML = '<strong>Partidos Jugados:</strong> <input type="number" id="inputPartidos" value="125">';
        goles.innerHTML = '<strong>Goles:</strong> <input type="number" id="inputGoles" value="13">';
        palos.innerHTML = '<strong>Palos:</strong> <input type="number" id="inputPalos" value="37">';
        ganados.innerHTML = '<strong>Partidos Ganados:</strong> <input type="number" id="inputGanados" value="78">';
        btnEditar.textContent = 'Guardar';
        editando = true;
    } else {
        const inputPartidos = document.getElementById('inputPartidos').value;
        const inputGoles = document.getElementById('inputGoles').value;
        const inputPalos = document.getElementById('inputPalos').value;
        const inputGanados = document.getElementById('inputGanados').value;
        partidos.innerHTML = `<strong>Partidos Jugados:</strong> ${inputPartidos}`;
        goles.innerHTML = `<strong>Goles:</strong> ${inputGoles}`;
        palos.innerHTML = `<strong>Palos:</strong> ${inputPalos}`;
        ganados.innerHTML = `<strong>Partidos Ganados:</strong> ${inputGanados}`;
        btnEditar.textContent = 'Editar';
        editando = false;
}}  
btnEditar.addEventListener('click', editarStats);