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

function speak(text){
    const msg = new SpeechSynthesisUtterance(text);
    msg.volume = 1; // 0 to 1
    msg.rate = 1; // 0.1 to 10
    msg.pitch = 0.8; // 0 to 2

    const voice = speaks[0]; //47
    console.log(`Voice: ${voice.name} and Lang: ${voice.lang}`);
    msg.voiceURI = voice.name;
    msg.lang = voice.lang;


    speechSynthesis.speak(msg);
}

speak("Welcome to my user interface sir");
speak("If you want anything for me to do just click one of the links and i'll do the rest");

speak("For starters hour is " + h + " " + m)
speak("And today is " + day + " " + month)



