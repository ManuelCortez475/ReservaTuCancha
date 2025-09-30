const form = document.getElementById("registroForm");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const error = document.getElementById("error");

function comparandoPasswordARegistrar(e) {
    if (password.value !== confirmPassword.value) {
        e.preventDefault();
        error.textContent = "Las contraseñas no coinciden";
    } 
    else {
        error.textContent = "";
    }
}

form.addEventListener("submit", comparandoPasswordARegistrar);
