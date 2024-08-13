function confirmarExclusao(eventoId) {
    if (confirm("Tem certeza de que deseja excluir este evento?")) {
        window.location.href = "/gaps/excluir_evento/" + eventoId + "/";
    }
}

// Esconde a mensagem de sucesso após 3 segundos
setTimeout(function() {
    document.getElementById('alert-message').style.display = 'none';
}, 3000);
