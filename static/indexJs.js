
document.addEventListener("DOMContentLoaded", function() {
    var damageBtn = document.querySelector(".damage-btn");
    var pokemonGif = document.getElementById("pokemon-gif");

    damageBtn.addEventListener("click", function() {
        pokemonGif.classList.add("parpadeo-gif");

        setTimeout(function() {
            pokemonGif.classList.remove("parpadeo-gif");
        }, 1800);
    });
});