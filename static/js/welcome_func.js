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