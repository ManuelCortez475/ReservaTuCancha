
function cambiarAvatar(e) {
    const imagen = document.getElementById('avatarInput');
    var file = this.files[0];
    
    if (!file) {
        return;
    }

    if (!file.type.startsWith("image/")) {
        alert("Solo se permiten imágenes");
        this.value = "";
        return;
    }

    var reader = new FileReader();

    reader.onload = function () {
        document.getElementById("avatarPreview").src = reader.result;
    };

    reader.readAsDataURL(file);
}

imagen.addEventListener("change", cambiarAvatar)