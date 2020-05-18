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

    $(".meal-add-input").keyup(function( event ) {
        type = $(this).data("type")
        inp = $(this).val()

        if (inp.length >= 1){
                $.ajax({
                url: "http://localhost:5000/get_meal_input",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({"inp": inp,})
            }).done(function(data) {
                console.log(data)
                if (data)
                {
                    $("#meal-input-items-"+ type).empty()
                    $("#meal-input-items-"+ type).fadeIn()
                    data.forEach(function(entry, i) {
                        name = entry[1]

                        item = document.createElement("strong");
                        item.className = "meal-input-item";
                        item.setAttribute("data-type", type)
                        item.id = "meal-input-item-" + entry[0];
                        item.innerHTML = name;
                        $("#meal-input-items-"+ type).append(item)
                    })
                }
            });
        }else{
            $(".meal-input-items-"+ type).empty()
            $("#meal-input-items-"+ type).fadeOut()

        }
    })

    $(document).on("click", ".meal-input-item", function() {
        id = $(this).attr("id")
        id = id.replace("meal-input-item-", "")

        type = $(this).data("type")
        gram = $(".gr-"+type).val()


        $("#meal-"+ type).val($(this).html())
        $("#meal-"+ type).attr("data-meal-id", id)
        $("#meal-"+ type).attr("data-meal-gram", gram)
        $(".meal-input-items-"+ type).empty()
        $("#meal-input-items-"+ type).fadeOut()
    })


    $(document).on("click", ".meal-add-button", function() {
        type = $(this).data("type")

        meal_id = $("#meal-"+type).data("meal-id")
        meal_gram = $(".gr-"+type).val()
        alert(meal_gram)
        meal = $("#meal-"+ type).val()
         $.ajax({
            url: "http://localhost:5000/add_meal",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"meal": meal, "meal-id": meal_id, "meal-gram": meal_gram, "type": type})
         }).done(function(data) {
            if (data)
            {
                fill_meal_panel(data)
            }
            else{

            }
        });
    })

})

function get_meals(){
    $.ajax({
            url: "http://localhost:5000/get_meals",
            type: "GET",
         }).done(function(data) {
            if (data)
            {
                console.log(data)
                fill_meal_panel(data)
            }
            else{

            }
        });
}

function fill_meal_panel(data){
    $(".morning-meals").empty();
    $(".evening-meals").empty();
    $(".afternoon-meals").empty();

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

    nutrition_values = data[0]["nutrition"]

    $("#nutrition-kcal").html(nutrition_values["kcal"] + " / " + $("#daily_kcal").html())
    $("#nutrition-carb").html(nutrition_values["carb"] + " / " + $("#daily_kcal").html())
    $("#nutrition-prot").html(nutrition_values["prot"] + " / " + $("#daily_kcal").html())
    $("#nutrition-fat").html(nutrition_values["fat"] + " / " + $("#daily_kcal").html())

}

function check_cal(callback) {
    $.ajax({
        url: "http://localhost:5000/check_cal",
        type: "POST",
    }).done(function(data) {
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



