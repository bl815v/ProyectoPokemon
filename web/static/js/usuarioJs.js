document.addEventListener('DOMContentLoaded', (event) => {
    const botonSalir = document.getElementById('boton_salir');
    botonSalir.addEventListener('click', () => {
        window.location.href = '/';
    });
});