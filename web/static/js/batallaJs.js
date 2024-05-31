document.addEventListener('DOMContentLoaded', (event) => {
    const divBotones = document.querySelector('.div_botones');
    const contenidoOriginal = `
        <button type="button" id="boton_atacar" name="boton_atacar">Atacar</button>
        <button type="button" id="boton_mochila" name="boton_mochila">Mochila</button>
    `;
    
    divBotones.innerHTML = contenidoOriginal;

    function aplicarEstiloBoton(buttons) {
        buttons.forEach(button => {
            button.style.fontFamily = "Pixelify Sans, sans-serif";
            button.style.fontSize = "20px";
            button.style.padding = "20px";
            button.style.border = "none";
            button.style.backgroundColor = "#7700ff";
            button.style.color = "white";
            button.style.cursor = "pointer";
            button.style.transition = "background-color 0.3s ease";
            button.style.maxWidth = "500px";
            button.style.maxHeight = "80px";
            button.style.width = "100%";
            button.style.boxSizing = "border-box";
            button.style.textAlign = "center";
            button.style.borderRadius = "10px";

            button.addEventListener('mouseover', () => {
                button.style.backgroundColor = "#37006b";
            });

            button.addEventListener('mouseout', () => {
                button.style.backgroundColor = "#7700ff";
            });
        });
    }

    function configBotonesOriginales() {
        const botonAtacar = document.getElementById('boton_atacar');
        botonAtacar.addEventListener('click', opcionesAtaque);
        
        const botonMochila = document.getElementById('boton_mochila');
        botonMochila.addEventListener('click', opcionesMochila);
    }

    function opcionesAtaque() {
        divBotones.innerHTML = `
            <button type="button" id="boton_ataque1" name="boton_ataque1">ATAQUE 1</button>
            <button type="button" id="boton_ataque2" name="boton_ataque2">ATAQUE 2</button>
            <button type="button" id="boton_ataque3" name="boton_ataque3">ATAQUE 3</button>
            <button type="button" id="boton_ataque4" name="boton_ataque4">ATAQUE 4</button>
            <button type="button" id="boton_regresar" name="boton_regresar">Regresar</button>
        `;
        const botonesAtaque = divBotones.querySelectorAll('button');
        aplicarEstiloBoton(botonesAtaque);
        const botonRegresar = document.getElementById('boton_regresar');
        botonRegresar.addEventListener('click', () => {
            divBotones.innerHTML = contenidoOriginal;
            aplicarEstiloBoton(divBotones.querySelectorAll('button'));
            configBotonesOriginales();
        });
    }

    function opcionesMochila() {
        divBotones.innerHTML = `
            <button type="button" id="boton_objeto1" name="boton_objeto1">Objeto1</button>
            <button type="button" id="boton_objeto2" name="boton_objeto2">Objeto2</button>
            <button type="button" id="boton_objeto3" name="boton_objeto3">Objeto3</button>
            <button type="button" id="boton_objeto4" name="boton_objeto4">Objeto4</button>
            <button type="button" id="boton_objeto5" name="boton_objeto5">Objeto5</button>
            <button type="button" id="boton_objeto6" name="boton_objeto6">Objeto6</button>
            <button type="button" id="boton_regresar" name="boton_regresar">Regresar</button>
        `;

        divBotones.style.gridTemplateColumns = "1fr 1fr 1fr";
        const botonesObjeto = divBotones.querySelectorAll('button');
        aplicarEstiloBoton(botonesObjeto);
        const botonRegresar = document.getElementById('boton_regresar');
        botonRegresar.style.gridColumn = "3";
        botonRegresar.addEventListener('click', () => {
            divBotones.innerHTML = contenidoOriginal;
            aplicarEstiloBoton(divBotones.querySelectorAll('button'));
            configBotonesOriginales();
        });
    }

    aplicarEstiloBoton(divBotones.querySelectorAll('button'));
    configBotonesOriginales();
});
``
