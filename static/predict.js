$(document).ready(function(){

    $(".modal-radio").on("click", function(){
        console.log("checked")
        if($(this).val() == 1){
            $("#car-predict").fadeToggle()
            $("#house-predict").fadeToggle();
            $(".predict-button").attr("data-predict-type", "house")
        }
        else{
            $("#house-predict").fadeToggle()
            $("#car-predict").fadeToggle();
            $(".predict-button").attr("data-predict-type", "car")

        }

    })

    $(".predict-button").on("click", function(){
        error = 0
        if ($(".predict-button").data("predict-type") == "car"){
            post_data = {
                "brand" : ($("#brand-input").val()) != "" ? $("#brand-input").val() : (speak("Sir please fill all the inputs"), error = 1),
                "year" : $("#year-input").val() != "" ? $("#year-input").val() : (speak("Sir please fill all the inputs"), error = 1),
                "mileage" : $("#mileage-input").val() != "" ? $("#mileage-input").val() : (speak("Sir please fill all the inputs"), error = 1),
                "transmission" : $("#transmission-input").val() != "" ? $("#transmission-input").val() : (speak("Sir please fill all the inputs"), error = 1)
            }
        }else{
        }
        if(error == 1){ return ;}
        $.ajax({
            url: "http://localhost:5000/car_predict",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(post_data)
         }).done(function(data) {
            console.log(data)
            if (data)
            {
                if (!data["success"]){
                    speak("Sir there is and error at the" + data["error_line"] + "you gave me please send me valid" + data["error_line"])

                    return;
                }
                //speak(finish_a[Math.floor(Math.random() * finish_a.length)])
                price = data["price"].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                price = price.split(",")

                speak("I think that this type of car would worth" + price + "US Dollars boss")

                $(".predict-result").fadeIn()
                $(".predict-result").html(data["price"] + " $");


                setTimeout(() => { $(".predict_modal").fadeOut(); $(".predict-result").fadeOut(); $("#index-section").fadeIn() }, 4000);
            }
            else{
                //
            }
        });
    })


})