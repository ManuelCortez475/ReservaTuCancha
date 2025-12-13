const form = document.getElementById("registroForm");
const CVU = document.getElementById("cvu");
const errorCVU = document.getElementById("errorCVU");

function validarLongitudCVU(e) {
    if (CVU.value.length !== 22){
        e.preventDefault();
        errorCVU.textContent = "El CVU debe tener 22 caracteres";
    }
    else {
        errorCVU.textContent = "";
    }
}
function soloNumerosCVU(e) {
    const regex = /^[0-9]+$/;
    if (!regex.test(CVU.value)) {
      e.preventDefault();
      errorCVU.textContent = "El CVU debe contener solo números.";
    } else {
      errorCVU.textContent = "";
    }
  };

form.addEventListener("submit", validarLongitudCVU);
form.addEventListener("submit", soloNumerosCVU);