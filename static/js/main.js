document.addEventListener("DOMContentLoaded", function () {
    const burgerMenu = document.getElementById('burgerMenu');
    const navMenu = document.getElementById('navMenu');

    burgerMenu.addEventListener('click', function () {
        navMenu.classList.toggle('open');
    });
});


