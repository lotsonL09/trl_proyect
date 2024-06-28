function handleNoneOption(element) {
    const fieldset = element.closest('fieldset');
    const options = fieldset.querySelectorAll('.option');
    options.forEach(option => {
        option.checked = false;
        option.disabled = element.checked;
    });
}

function redirectToResultPage() {
    // Aquí puedes agregar lógica para calcular resultados o manejar datos antes de redirigir
    window.location.href = '/resultados/';
}