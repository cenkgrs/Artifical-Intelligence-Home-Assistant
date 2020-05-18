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

    $(".meal-add-input").keypress(function( event ) {
        alert("changed")

    })

    $(document).on("click", ".meal-add-button", function() {
        console.log($(this))
        type = $(this).data("type")

        meal = $("#meal-"+ type).val()
        console.log(meal, type)
         $.ajax({
            url: "http://localhost:5000/add_meal",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"meal": meal, "type": type})
         }).done(function(data) {
            console.log(data)
            if (data)
            {
                fill_panel(data)
            }
            else{

            }
        });
    })

})

function get_meals(){
    console.log("worked")
    $.ajax({
            url: "http://localhost:5000/get_meals",
            type: "GET",
         }).done(function(data) {
            console.log(data)
            if (data)
            {
                fill_panel(data)
            }
            else{

            }
        });
}

function fill_panel(data){
    $(".morning-meals").empty();
    $(".evening-meals").empty();
    $(".afternoon-meals").empty();
    console.log(data)
    console.log(data[0])
    console.log(data["morning"])
    console.log(data[0]["morning"])
    morning_meals = data[0]["morning"]

    morning_meals.forEach(function(entry, i) {
        item = document.createElement("strong");
        item.className = "meal-item";
        item.id = "morning-meal-" + i;
        item.innerHTML = (i = i + 1) + " - " + entry;
        $(".morning-meals").append(item)
    })

    evening_meals = data[0]["evening"]

    evening_meals.forEach(function(entry, i) {
        item = document.createElement("strong");
        item.className = "meal-item";
        item.id = "evening-meal-" + i;
        item.innerHTML = (i = i + 1) + " - " + entry;
        $(".evening-meals").append(item)
    })

    afternoon_meals = data[0]["afternoon"]

    afternoon_meals.forEach(function(entry, i) {
        item = document.createElement("strong");
        item.className = "meal-item";
        item.id = "afternoon-meal-" + i;
        item.innerHTML = (i = i + 1) + " - " + entry;
        $(".afternoon-meals").append(item)
    })
}

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



