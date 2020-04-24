showTime();
showWeather();

speak(greetings_a[Math.floor(Math.random() * greetings_a.length)]);




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
    });

});




//speak("If you want anything for me to do just click one of the links and i'll do the rest");

//speak("For starters hour is " + h + " " + m)
//speak("And today is " + day + " " + month)
//speak("If you need anything i'm here sir ")



