$(document).ready(function () {
    // Agregar un efecto de brillo al pasar el mouse sobre los botones
    $('.btn-primary').hover(function () {
        $(this).toggleClass('btn-secondary');
    });
});


/* scripts.js */
document.addEventListener("DOMContentLoaded", function () {
    const filterButtons = document.querySelectorAll(".filter-button");
    const projectCards = document.querySelectorAll(".project-card");

    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
            filterButtons.forEach((btn) => btn.classList.remove("active-filter"));
            button.classList.add("active-filter");

            const filterValue = button.dataset.filter;

            projectCards.forEach((card) => {
                card.classList.add("hidden-project");

                if (card.classList.contains(filterValue)) {
                    card.classList.remove("hidden-project");
                }
            });
        });
    });
});


// JavaScript code in filter.js

// Función para filtrar proyectos por categoría
function filterProjects(category) {
    // Obtener todos los elementos de proyecto
    const projectElements = document.querySelectorAll('.project-card');

    projectElements.forEach((element) => {
        const categories = element.getAttribute('data-categories').split(' ');

        if (category === 'todos' || categories.includes(category)) {
            element.style.display = 'block';
        } else {
            element.style.display = 'none';
        }
    });
}

// Función para resaltar el botón de filtro seleccionado
function highlightButton(button) {
    const filterButtons = document.querySelectorAll('.btn-filter');

    filterButtons.forEach((btn) => {
        btn.classList.remove('active');
    });

    button.classList.add('active');
}

// Asignar eventos a los botones de filtro
document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.btn-filter');

    filterButtons.forEach((button) => {
        button.addEventListener('click', (e) => {
            const category = e.target.getAttribute('data-filter');
            filterProjects(category);
            highlightButton(e.target);
        });
    });
});

$(document).ready(function () {
    $('.menu-link').on('click', function (e) {
        e.preventDefault();
        const target = $(this).attr('href');
        const offset = $(target).offset().top - 80;
        $('html, body').animate({
            scrollTop: offset
        }, 500);
    });
});