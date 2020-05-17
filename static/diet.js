$(document).ready(function(){

    $(".calorie-button").on("click", function() {
        console.log($("#age-input").val())
        post_data = {
            "gender": document.querySelector('input[name="gender"]:checked').value,
            "activity": document.querySelector('input[name="activity"]:checked').value,
            "aim": document.querySelector('input[name="aim"]:checked').value,
            "height": $("#height-input").val(),
            "weight": $("#weight-input").val(),
            "age": $("#age_input").val()
        }

        $.ajax({
            url: "http://localhost:5000/calculate_cal",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(post_data)
         }).done(function(data) {
            if (data)
            {
                console.log(data)
                speak("Thank you for trusting me about your data sir")
                speak("You can be sure that i will only use them for your health")

                $("#daily_kcal").html(data["kcal"])
                sections.not( $("#diet-section") ).css({"display": "none"})
                $("#calorie-section").fadeOut()
                $("#diet-section").fadeIn()
            }
            else{
                //
            }
        });

    })

})

function check_cal(callback) {
    $.ajax({
        url: "http://localhost:5000/check_cal",
        type: "POST",
    }).done(function(data) {
        console.log(data)
        if (data)
        {
            if(data["kcal"] != ""){
                $("#daily_kcal").html(data["kcal"])
                callback(true);
            }else{
                callback(false)
            }
        }
        else{
        //
        }
    });
}
