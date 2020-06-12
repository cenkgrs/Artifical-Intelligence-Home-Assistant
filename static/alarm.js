$(document).ready(function() {
    var alarms;


    $(document).on("click", ".alarm-hour-arrow", function() {
        type = $(this).data("type")
        type = type.split("-")
        console.log(type)
        console.log($("#alarm-"+ type[0] + "-picker").html())

        // type[0] -> hour, minute -  type[1] -> up, down

        // If type is up then add + 1 to hour picker ( by first converting it to int)
        $("#alarm-"+ type[0] + "-picker").html( (type[1] == "up") ?  parseInt($("#alarm-"+ type[0] + "-picker").html()) + 1 : $("#alarm-"+ type[0] + "-picker").html() - 1 )

        // After hour up or down if html value below 10 like ( 5 9) make it like ( 05 09)
        $("#alarm-"+ type[0] + "-picker").html() < 10 ? $("#alarm-"+ type[0] + "-picker").html( "0" + $("#alarm-"+ type[0] + "-picker").html() ) : ""

        $("#alarm-hour-hour").html() == "00" ? $('*[data-type=hour-down]').prop('disabled', true)  : $('*[data-type=hour-down]').prop('disabled', false)

        $("#alarm-minute-picker").html() == "00" ? $('*[data-type=minute-down]').prop('disabled', true)  : $('*[data-type=minute-down]').prop('disabled', false)

    })

    $(".alarm-add-button").on("click", function() {

        hour = $("#alarm-hour-picker").html()
        minute = $("#alarm-minute-picker").html()
        text = "set an alarm for " + hour + " " + minute
        console.log(text)
        alarm(text)
    })
})

// This function sends command to backend and there sets an alarm or get alarms or delete alarms
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
        }else if(data["status"] != false && data["action"] == "show"){
            open_alarm()
            tell_alarms()
        }else if(data["action"] == "delete"){
            speak("All alarms deleted sir")
        }else{
            speak(data["error"])
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
            $(".alarms").empty();
            return
        }
        fill_alarms_panel(alarms)
    });
}

function fill_alarms_panel(alarms){

    $(".alarms").empty();

    alarms.forEach(function(entry, i) {
        console.log(entry)
        hour = (entry[1] < 10) ? "0" + entry[1] : entry[1]
        minute = (entry[2] < 10) ? "0" + entry[2] : entry[2]
        item = document.createElement("strong");
        item.className = "alarm-item";
        item.id = "alarm-" + entry[0];
        item.innerHTML = "<span>" + (i = i + 1) + "</span> - <span class='alarm-clock'>" + hour + " : " + minute + "</span>";
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