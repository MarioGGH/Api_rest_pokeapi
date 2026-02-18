const toggle = document.getElementById('shiny-toggle');
const sprite = document.getElementById('pokemon-sprite');

toggle.addEventListener('click', () => {
    const isShiny = sprite.src === sprite.dataset.shiny;
    sprite.src = isShiny ? sprite.dataset.normal : sprite.dataset.shiny;

    toggle.classList.toggle('active');
});