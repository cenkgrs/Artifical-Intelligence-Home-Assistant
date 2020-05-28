function get_weather_information(text){
    $.ajax({
        url: "http://localhost:5000/get_weather_information",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"text": text})
     }).done(function(data) {
         console.log(data)
        if (data && data["day"] == "today")
        {
            open_weather()

            data = data["data"][0]
            console.log(data)

            weather_status = data["Status"]
            console.log(weather_status)
            weather_temp = data["Temp"]
            $("#temp").html(weather_temp + "º")

            speak("I think today weather will be" + weather_status + "sir")
            speak("and temperature is " + weather_temp + "degree right now")

            $("#weather-temps").html("<span class='max-temp'> " + data["temp_max"] + "º</span> / " + data["temp_min"] + "º " )
            $("#weather-wind").html("Wind: " + data["wind"] + "km/s")
            $("#weather-humidity").html("Humidity: " + data["humidity"] + "%")
            $("#weather-pressure").html("Pressure: " + data["pressure"])

            setTimeout(() => { open_index(); idle_listen() }, 20000);
        }
        else if(data && data["day"] == "tomorrow"){
            show_predicted_data(data)
        }
    });
}


function show_predicted_data(data){

    open_weather()

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

    setTimeout(() => { open_index(); idle_listen() }, 20000);
}