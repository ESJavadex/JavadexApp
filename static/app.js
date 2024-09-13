document.addEventListener('DOMContentLoaded', function() {
    obtenerMensajes();

    document.getElementById('formulario').addEventListener('submit', function(e) {
        e.preventDefault();
        enviarMensaje();
    });
});

function obtenerMensajes() {
    fetch('/mensajes')
        .then(response => response.json())
        .then(data => {
            const mensajesDiv = document.getElementById('mensajes');
            mensajesDiv.innerHTML = '';
            for (let id in data) {
                const p = document.createElement('p');
                p.textContent = data[id].mensaje;
                mensajesDiv.appendChild(p);
            }
        });
}

function enviarMensaje() {
    const mensajeInput = document.getElementById('mensaje');
    const mensaje = mensajeInput.value;
    fetch('/enviar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mensaje: mensaje })
    })
    .then(response => response.json())
    .then(data => {
        mensajeInput.value = '';
        obtenerMensajes();
    });
}
