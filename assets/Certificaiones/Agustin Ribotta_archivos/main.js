document.querySelectorAll('.card-body').forEach(card => {
    card.addEventListener('click', function () {
        const imgSrc = this.getAttribute('data-img-src');
        const modalImage = document.querySelector('#imageModal .modal-body img');
        modalImage.src = imgSrc;
    });
});