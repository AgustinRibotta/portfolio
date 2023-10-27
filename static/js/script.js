document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('.fade-in');

    const options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2, // Porcentaje visible requerido para activar la animación
    };

    const observer = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Evita que se agregue 'active' repetidamente
            }
        });
    }, options);

    sections.forEach(section => {
        observer.observe(section);
    });
});

