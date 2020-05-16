function record_bedtime(){

    speak("Can you please rate this day from 1 to 10 sir")
    get_listen_input( function(result){
        rate = parseInt(result) * 10

    var now = new Date();

    now = (now.toString()).split(" ")

    month = months[now[1]]
    month = months.indexOf("May") + 1
    month = (month < 10) ? "0" + month : month

    time = now[4].split(":")
    hour = time[0]
    minutes = time[1]

    hour = parseInt(time[0]) + Math.round(minutes/60)
    waketime = null

    date = now[2] + "." + month + "." + now[3]

    post_data = {
        "date": date,
        "bedtime": hour,
        "waketime": waketime,
        "rate": rate,
    }

    $.ajax({
        url: "http://localhost:5000/record_bedtime",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(post_data)
     }).done(function(data) {
        console.log(data)
        if (data)
        {
            speak(night_a[Math.floor(Math.random() * night_a.length)])
        }
        else{

        }
    });

}

function update_waketime(){

    var now = new Date();

    now = (now.toString()).split(" ")
    time = now[4].split(":")
    hour = time[0]
    minutes = time[1]

    waketime = parseInt(time[0]) + Math.round(minutes/60) + 8

    waketime = (waketime < 10) ? "0" + waketime : waketime

    $.ajax({
        url: "http://localhost:5000/update_waketime",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify("waketime": waketime)
     }).done(function(data) {
        console.log(data)
        if (data)
        {

        }
        else{
            //
        }
    });

}