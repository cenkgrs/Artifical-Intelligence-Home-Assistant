$('#msg-link').on('click', function() {
    location.href = '/messages';
});

showTime();

speak(greetings_a[Math.floor(Math.random() * greetings_a.length)]);


$(".circle-1, .text-box").click(function(){
    beep()
    text = listen()
});

$(".weather").click(function(){
    message = "hi"
    $.ajax({
        url: "http://localhost:5000/weather",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"message": message})
    }).done(function(data) {
        weather_status = data[0]["Status"]
        weather_temp = data[0]["Temp"]
        console.log(weather_status)
        console.log(weather_temp)
    });

});




//speak("If you want anything for me to do just click one of the links and i'll do the rest");

//speak("For starters hour is " + h + " " + m)
//speak("And today is " + day + " " + month)
//speak("If you need anything i'm here sir ")



