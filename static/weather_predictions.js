function predict_weather(){

    // This request will get today's weather information
     message = "",
     $.ajax({
        url: "http://localhost:5000/weather",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"message": message})
    }).done(function(data) {
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

        // Sending today's weather data for prediction
        $.ajax({
            url: "http://localhost:5000/get_weather_prediction",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"weather_data": weather_data})
        }).done(function(data) {
            condition = data["data"][0]["condition"]

            speak("I think weather will be" + condition + "tomorrow sir")
            speak("Maximum temperature will be " + data["data"][0]["max_temp"] + "degree and minimum temperature will be "+ data["data"][0]["min_temp"] + "degree")
            speak("And the wind will be "+ data["data"][0]["wind"] + "kilometer per hour alongside with " + data["data"][0]["humidity"] +
                    "percent of humidity and" + data["data"][0]["pressure"] + "pressure")

            // Filling modal with tomorrow's predicted weather data
            $("#weather-temps").html("<span class='max-temp'> " + data["data"][0]["max_temp"] + "º</span> / " + data["data"][0]["min_temp"] + "º " )
            $("#weather-wind").html("Wind: " + data["data"][0]["wind"] + "km/s")
            $("#weather-humidity").html("Humidity: " + data["data"][0]["humidity"] + "%")
            $("#weather-pressure").html("Pressure: " + data["data"][0]["pressure"])

            // Filling the weather condition animation
            if( cloud.includes(condition) ){
                $(".weather-condition-svg").attr("src","/static/animated/cloudy.svg");
            }else if (sunny.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/day.svg");
            }else if (partly_cloud.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/cloudy-day-1.svg");
            }else if (partly_rain.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/rainy-3.svg");
            }else if (light_rain.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/rainy-4.svg");
            }else if (moderate_rain.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/rainy-5.svg");
            }else if (heavy_rain.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/rainy-6.svg");
            }else if (moderate_snow.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/snowy-4.svg");
            }else if (heavy_snow.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/snowy-6.svg");
            }else if (rain_snow.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/rainy-4.svg");
            }else if (rain_snow_m.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/snowy-5.svg");
            }else if (thunder.includes(condition)){
                $(".weather-condition-svg").attr("src","/static/animated/thunder.svg");
            }

        setTimeout(() => { open_index() }, 20000);
        });
    });
}