showTime()
showWeather()

//speak(what_a[Math.floor(Math.random() * what_a.length)])

//listen("mails")

get_email_info()

/* Mail Page */
function get_email_info(){ //
    idle_listen("stop")

    get_listen_input.then(function(result){
        $("#to").val(result)
    })
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


function get_input (input){

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