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
            console.log(data)
            if (data)
            {
                console.log(data)
            }
            else{
                //
            }
        });

    })

})

function check_cal() {
    $.ajax({
        url: "http://localhost:5000/check_cal",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(post_data)
    }).done(function(data) {
        console.log(data)
        if (data)
        {
        console.log(data)
        }
        else{
        //
        }
    });
}
