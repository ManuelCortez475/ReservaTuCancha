// ===== Nordelta =====
const fechaNordelta = document.getElementById("fechaNordelta");
const horaNordelta  = document.getElementById("horaNordelta");
const btnNordelta   = document.getElementById("btnNordelta");
const errorNordelta = document.getElementById("errorNordelta");

function validarNordelta(e) {
  const sinFecha = fechaNordelta.value === "";
  const horaSinSeleccion = horaNordelta.selectedIndex === 0;
  if (sinFecha || horaSinSeleccion) {
    e.preventDefault();
    errorNordelta.textContent = "⚠️ Debes elegir fecha y horario para Nordelta.";
  } else {
    errorNordelta.textContent = "";
  }
}
btnNordelta && btnNordelta.addEventListener("click", validarNordelta);


// ===== Beccar =====
const fechaBeccar = document.getElementById("fechaBeccar");
const horaBeccar  = document.getElementById("horaBeccar");
const btnBeccar   = document.getElementById("btnBeccar");
const linkBeccar  = document.getElementById("linkBeccar");
const errorBeccar = document.getElementById("errorBeccar");

function validarBeccar(e) {
  const sinFecha = fechaBeccar.value === "";
  const horaSinSeleccion = horaBeccar.selectedIndex === 0;
  if (sinFecha || horaSinSeleccion) {
    e.preventDefault();
    errorBeccar.textContent = "⚠️ Debes elegir fecha y horario para Beccar.";
  } else {
    errorBeccar.textContent = "";
  }
}
btnBeccar && btnBeccar.addEventListener("click", validarBeccar);
linkBeccar && linkBeccar.addEventListener("click", validarBeccar);


// ===== Benavidez =====
const fechaBenavidez = document.getElementById("fechaBenavidez");
const horaBenavidez  = document.getElementById("horaBenavidez");
const btnBenavidez   = document.getElementById("btnBenavidez");
const errorBenavidez = document.getElementById("errorBenavidez");

function validarBenavidez(e) {
  const sinFecha = fechaBenavidez.value === "";
  const horaSinSeleccion = horaBenavidez.selectedIndex === 0;
  if (sinFecha || horaSinSeleccion) {
    e.preventDefault();
    errorBenavidez.textContent = "⚠️ Debes elegir fecha y horario para Benavidez.";
  } else {
    errorBenavidez.textContent = "";
  }
}
btnBenavidez && btnBenavidez.addEventListener("click", validarBenavidez);