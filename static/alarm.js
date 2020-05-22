function alarm(text){
    $.ajax({
        url: "http://localhost:5000/alarm",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"text": text})
    }).done(function(data) {
        console.log(data)
        if (data && data["status"] != false)
        {
            speak(complete_a[Math.floor(Math.random() * complete_a.length)])
            idle_listen()
        }
        else{
            speak("There is an "+ data["error"] + "sir")
        }
    });
}

function check_alarm(){
    console.log("checked alarm")
    $.ajax({
        url: "http://localhost:5000/check_alarm",
        type: "GET",
    }).done(function(data) {
        console.log(data)
        if (data["status"] == "alarm")
        {
            keys = Object.keys(intro);
            $('.my_audio').append("<source id='sound_src' src=" + intro[keys[Math.floor(Math.random() * keys.length)]] + " type='audio/mpeg'>");
            $(".my_audio").trigger('play');
            setTimeout(() => { $(".my_audio").trigger('pause') }, 14000);
        }
    });
}