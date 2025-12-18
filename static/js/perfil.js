const imagen = document.getElementById("avatarInput");
const preview = document.getElementById("avatarPreview");

imagen.addEventListener("change", function () {
    const file = this.files[0];

    if (!file) return;

    if (!file.type.startsWith("image/")) {
        alert("Solo se permiten imágenes");
        this.value = "";
        return;
    }

    const reader = new FileReader();

    reader.onload = function (e) {
        preview.src = e.target.result;
    };

    reader.readAsDataURL(file);
});