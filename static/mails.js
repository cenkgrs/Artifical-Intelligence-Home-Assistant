showTime()
showWeather()

//speak(what_a[Math.floor(Math.random() * what_a.length)])


/* Mail Page */
function get_email_info(){ //

    get_listen_input( function(result){
        console.log(result)
        speak("So i will send this mail to " + result)
        $("#to").val(result)
        speak("What is the subject")

        get_listen_input( function (result) {
            console.log(result)
            $("#subject").val(result)
            speak("Then subject is" + result)
            speak("Lastly what will be the body")

            get_listen_input(function ( result ) {
                console.log(result)
                $("#body").val()
                speak("I wrote to body this " + result)
                speak("All done sir, i will send the mail to " + to + " is there anything you want to change or should i send the mail now")

                get_listen_input(function ( result ) {
                    console.log(result)

                    if(confirm_q.includes(command)) {
                        speak(complete_a[Math.floor(Math.random() * complete_a.length)])
                        send_email()
                    }else{

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