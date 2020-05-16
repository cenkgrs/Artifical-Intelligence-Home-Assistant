var sections = $(".section");

$('#msg-link').on('click', function() {
    open_messages()
});

$('#mail-link').on('click', function() {
    open_mails()
});

$('#todo-link').on('click', function() {
    open_todo()
});

$("#calendar-link").on('click', function() {
    open_calendar()
})

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
    speak("Who we are sending this mail ?")

    get_email_info()
}
const open_todo = function(){
    oracleType = "todo"
    sections.not( $("#todo-section") ).css({"display": "none"})
    $("#todo-section").fadeIn()

    speak("This is the works you should do in little time sir")
    get_todo()
    idle_listen()
}
const open_calendar = function(){
    oracleType = "calendar"
    sections.not( $("#calendar-section") ).css({"display": "none"})
    $("#calendar-section").fadeIn()
}