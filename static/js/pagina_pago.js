const form = document.getElementById("registroForm");

const errorCVU = document.getElementById("errorCVU");

function validarLongitudCVU(e) {
    const CVU = document.getElementById("cvu");
    if (CVU.value.length !== 22){
        errorCVU.textContent = "El CVU debe tener 22 caracteres";
        return false
    }
    else {
        errorCVU.textContent = "";
        return true
    }
}
function soloNumerosCVU(e) {
    const CVU = document.getElementById("cvu");
    const regex = /^[0-9]+$/;
    if (!regex.test(CVU.value)) {
      errorCVU.textContent = "El CVU debe contener solo números.";
      return false;
    } else {
      errorCVU.textContent = "";
      return true;
    }
  }

function validarCamposVacios(event) {

  const nombre = document.getElementById("nombre");
  const cvu = document.getElementById("cvu");
  const comprobante = document.getElementById('comprobante');
  const CamposVacios = document.getElementById('CamposVacios');

  if (nombre.value === "" || cvu.value === "" || comprobante.value === "") {
    CamposVacios.textContent = 'Todos los campos deben estar completos'
    return false;
  } else {
    return true;
  }
}

function corregirCVU(e){
  e.preventDefault()
  if (validarCamposVacios(e) && soloNumerosCVU(e) && validarLongitudCVU(e)){
    form.submit()
  }
  

}

form.addEventListener("submit",corregirCVU)