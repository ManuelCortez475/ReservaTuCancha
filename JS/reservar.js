// ===== Nordelta =====
const fechaNordelta = document.getElementById("fechaNordelta");
const horaNordelta  = document.getElementById("horaNordelta");
const btnNordelta   = document.getElementById("btnNordelta");

function validarNordelta(e) {
  if (fechaNordelta.value === "" || horaNordelta.value === "Seleccionar...") {
    e.preventDefault();
    alert("Debes elegir fecha y horario para Nordelta.");
  }
}
btnNordelta.addEventListener("click", validarNordelta);


// ===== Beccar =====
const fechaBeccar = document.getElementById("fechaBeccar");
const horaBeccar  = document.getElementById("horaBeccar");
const btnBeccar   = document.getElementById("btnBeccar");

function validarBeccar(e) {
  if (fechaBeccar.value === "" || horaBeccar.value === "Seleccionar...") {
    e.preventDefault();
    alert("Debes elegir fecha y horario para Beccar.");
  }
}
btnBeccar.addEventListener("click", validarBeccar);


// ===== Benavidez =====
const fechaBenavidez = document.getElementById("fechaBenavidez");
const horaBenavidez  = document.getElementById("horaBenavidez");
const btnBenavidez   = document.getElementById("btnBenavidez");

function validarBenavidez(e) {
  if (fechaBenavidez.value === "" || horaBenavidez.value === "Seleccionar...") {
    e.preventDefault();
    alert("Debes elegir fecha y horario para Benavidez.");
  }
}
btnBenavidez.addEventListener("click", validarBenavidez);