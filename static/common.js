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

function idle_listen(){
    var rec = new webkitSpeechRecognition() || new SpeechRecognition();
    //let rec = new window.SpeechRecognition();
    rec.lang = "en-UK";

    rec.start()

    rec.addEventListener('speechstart', function() {
        listen("default")
    });
}

function listen(type){
    beep()

    window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
    let finalTranscript = '';
    let recognition = new window.SpeechRecognition();

    recognition.interimResults = true;
    recognition.maxAlternatives = 10;
    recognition.continuous = true;
    recognition.lang = "en-UK";

    recognition.onresult = (event) => {
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
        console.log("waited")
        console.log(finalTranscript)
        if (type == "form" && finalTranscript != ""){
            console.log("checked")
            return finalTranscript
        }

        finalTranscript = check_command(finalTranscript, type)
    }
    recognition.start();

    recognition.onspeechend = function() {
      recognition.stop();
      idle_listen()
    }

}

const get_listen_input = new Promise(function(resolve, reject){
    beep()

    var streaming = new webkitSpeechRecognition();
    streaming.lang = 'en-IN';
    streaming.continuous = true;
    streaming.interimResults = true;

    streaming.onresult = function(event) {


        l_pos = event.results.length - 1 ;
        document.getElementById('user-input').innerHTML = event.results[l_pos][0].transcript;
        result = event.results[l_pos][0].transcript
        console.log(result)

        setTimeout(() => { resolve(result) }, 3000);

    }

    streaming.onspeechend = function(event) {
        //
    }

    streaming.start();
})

function check_command(audio, type){
    audio = audio.toString().toLowerCase();

    if(greetings_q.includes(audio)){
        speak(greetings_a[Math.floor(Math.random() * greetings_a.length)])
        record_command(audio, "greeting")
        setTimeout(() => { listen("default") }, 4000);

        return ""
    }
    else if (message_q.includes(audio)){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        record_command(audio, "greeting")
        setTimeout(() => { location.href = '/messages';}, 2000);

        return ""
    }
    else if (who_q.includes(audio)){
        speak( who_a[Math.floor(Math.random() * who_a.length)] )
        record_command(audio, "greeting")
        setTimeout(() => { listen("default") }, 4000);

        return ""
    }
    else if (thanks_q.includes(audio)){
        speak( thanks_a[Math.floor(Math.random() * thanks_a.length)] )
        record_command(audio, "greeting")
        setTimeout(() => { listen("default") }, 4000);

        return ""
    }
    else if (bg_music_q.includes(audio) || audio.includes("play music")) {  // Start the music
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        setTimeout(() => {  play_bg_music("play"); }, 2000);

        return ""
    }
    else if (bg_music_s.includes(audio) || audio.includes("stop music")) { // Stop the music
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        setTimeout(() => {  play_bg_music("stop"); }, 2000);

        return ""
    }
    else if ( audio.includes("open mails") || audio.includes("open emails") ){ // Open mails page
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        setTimeout(() => { location.href = '/mails';}, 2000);

    }
    else if (currency_q.includes(audio)){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        getCurrency()
    }
    else if (quit_q.includes(audio)){
        alert(audio)
        alert("came here")
        quit()
    }
    /* Mails Page */
    else if ( (audio.includes("input") || audio.includes("fill") || form_q.includes(audio)) && type == "mails" ){
        get_email_info()
    }
    else if (send_q.includes(audio) && type == "mails"){
        send_email()
        listen("mails")
    }

    /* to-do page */
    else if (todo_q.includes(audio)){
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
        setTimeout(() => { location.href = '/todo';}, 2000);
    }
    else if (add_q.includes(audio) && type == "todo"){
    }
    return audio
}

function play_intro_music(){
    keys = Object.keys(intro);
    $('.my_audio').append("<source id='sound_src' src=" + intro[keys[Math.floor(Math.random() * keys.length)]] + " type='audio/mpeg'>");
    $(".my_audio").trigger('play');
    setTimeout(() => { $(".my_audio").trigger('pause') }, 14000);

}

function play_bg_music(task){
    keys = Object.keys(playlist);
    $('.my_audio').append("<source id='sound_src' src=" + playlist[keys[Math.floor(Math.random() * keys.length)]] + " type='audio/mpeg'>");

    if(task == 'play'){
          $(".audio-stop").fadeToggle();
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

/* Mail Page */
function get_email_info(){ //
    speak("Who we are sending this mail ?")
    to = $("#to")
    to = get_input(to)

    /*
    speak("What is the subject ?")
    subject = $("#subject")
    subject = get_input(subject)

    speak("And what should i write in the body ?")
    body = $("#body")
    body = get_input(body)

    speak("All done sir, i will send the mail to is there anything you want to change or should i send the mail now")

    command =  listen("form")

    if (confirm_q.includes(command)){

    }
    else{
        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
    }
    */
}


function get_input(input){

    get_listen_input.then(function(result){
        input.val(result)
    })


}

function send_email(){
    speak(complete_a[Math.floor(Math.random() * complete_a.length)])

    to = $("#to").val()
    subject = $("#subject").val()
    message = $("#body").val()

    $.ajax({
        url: "http://localhost:5000/email_send",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"to": to, "subject": subject, "message": message})
    }).done(function(data) {

        if (data == "success")
        {
            speak(finish_a[Math.floor(Math.random() * finish_a.length)])
        }
        else{
            //
        }
    });
}


function record_command(text, command)
{
    console.log(command)
     $.ajax({
        url: "http://localhost:5000/record_command",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"text": text, "command": command})
    }).done(function(data) {

    });
}



$(document).ready(function(){

    $(".circle-1, .text-box").click(function(){
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
