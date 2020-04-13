$('#msg-link').on('click', function() {
    location.href = '/messages';
});

function showTime(){
    var date = new Date();
    h = date.getHours(); // 0 - 23
    m = date.getMinutes(); // 0 - 59
    var s = date.getSeconds(); // 0 - 59
    var session = "AM";

    if(h == 0){
        h = 12;
    }

    if(h > 12){
        session = "PM";
    }

    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;

    var time = h + ":" + m + ":" + s;
    document.getElementById("clock").innerText = time;
    document.getElementById("clock").textContent = time;

    day = date.getDate();
    month = date.getMonth();
    var year = date.getFullYear();
    var day_string = days[date.getDay()]

    month = months[month]

    var date = day + " " + month + " " + day_string ;

    document.getElementById("date").innerText = date;
    document.getElementById("date").textContent = date;


    setTimeout(showTime, 1000);

}
showTime();

speak(greetings[Math.floor(Math.random() * greetings.length)]);


$(".circle-1").click(function(){
    speak("Tell me something")
    text = listen()
});




//speak("If you want anything for me to do just click one of the links and i'll do the rest");

//speak("For starters hour is " + h + " " + m)
//speak("And today is " + day + " " + month)
//speak("If you need anything i'm here sir ")



