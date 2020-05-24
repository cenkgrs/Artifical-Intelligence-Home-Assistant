$(document).ready(function() {
    var alarms
})


function alarm(text){
    $.ajax({
        url: "http://localhost:5000/alarm",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"text": text})
    }).done(function(data) {
        if (data && data["status"] != false && data["action"] == "")
        {
            get_alarms()
            speak(complete_a[Math.floor(Math.random() * complete_a.length)])
            idle_listen()
        }else if(data["status"] != false && data["action"] != ""){
            open_alarm()
            tell_alarms()
        }
        else{
            speak("There is an "+ data["error"] + "sir")
        }
    });
}

function check_alarm(){

    $.ajax({
        url: "http://localhost:5000/check_alarm",
        type: "GET",
    }).done(function(data) {
        if (data["status"] == "alarm")
        {
            keys = Object.keys(intro);
            $('.my_audio').append("<source id='sound_src' src=" + intro[keys[Math.floor(Math.random() * keys.length)]] + " type='audio/mpeg'>");
            $(".my_audio").trigger('play');
            setTimeout(() => { $(".my_audio").trigger('pause'); speak("You did set an alarm for this hour sir") }, 14000);
        }
    });
}

function get_alarms(){
    $.ajax({
        url: "http://localhost:5000/get_alarms",
        type: "GET",
    }).done(function(data) {
        console.log(data)
        alarms = data["data"]
        if(!alarms){
            return
        }
        fill_alarms_panel(alarms)
    });
}

function fill_alarms_panel(alarms){

    $(".alarms").empty();

    alarms.forEach(function(entry, i) {
        item = document.createElement("strong");
        item.className = "alarm-item";
        item.id = "alarm-" + entry[0];
        item.innerHTML = (i = i + 1) + " - " + entry[1] + " : " + entry[2];
        $(".alarms").append(item)
    })
}

function tell_alarms(){

    setTimeout(() => {
        // If there isn't any alarms just return
        if(!alarms){
            speak("You didn't set any alarm sir")
            idle_listen()

            return
        }

        speak("Sir this is your setted alarms ")
        alarms.forEach( function (entry, i) {
            speak(deca[i + 1])
            speak("at" + entry[1] + " " + entry[2])
        })

        speak("That's all boss")
        idle_listen()
     }, 1000);
}