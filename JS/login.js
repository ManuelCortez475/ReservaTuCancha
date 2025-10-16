const form = document.getElementById("form");


function validandoFormatoMail(event) {
  
  const mail = document.getElementById("mail");
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  /*
  Explicación del regex:
  ^ → inicio de la cadena
  [a-zA-Z0-9._%+-]+ → permite letras, números y algunos símbolos antes del @
  @ → debe tener un arroba
  [a-zA-Z0-9.-]+ → dominio (por ejemplo: gmail, outlook, etc.)
  \. → un punto literal
  [a-zA-Z]{2,} → extensión (por ejemplo: com, ar, org)
  $ → final de la cadena
  */

  if (regex.test(mail.value)) {
    return true;
  } else {
    return false;
  }
};

function validarCamposVacios(event) {

  const mail = document.getElementById("mail");
  const password = document.getElementById("pass");

  if (mail.value === "" || password.value === "") {
    return false;
  } else {

    return true;
  }
}

function validarErrores(event) {
  event.preventDefault();
  const mailOk = validandoFormatoMail(event);
  const camposOk = validarCamposVacios(event); 
  errorMail.textContent = "";
  errorPass.textContent = "";

  if (mailOk) {
    if (camposOk) {
      form.submit();
    }
    else {
      errorPass.textContent = "La contraseña no puede estar vacía";
      errorPass.style.color = "red";
    }
  }
  else {
    errorMail.textContent = "El correo no está bien formado. Ejemplo: usuario@dominio.com.ar";
    errorMail.style.color = "red";
  }
}

form.addEventListener("submit", validarErrores);