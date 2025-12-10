const form = document.getElementById("registroForm");
const errorPassword = document.getElementById("errorPassword");
const error = document.getElementById("errorComparativo");

function comparandoPasswordARegistrar(e) {

  const password = document.getElementById("password");
  const confirmPassword = document.getElementById("confirmPassword");

  if (password.value !== confirmPassword.value) {
    return false;
  } 
  else {
    return true;
  }
}

function requisitosPassword(event) {

  const password = document.getElementById("password");
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;

  if (regex.test(password.value)) {
    return true;
  } else {
    return false;
  }
}

function validandoFormatoMail(event) { 
  
  const email = document.getElementById("email");
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (regex.test(email.value)) {
    return true;
  } else {
    return false;
  }
}

function validarFormulario(event) {
  
  event.preventDefault();
  
  const mailOk = validandoFormatoMail(event);
  const passOk = requisitosPassword(event);
  const passCompOk = comparandoPasswordARegistrar(event);
  const tipoUsuario = document.getElementById("categoria").value;

  errorMail.textContent = "";
  errorPassword.textContent = "";
  error.textContent = "";

  if (mailOk) {
    if (passOk) {
      if (passCompOk) {
        if (tipoUsuario === "usuario") {
          form.submit();
        }
        else if (tipoUsuario === "admin") {
          form.submit();
        }
      }
      else {
        error.textContent = "Las contraseñas no coinciden";
        error.style.color = "red";
      }
    }
    else {
      errorPassword.textContent = "Debe tener al menos una mayúscula, una minúscula, un número, un carácter especial y 8 caracteres.";
      errorPassword.style.color = "red";
    }
  }
  else {
    errorMail.textContent = "El correo no está bien formado. Ejemplo: usuario@dominio.com.ar";
    errorMail.style.color = "red";
  }
}

form.addEventListener("click", validarFormulario);

