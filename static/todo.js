showTime()
showWeather()
idle_listen()
//speak("This is the works you should do in little time sir")
get_todo()
/* To - Do Page */



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
            console.log(data)
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

    });
}

function fill_panel(data){

    today_todo = data[0]["today"]

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