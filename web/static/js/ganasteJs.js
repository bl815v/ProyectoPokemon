document.addEventListener('DOMContentLoaded', (event) => {
    const botonRegresar = document.getElementById('boton_regresar');
    botonRegresar.addEventListener('click', () => {
        window.location.href = '/usuario';
    });
});