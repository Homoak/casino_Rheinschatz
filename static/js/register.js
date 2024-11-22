document.addEventListener("DOMContentLoaded", function() {
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const replPasswordInput = document.getElementById('repl_password');
    const submitButton = document.getElementById('submitButton');

    // Функція для перевірки форми
    function checkForm() {
        const name = nameInput.value.trim();
        const email = emailInput.value.trim();
        const password = passwordInput.value.trim();
        const replPassword = replPasswordInput.value.trim();

        // Перевірка на заповненість полів та співпадіння паролів
        if (name && email && password && replPassword && password === replPassword) {
            submitButton.disabled = false; // Активувати кнопку, якщо всі умови виконано
        } else {
            submitButton.disabled = true; // Інакше залишити кнопку неактивною
        }
    }

    // Додаємо слухачів на кожне поле вводу
    [nameInput, emailInput, passwordInput, replPasswordInput].forEach(input => {
        input.addEventListener('input', checkForm);
    });

    // Початкова перевірка форми при завантаженні сторінки
    checkForm();

    // Відправка форми з анімацією при натисканні на кнопку
    submitButton.addEventListener('click', function(event) {
        if (!submitButton.disabled) {
            event.preventDefault(); // Запобігання стандартній поведінці для початку
            const audio = document.getElementById('audio');
            if (audio) {
                audio.play().then(() => {
                    document.getElementById('registrationForm').submit();
                }).catch(error => {
                    console.error('Не вдалося програти аудіо:', error);
                    document.getElementById('registrationForm').submit(); // Відправка форми у разі помилки аудіо
                });
            } else {
                document.getElementById('registrationForm').submit(); // Якщо нема аудіо, відправляємо форму відразу
            }
        }
    });

    // Виведення повідомлень Flash (якщо є)
    const messages = document.querySelectorAll('.flash-message');
    messages.forEach(function(message) {
        setTimeout(function() {
            message.classList.add('visible');
        }, 100);
        setTimeout(function() {
            message.classList.add('hidden');
            setTimeout(function() {
                message.remove();
            }, 1000);
        }, 5000);
    });
});

function play() {
         var audio = document.getElementById("audio");
         audio.currentTime = 0;
         audio.play();
       }
         const button = document.getElementById('soundButton');
         const hoverSound = document.getElementById('hoverSound');

         button.addEventListener('mouseenter', () => {
             hoverSound.currentTime = 0; // Возвращает звук к началу
             hoverSound.play();
         });
         function playSound() {
     var sound = document.getElementById("clickSound");
     sound.play();
 }