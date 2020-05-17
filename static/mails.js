showTime()
showWeather()

//speak(what_a[Math.floor(Math.random() * what_a.length)])


/* Mail Page */
function get_email_info(){ //

    get_listen_input( function(result){
        to = result
        speak("So i will send this mail to " + to)
        $("#to").val(to)
        speak("What is the subject")

        get_listen_input( function (result) {
            subject = result
            $("#subject").val(subject)
            speak("Then subject is" + subject)
            speak("Lastly what will be the body")

            get_listen_input(function ( result ) {
                $("#body").val(result)
                speak("I wrote to body this " + result)
                speak("All done sir, i will send the mail to " + to + " with " + subject + " subject. Is there anything you want to change or should i send the mail now")

                get_listen_input(function ( result ) {
                    console.log(result)

                    if(confirm_q.includes(result)) {
                        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
                        send_email()
                    }else if(abort_q.includes(result)){
                        speak("Okay sir when you ready just ask me to send it")
                    }else{
                        speak("Did not get that sir, please repeat")
                        idle_listen()
                    }
                });
            });
        });
    });

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

        if (data["success"])
        {
            speak(finish_a[Math.floor(Math.random() * finish_a.length)])
        }
        else{
            //
        }
    });
}