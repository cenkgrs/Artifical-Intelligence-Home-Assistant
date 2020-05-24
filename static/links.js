var sections = $(".section");
console.log(sections)
$('#msg-link').on('click', function() {
    open_messages()
});

$('#mail-link').on('click', function() {get_email_info
    open_mails()
});

$('#todo-link').on('click', function() {
    open_todo()
});

$('#alarm-link').on('click', function() {
    open_alarm()
});

$('#diet-link').on('click', function() {
    open_diet()
});

$("#calendar-link, #cal-link").on('click', function() {
    open_calendar()
});

const open_index = function(){
    oracleType = "index"
    sections.not( $("#index-section") ).css({"display": "none"})

    $("#index-section").fadeIn()
    idle_listen()
}

const open_messages = function(){
    oracleType = "messages"
    sections.not( $("#messages-section") ).css({"display": "none"})

    $("#messages-section").fadeIn()
    predictions()
}
const open_mails = function(){
    oracleType = "mails"
    sections.not( $("#mails-section") ).css({"display": "none"})

    $("#mails-section").fadeIn()
    //speak("Who we are sending this mail ?")

    //get_email_info()

}
const open_todo = function(){
    oracleType = "todo"
    sections.not( $("#todo-section") ).css({"display": "none"})
    $("#todo-section").fadeIn()

    get_todo()
    //idle_listen()
}
const open_alarm = function(){
    oracleType = "alarm"
    sections.not( $("#alarm-section") ).css({"display": "none"})
    $("#alarm-section").fadeIn()

    get_alarms()
    idle_listen()
}
const open_diet = function(){
    oracleType = "diet"

    check_cal(function ( result ) {
        if (!result){
            speak("I need you to fill this form for giving advice and preparing your diet program sir")
            speak("Don't worry this is for the first and last time")
            sections.not( $("#calorie-section") ).css({"display": "none"})
            $("#calorie-section").fadeIn()

        }else{
            sections.not( $("#diet-section") ).css({"display": "none"})
            $("#diet-section").fadeIn()

        }

    })
    sections.not( $("#diet-section") ).css({"display": "none"})
    $("#diet-section").fadeIn()

    get_meals()
    idle_listen()
}
const open_book = function(){
    oracleType = "book"

    sections.not( $("#book-section") ).css({"display": "none"})
    $("#book-section").fadeIn()
    get_book_input()

}
const open_weather = function(){
    oracleType = "weather"

    sections.not( $("#weather-section") ).css({"display": "none"})
    $("#weather-section").fadeIn()
    predict_weather()

}
const open_calendar = function(){
    oracleType = "calendar"
    sections.not( $("#calendar-section") ).css({"display": "none"})
    $("#calendar-section").fadeIn()
}