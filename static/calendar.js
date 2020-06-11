let calendar_days = [];
let month = new Date().getMonth() + 1;
let year = new Date().getFullYear();

// This gets the days in this month
function getDaysInMonth() {

    $(".calendar-header").html(months[new Date().getMonth()])

    var date = new Date(year, month, 1);

    while (date.getMonth() === month) {
        calendar_days.push( new Date(date).getDate()  );
        date.setDate(date.getDate() + 1);
    }
    console.log(calendar_days);
}

// This is creating days at the calendar
function makeRows(rows, cols) {
    const container = document.getElementById("calendar-days");
    container.style.setProperty('--grid-rows', rows);
    container.style.setProperty('--grid-cols', cols);

    for (c = 0; c < (rows * cols); c++) {
        let day_header = document.createElement("div");
        day_header.innerText = (c + 1);
        day_header.className = "calendar-day-header";

        let day_information = document.createElement("div");
        day_information.className = "calendar-day-information";

        let cell = document.createElement("div");
        cell.setAttribute("data-id", c + 1);

        cell.appendChild(day_header);
        cell.appendChild(day_information);

        if(day > c) cell.style.backgroundColor = "rgba(255, 255, 255, 0.14)";
        container.appendChild(cell).className = "calendar-day";
    };

};

// This is filling calendar with informations
function fill_calendar(informations){
    informations.forEach(function(day, index){
        $('*[data-id='+ day[1] +'] .calendar-day-information').html(day[0])

    })

}

// This is for getting day info from user
function get_calendar_day(callback) {
    speak("Which day do you want to set sir")

    setTimeout(() => {
         get_listen_input( function (text) {

            if(hasNumber(text)){
                selected_day = text.match(/\d+/)[0]
            }

            callback(selected_day);
         });

    }, 2000);

}

function get_calendar_info(selected_day){

    // If day didn't specified ask for the day
    if(!selected_day){

        get_calendar_day( function(result){
            selected_day = result

            speak(listening_a[Math.floor(Math.random() * listening_a.length)])

            // Get the calendar information and set it
            get_listen_input( function (text) {

                // This will make first character upper case
                text = text[0].toUpperCase() + text.slice(1)

                speak(complete_a[Math.floor(Math.random() * complete_a.length)])
                $.ajax({
                    url: "http://localhost:5000/add_calendar_info",
                    type: "POST",
                    contentType: "application/json",
                    data: JSON.stringify({"text": text, "day": selected_day})
                }).done(function(data) {
                    console.log(data)
                    if (data && data["error"] == "")
                    {
                        fill_calendar(data["response"])
                        idle_listen()
                    }
                    else{
                        speak(data["error"])
                        speak("Can you repeat it sir ?")
                        setTimeout(() => { $(this).click() }, 4000);
                    }
                });

            })
        })
    }
    else{
        // If user specified the day just send act like user clicked to that day
        $('*[data-id='+ selected_day +']').click();
    }



}

$(document).ready(function(){
    getDaysInMonth()
    makeRows(6, 5);

    // This is for getting calendar informations
    $.ajax({
            url: "http://localhost:5000/get_calendar_info",
            type: "GET",
         }).done(function(data) {
            if (data && data["error"] == "")
            {
                fill_calendar(data["response"])
            }
            else{

            }
        });


    $(".calendar-day").click(function(){
        selected_day = $(this).data("id");
        console.log(selected_day);

        speak(listening_a[Math.floor(Math.random() * listening_a.length)])

        get_listen_input( function (text) {

            // This will make first character upper case
            text = text[0].toUpperCase() + text.slice(1)

            speak(complete_a[Math.floor(Math.random() * complete_a.length)])
            $.ajax({
                url: "http://localhost:5000/add_calendar_info",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({"text": text, "day": selected_day})
            }).done(function(data) {
                console.log(data)
                if (data && data["error"] == "")
                {
                    fill_calendar(data["response"])
                    idle_listen()
                }
                else{
                    speak(data["error"])
                    speak("Can you repeat it sir ?")
                    setTimeout(() => { $(this).click() }, 4000);
                }
            });

        })



    })



});
