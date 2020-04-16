$('#msg-link').on('click', function() {
    location.href = '/messages';
});

showTime();

speak(greetings_a[Math.floor(Math.random() * greetings_a.length)]);


$(".circle-1, .text-box").click(function(){
    beep()
    text = listen()
});




//speak("If you want anything for me to do just click one of the links and i'll do the rest");

//speak("For starters hour is " + h + " " + m)
//speak("And today is " + day + " " + month)
//speak("If you need anything i'm here sir ")



