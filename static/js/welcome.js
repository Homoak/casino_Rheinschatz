const checkbox = document.getElementById('checkbox');
    const submitButton = document.getElementById('submitButton');

    checkbox.addEventListener('change', function() {
        submitButton.disabled = !this.checked; // Активируем кнопку, если галочка отмечена
    });