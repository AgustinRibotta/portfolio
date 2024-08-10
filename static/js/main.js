document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('imageModal');

    modal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget; // Elemento que abrió el modal
        var imgSrc = button.getAttribute('data-img-src');
        var validationUrl = button.getAttribute('data-validation-url');
        var modalImage = modal.querySelector('#modalImage');
        var validateButton = modal.querySelector('#validateButton');

        // Actualizar imagen del modal
        modalImage.src = imgSrc;

        // Actualizar URL del botón de validación
        validateButton.href = validationUrl;
    });
});