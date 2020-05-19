function beep() {
    var snd = new Audio("data:audio/wav;base64,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qJrx4KOQjahZxWbcZgztj2c49nKmkId44S71j0c8eV9yDK6uPRzx5X18eDvjvQ6yKo9ZSS6l//8elePK/Lf//IInrOF/FvDoADYAGBMGb7FtErm5MXMlmPAJQVgWta7Zx2go+8xJ0UiCb8LHHdftWyLJE0QIAIsI+UbXu67dZMjmgDGCGl1H+vpF4NSDckSIkk7Vd+sxEhBQMRU8j/12UIRhzSaUdQ+rQU5kGeFxm+hb1oh6pWWmv3uvmReDl0UnvtapVaIzo1jZbf/pD6ElLqSX+rUmOQNpJFa/r+sa4e/pBlAABoAAAAA3CUgShLdGIxsY7AUABPRrgCABdDuQ5GC7DqPQCgbbJUAoRSUj+NIEig0YfyWUho1VBBBA//uQZB4ABZx5zfMakeAAAAmwAAAAF5F3P0w9GtAAACfAAAAAwLhMDmAYWMgVEG1U0FIGCBgXBXAtfMH10000EEEEEECUBYln03TTTdNBDZopopYvrTTdNa325mImNg3TTPV9q3pmY0xoO6bv3r00y+IDGid/9aaaZTGMuj9mpu9Mpio1dXrr5HERTZSmqU36A3CumzN/9Robv/Xx4v9ijkSRSNLQhAWumap82WRSBUqXStV/YcS+XVLnSS+WLDroqArFkMEsAS+eWmrUzrO0oEmE40RlMZ5+ODIkAyKAGUwZ3mVKmcamcJnMW26MRPgUw6j+LkhyHGVGYjSUUKNpuJUQoOIAyDvEyG8S5yfK6dhZc0Tx1KI/gviKL6qvvFs1+bWtaz58uUNnryq6kt5RzOCkPWlVqVX2a/EEBUdU1KrXLf40GoiiFXK///qpoiDXrOgqDR38JB0bw7SoL+ZB9o1RCkQjQ2CBYZKd/+VJxZRRZlqSkKiws0WFxUyCwsKiMy7hUVFhIaCrNQsKkTIsLivwKKigsj8XYlwt/WKi2N4d//uQRCSAAjURNIHpMZBGYiaQPSYyAAABLAAAAAAAACWAAAAApUF/Mg+0aohSIRobBAsMlO//Kk4soosy1JSFRYWaLC4qZBYWFRGZdwqKiwkNBVmoWFSJkWFxX4FFRQWR+LsS4W/rFRb/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VEFHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAU291bmRib3kuZGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjAwNGh0dHA6Ly93d3cuc291bmRib3kuZGUAAAAAAAAAACU=");
    snd.play();
}

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

function showWeather(){
    message = "hi"
    $.ajax({
        url: "http://localhost:5000/weather",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"message": message})
    }).done(function(data) {
        weather_status = data[0]["Status"]
        weather_temp = data[0]["Temp"]
        $("#temp").html(weather_temp + "º")
    });
}

function getCurrency(){

    speak(complete_a[Math.floor(Math.random() * finish_a.length)])

    message = "hi"
    $.ajax({
        url: "http://localhost:5000/get_currency",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"message": message})
    }).done(function(data) {

        if (data[0]["status"])
        {

            speak("US Dollar is " + data[0]["usd"], 1)
            speak("and EURO is " + data[0]["eur"], 1)
            speak("lastly Pound is " + data[0]["pound"], 1)

        }
        else{
            speak(finish_a[Math.floor(Math.random() * finish_a.length)])
        }
    });
}

function quit(){
    speak(quit_a[Math.floor(Math.random() * finish_a.length)])
    record_command(audio, "quit", 7)

    setTimeout(() => {
         $.ajax({
            url: "http://localhost:5000/quit",
            type: "POST",
         })
     }, 3000);


}

async function speak(text){
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

function idle_listen(type){


    var rec = new webkitSpeechRecognition() || new SpeechRecognition();
    //let rec = new window.SpeechRecognition();
    rec.lang = "en-UK";

    rec.start()

    type = (typeof type == "undefined") ? type = null : type
    console.log(type)
    if(type == "stop" ){
        console.log("stopped")
        rec.stop();
    }

    if(type == "predict"){
        console.log("predicted")
        rec.stop()
        setTimeout(() => {  predictions() }, 2000);
    }

    rec.addEventListener('speechstart', function(event) {
        console.log(event)
        console.log(oracleType);
        result = listen(oracleType);
        console.log("didnt wait")
        if (result == "stop") { rec.stop(); return;}

    });


    rec.addEventListener('speechend', function(event) {
        //rec.stop();
        //idle_listen()
    });

}

 function listen(type) {
    beep()

    window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
    let finalTranscript = '';
    let recognition = new window.SpeechRecognition();

    recognition.interimResults = true;
    recognition.maxAlternatives = 10;
    recognition.continuous = true;
    recognition.lang = "en-UK";

    recognition.start();

    recognition.onresult = (event) => {
       let resultScript = null
      let interimTranscript = '';
      for (let i = event.resultIndex, len = event.results.length; i < len; i++) {
        let transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          finalTranscript += transcript;
        } else {
          interimTranscript += transcript;
        }
      }
        document.getElementById('user-input').innerHTML = finalTranscript + '<i style="color:#ddd;">' + interimTranscript + '</>';

            if ( finalTranscript != ""){ resultScript = check_command(finalTranscript, type) }

        if ( resultScript == "no command") { speak("Did not get that sir, please repeat"), listen("index")}

        if( resultScript == "") { console.log("got here "); recognition.stop(); idle_listen() }

        if( resultScript == "predict") { console.log("got form"); recognition.stop(); idle_listen("predict") }

        if( resultScript == "stop") { console.log("got here 2"); recognition.stop(); idle_listen("stop"); }

        /*if (type == "form" && finalTranscript != ""){
            return finalTranscript
        }*/


    }

    recognition.onspeechend = function() {
        recognition.stop();
        //idle_listen()
    }

}

//var get_listen_input = new Promise(function(resolve, reject){
function get_listen_input(callback) {
    max_confidence = 0
    console.trace();
    beep()
    console.log("i'm listening")
    var streaming = new webkitSpeechRecognition();
    streaming.lang = 'en-IN';
    streaming.continuous = true;
    streaming.interimResults = true;

    streaming.onresult = function(event) {

        l_pos = event.results.length - 1 ;

        confidence = event.results[l_pos][0].confidence
        console.log(confidence)
        if( confidence > max_confidence ){
            console.log("max : "+ confidence)
            console.log(event)
            max_confidence = confidence
            transcript = event.results[l_pos][0].transcript;
            document.getElementById('user-input').innerHTML = transcript
        }

        //setTimeout(() => { resolve(result) }, 3000);

        setTimeout(() => {
            if(event.results[l_pos].isFinal){
                result = transcript
                streaming.stop()
                callback(result);
            }
         } , 3000);


    }

    streaming.onspeechend = function(event) {
        //
    }

    streaming.start();
}

function check_command(audio, type){
    //audio = audio.toString().toLowerCase();
    console.log(audio)
    console.log(oracleType)
    if(greetings_q.includes(audio)){
        speak(greetings_a[Math.floor(Math.random() * greetings_a.length)])
        record_command(audio, "greeting", 1)
        //setTimeout(() => { idle_listen("default") }, 4000);

        return ""
    }
    else if (message_q.includes(audio)){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "message", 8)

        setTimeout(() => { open_messages() }, 2000);
        setTimeout(() => { idle_listen() }, 4000);

        return ""
    }
    else if (who_q.includes(audio)){
        speak( who_a[Math.floor(Math.random() * who_a.length)] )
        record_command(audio, "who", 2)
        setTimeout(() => { idle_listen() }, 4000);

        return ""
    }
    else if (how_q.includes(audio)){
        speak(how_a[Math.floor(Math.random() * how_a.length)])
        setTimeout(() => { idle_listen() }, 4000);

        return ""
    }
    else if (thanks_q.includes(audio)){
        speak( thanks_a[Math.floor(Math.random() * thanks_a.length)] )
        record_command(audio, "thank", 3)
        setTimeout(() => { idle_listen() }, 4000);

        return ""
    }

    /* Day Messages */

    else if (night_q.includes(audio)) {
        setTimeout(() => { record_bedtime() }, 2000);

        return "stop"
    }

    /* Music Commands */
    else if (bg_music_q.includes(audio) || audio.includes("play music")) {  // Start the music
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "music-start", 4)

        setTimeout(() => {  play_bg_music("play"); }, 2000);

        return ""
    }
    else if (bg_music_c.includes(audio) || audio.includes("change music")) {  // Change the music
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "music-change", 9)

        setTimeout(() => {  play_bg_music("change"); }, 2000);

        return ""
    }
    else if (bg_music_s.includes(audio) || audio.includes("stop music")) { // Stop the music
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "music-stop", 5)

        setTimeout(() => {  play_bg_music("stop"); }, 2000);

        return ""
    }

    else if (currency_q.includes(audio)){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "currency", 6)

        getCurrency()
    }
    else if (quit_q.includes(audio)){

        quit()
    }

    /* Mails Page */

    else if ( audio.includes("open mails") || audio.includes("open emails") || open_emails_q.includes(audio) ){ // Open mails page
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        setTimeout(() => {  open_mails() }, 4000);

        return ""
    }
    else if ( email_input_q.includes(audio) ){

        open_mails()
        setTimeout(() => {  get_email_info() }, 2000);


        return "stop"
    }
    else if (send_email_q.includes(audio) && (type == "mails" || oracleType == "mails")){
        send_email()

        return "stop"
    }

    /* Diet page */

    else if( diet_input_q.includes(audio)  && oracleType == "diet"){

        setTimeout(() => {  get_meal_input() }, 3000);

        return ""
    }

    /* to-do page */
    else if (open_todo_q.includes(audio)){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "todo", 8)
        speak("This is the works you should do in little time sir")

        open_todo()

        return ""
    }

    else if (todo_q.includes(audio)){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "todo", 8)

        setTimeout(() => { open_todo(); tell_works() }, 000);

        return "stop"
    }

    else if (todo_input_q.includes(audio) && oracleType == "todo"){
        //open_todo()

       setTimeout(() => {

        speak("I'm listening you sir")

            get_listen_input( function(result){
                console.log(result)

                speak("Should i save this sir ?")
                $("#todo-body").val(result)
                get_listen_input( function (result) {
                    console.log(result)

                    if(confirm_q.includes(result)){
                        add_todo_item()
                    }else{
                        speak("If you want to save it just let me know")
                    }

                })
            });
        }, 2000);

        return "stop"
    }
    else if (add_q.includes(audio) && oracleType == "todo"){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])

        setTimeout(() => { add_todo_item() }, 2000);

        return ""
    }
    /* Predictions */

    else if (predict_q.includes(audio)) {
        speak(predict_a[Math.floor(Math.random() * predict_a.length)])

        return "predict"
    }

    else if (audio.includes("timer")){
        var bmpDigits = /[0-9\u0660-\u0669\u06F0-\u06F9\u07C0-\u07C9\u0966-\u096F\u09E6-\u09EF\u0A66-\u0AE6\u0AE6-\u0AEF\u0B66-\u0B6F\u0BE6-\u0BEF\u0C66-\u0C6F\u0CE6-\u0CEF\u0D66-\u0D6F\u0DE6-\u0DEF\u0E50-\u0E59\u0ED0-\u0ED9\u0F20-\u0F29\u1040-\u1049\u1090-\u1099\u17E0-\u17E9\u1810-\u1819\u1946-\u194F\u19D0-\u19D9\u1A80-\u1A89\u1A90-\u1A99\u1B50-\u1B59\u1BB0-\u1BB9\u1C40-\u1C49\u1C50-\u1C59\uA620-\uA629\uA8D0-\uA8D9\uA900-\uA909\uA9D0-\uA9D9\uA9F0-\uA9F9\uAA50-\uAA59\uABF0-\uABF9\uFF10-\uFF19]/;
        var hasNumber = RegExp.prototype.test.bind(bmpDigits);

        has = hasNumber(audio)
        if(has) {
            var date = new Date();
            number = audio.match(/\d+/)[0] // "3"
            speak("Timer is started sir")

            if( audio.includes("minute") || audio.includes("minute")){
                date.setMinutes( date.getMinutes() + parseInt(number) );
                console.log(date)
            }
            else if( audio.includes("hour") || audio.includes("hours") ){
                date.setHours( date.getHours() + parseInt(number) );
            }
            else if ( audio.includes("second") || audio.includes("seconds")) {
                date.setSeconds( date.getSeconds() + parseInt(number) );
            }
            else{
                speak("Did you said hour or minute sir ?")
                return ;
            }
            localStorage.setItem("stored-timer",date);
            sessionStorage.setItem("timer", date);
            setTimer(date)
            return ""
        }
    }

    return "no command"
}

function play_intro_music(){
    keys = Object.keys(intro);
    $('.my_audio').append("<source id='sound_src' src=" + intro[keys[Math.floor(Math.random() * keys.length)]] + " type='audio/mpeg'>");
    $(".my_audio").trigger('play');
    setTimeout(() => { $(".my_audio").trigger('pause') }, 14000);

}

function play_bg_music(task){
    keys = Object.keys(playlist);
    $(".my_audio").empty()

    if(task == 'play'){

        window.random = Math.floor(Math.random() * keys.length)
        alert(window.random)
        $('.my_audio').append("<source id='sound_src' src=" + playlist[keys[random]] + " type='audio/mpeg'>");

        $(".audio-stop").fadeIn();

        $(".my_audio").trigger('play');
    }
    if(task == "change"){
        $(".my_audio").trigger('pause');
        $(".my_audio").prop("currentTime",0);

        window.random++
        window.random = (window.random >= keys.length) ? 0 : window.random
        console.log(window.random, keys.length)

        $('.my_audio').append("<source id='sound_src' src=" + playlist[keys[window.random]] + " type='audio/mpeg'>");
        $(".my_audio").trigger('load');
        $(".my_audio").trigger('play');
    }
    if(task == "pause"){
        $(".audio-stop").fadeToggle();
        $(".my_audio").trigger('pause');
    }
    if(task == 'stop'){
           $(".audio-stop").fadeToggle();
           $(".my_audio").trigger('pause');
           $(".my_audio").prop("currentTime",0);
      }

}


function record_command(text, command, type)
{
    console.log(command)
     $.ajax({
        url: "http://localhost:5000/record_command",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"text": text, "command": command, "type": type})
    }).done(function(data) {

    });
}

function predictions () {

    get_listen_input( function(result){
        console.log(result)
        speak("So you want the " + result + " price")
        $(".predict_modal").fadeToggle()

        oracleType = "index"
        sections.css({"display": "none"})

        $(".predict-button").attr("data-predict-type", result)

        result == "house" ? $('#house_check').prop('checked', true) : $('#car_check').prop('checked', true)

        speak("Please give me the detail of the " + result + "and i'll do tha calculations sir ")
        idle_listen()
    });

}

function trial(){
    get_listen_input( function(result){
        console.log(result)
        speak("You said " + result)

        get_listen_input( function (result) {
            console.log(result)
            speak("You said" + result)
        });

    });
}

function setTimer(countDownDate){
    //var countDownDate = sessionStorage.getItem("timer");
    $(".timer").fadeIn();

    var x = setInterval(function() {

        // Get today's date and time
        var now = new Date();

        // Find the distance between now and the count down date
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="demo"

        if (hours >= 1 ){
            (hours < 10) ? $("#timer-1").html("0" + hours) : $("#timer-1").html(hours);
            (minutes < 10) ? $("#timer-2").html("0" + minutes) : $("#timer-2").html(minutes);

        }
        else{
            (minutes < 10) ? $("#timer-1").html("0" + minutes) : $("#timer-1").html(minutes);
            (seconds < 10) ? $("#timer-2").html("0" + seconds) : $("#timer-2").html(seconds);
        }

        // If the count down is finished, write some text
        if (distance < 0) {
            clearInterval(x);
            $("#timer-1").html("00")
            $("#timer-2").html("00")

            speak("Time is over sir")

            $(".timer").fadeOut();
        }
    }, 1000);
}

function checkClock(){
    var date = new Date();
    h = date.getHours(); // 0 - 23

    if ( h !== 6 && h !== 7 && h !== 8 && h !== 9 && h !== 10 && h !== 12 && h != 18 ){
        return false
    }else{
        return h
    }
}

$(document).ready(function(){



    $(".circle-1, .text-box, .circle-1-diet").click(function(){
        listen($(this).data("type"))
    });

    $('.my_audio').on('ended', function() {
       $("#sound_src").attr("src", playlist[keys[Math.floor(Math.random() * keys.length)]])[0];
       $(".my_audio").trigger('load');
       play_bg_music('play');
    });


    $(".audio-stop").on("click",function(){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        $(".my_audio").trigger('pause');
        $(".audio-stop").fadeToggle();
    });
});
