const imagen = document.getElementById("avatarInput");
const preview = document.getElementById("avatarPreview");

function mostrarPreview(e){
    preview.src = e.target.result;
}
function Imagen (e) {
    const file = this.files[0];

    if (!file) return;

    if (!file.type.startsWith("image/")) {
        alert("Solo se permiten imágenes");
        this.value = "";
        return;
    }

    const reader = new FileReader();

    reader.onload = mostrarPreview;

    reader.readAsDataURL(file);
}
imagen.addEventListener("change", Imagen )