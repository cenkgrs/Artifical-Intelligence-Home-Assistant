
function showTime(){
    var date = new Date();
    var h = date.getHours(); // 0 - 23
    var m = date.getMinutes(); // 0 - 59
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

    var day = date.getDate();
    var month = date.getMonth();
    var year = date.getFullYear();
    var day_string = days[date.getDay()]

    var month = months[month]

    var date = day + " " + month + " " + day_string ;

    document.getElementById("date").innerText = date;
    document.getElementById("date").textContent = date;


    setTimeout(showTime, 1000);

}

showTime();