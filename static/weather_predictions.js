function predict_weather(){
     message = "",
     $.ajax({
        url: "http://localhost:5000/weather",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"message": message})
    }).done(function(data) {
        console.log(data)

        sunrise = data[0]["sunrise"]
        sunrise = sunrise.split(":")
        sunrise = parseFloat(sunrise[0]) + "." + parseFloat(sunrise[1])

        sunset = data[0]["sunset"]
        sunset = sunset.split(":")
        sunset = parseFloat(sunset[0]) + "." + parseFloat(sunset[1])

        date = new Date()
        day = date.getDate();
        month = date.getMonth();

        date = parseFloat(day + 1) + "." + parseFloat(month + 1)

        weather_data = {
            "temp_max" : data[0]["temp_max"],
            "temp_min" : data[0]["temp_min"],
            "pressure" : data[0]["pressure"],
            "wind" : data[0]["wind"],
            "humidity" : data[0]["humidity"],
            "sunrise" : sunrise,
            "sunset" : sunset,
            "temp_min" : data[0]["temp_max"],
            "date": date
        }

        console.log("waiting")
        $.ajax({
            url: "http://localhost:5000/get_weather_prediction",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"weather_data": weather_data})
        }).done(function(data) {
            console.log(data)


        });
    });
}