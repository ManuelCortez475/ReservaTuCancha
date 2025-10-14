const form = document.getElementById("form");
const password = document.getElementById("pass");

function validandoFormatoMail(event) {
  const mail = document.getElementById("mail");
  const errorMail = document.getElementById("errorMail");

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

  if (regex.test(mail.value)) {
    errorMail.textContent = "Correo válido ";
    errorMail.style.color = "green";
  } else {
    errorMail.textContent = "El correo no está bien formado. Ejemplo: usuario@dominio.com.ar";
    errorMail.style.color = "red";
  }
};

form.addEventListener("submit", validandoFormatoMail);