const form = document.getElementById("registroForm");
const password = document.getElementById("password");
const errorPassword = document.getElementById("errorPassword");
const confirmPassword = document.getElementById("confirmPassword");
const error = document.getElementById("errorComparativo");
const email = document.getElementById("email");
const errorMail = document.getElementById("errorMail");

function comparandoPasswordARegistrar(e) {
    if (password.value !== confirmPassword.value) {
        e.preventDefault();
        error.textContent = "Las contraseñas no coinciden";
    } 
    else {
        error.textContent = "";
    }
}
function requisitosPassword(event) {
  event.preventDefault();
  const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;

  /*
  Explicación del regex:
  (?=.*[a-z]) → al menos una minúscula
  (?=.*[A-Z]) → al menos una mayúscula
  (?=.*\d) → al menos un número
  (?=.*[\W_]) → al menos un carácter especial (no alfanumérico)
  .{8,} → mínimo 8 caracteres de longitud
  */

  if (regex.test(password.value)) {
    errorPassword.textContent = "Contraseña válida";
    errorPassword.style.color = "green";
  } else {
    errorPassword.textContent = "Debe tener al menos una mayúscula, una minúscula, un número, un carácter especial y 8 caracteres.";
    errorPassword.style.color = "red";
  }
};
function validandoFormatoMail(event) {
  event.preventDefault(); 
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

  if (regex.test(email.value)) {
    errorMail.textContent = "Correo válido ";
    errorMail.style.color = "green";
  } else {
    errorMail.textContent = "El correo no está bien formado. Ejemplo: usuario@dominio.com.ar";
    errorMail.style.color = "red";
  }
};

form.addEventListener("submit", comparandoPasswordARegistrar);
form.addEventListener("submit", requisitosPassword);
form.addEventListener("submit", validandoFormatoMail);


function eleccion(event) {
  const categoria_select = document.getElementById('.categoria');
  const categoria = categoria_select.value;
  if (categoria === 'admin'){

  }

}