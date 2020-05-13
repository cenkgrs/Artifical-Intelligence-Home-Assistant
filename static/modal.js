$(document).ready(function(){

    $(".modal-radio").on("click", function(){
        console.log("checked")
        if($(this).val() == 1){
            $("#car-predict").css({"display" : "none"})
            $("#house-predict").fadeToggle();
        }
        else{
            $("#house-predict").css({"display" : "none"})
            $("#car-predict").fadeToggle();
        }

    })

    $(".predict-button").on("click", function(){
        brand = $("#brand-input").val()
        year = $("#year-input").val()
        mileage = $("#mileage-input").val()
        transmission = $("#transmission-input").val()

        $.ajax({
            url: "http://localhost:5000/car_predict",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"brand": brand, "year": year, "mileage": mileage, "transmission": transmission})
         }).done(function(data) {

            if (data)
            {
                console.log(data)
                //speak(finish_a[Math.floor(Math.random() * finish_a.length)])

                speak("I think that this type of car would worth" + data["price"] + "US Dollars boss")

            }
            else{
                //
            }
        });
    })


})