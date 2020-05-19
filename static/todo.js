showTime()
showWeather()
/* To - Do Page */

$(document).ready(function() {
    var today_todo
    var tomorrow_todo
})


function add_todo_item(){
    date = document.querySelector('input[name="day_selector"]:checked').value;
    todo = $("#todo-body").val()
     $.ajax({
        url: "http://localhost:5000/add_todo",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"date": date, "todo": todo})
     }).done(function(data) {

        if (data)
        {
            $("#todo-body").val("")
            speak(finish_a[Math.floor(Math.random() * finish_a.length)])

            fill_panel(data)

        }
        else{
            //
        }
    });
}

function get_todo(){
    $.ajax({
        url: "http://localhost:5000/get_todo",
        type: "GET",
    }).done(function(data) {

        fill_panel(data)
        console.log("got here")
        return data
    });
}

function fill_panel(data){

    today_todo = data[0]["today"]
    console.log("filled")
    $(".todo-today").empty();

    today_todo.forEach(function(entry, i) {
        item = document.createElement("strong");
        item.className = "todo-item";
        item.id = "today-" + i;
        item.innerHTML = (i = i + 1) + " - " + entry;
        $(".todo-today").append(item)
    })

    tomorrow_todo = data[0]["tomorrow"]

    $(".todo-tomorrow").empty()
    tomorrow_todo.forEach(function(entry, i) {
        item = document.createElement("strong");
        item.className = "todo-item";
        item.id = "tomorrow-" + i;
        item.innerHTML = (i = i + 1) + " - " + entry;
        $(".todo-tomorrow").append(item)

    })

}

function tell_works(){

    setTimeout(() => {
        speak("Sir today's works are")
        today_todo.forEach( function (entry, i) {
            speak(deca[i + 1])
            speak(entry)
        })

        speak("And tomorrow's works are")
            tomorrow_todo.forEach( function (entry, i) {
            speak(deca[i + 1])
            speak(entry)
        })

        speak("That's all boss")
     }, 2000);




}