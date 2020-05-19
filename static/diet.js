$(document).ready(function(){

    var daily_kcal = ""

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
                if (data && data != null)
                {
                    console.log(data)
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

    $("#nutrition-kcal").html(nutrition_values["kcal"].toFixed(2) + " / " + daily_kcal)
    $("#nutrition-carb").html(nutrition_values["carb"].toFixed(2) + " / " + 175)
    $("#nutrition-prot").html(nutrition_values["prot"].toFixed(2) + " / " + 75)
    $("#nutrition-fat").html(nutrition_values["fat"].toFixed(2) + " / " + 35)

    // 100% nutrition need is 313 px

    // Ex :  129,50(current calorie) / 2787 (target calorie) = 0.046.. * 313(full px of nutrition bar) = 14.54.. px (current height of nutrition bar)
    kcal_ratio = ((nutrition_values["kcal"] / daily_kcal) * 313)
    $("#nutritional-kcal-bar").css({"height": kcal_ratio})

    prot_ratio = ((nutrition_values["prot"] / 75) * 313)
    $("#nutritional-prot-bar").css({"height": prot_ratio})

    carb_ratio = ((nutrition_values["carb"] / 175) * 313)
    $("#nutritional-carb-bar").css({"height": carb_ratio})

    fat_ratio = ((nutrition_values["fat"] / 35) * 313)
    $("#nutritional-fat-bar").css({"height": fat_ratio})


}

function check_cal(callback) {
    $.ajax({
        url: "http://localhost:5000/check_cal",
        type: "POST",
    }).done(function(data) {
        if (data)
        {
            if(data["kcal"] != ""){
                daily_kcal = data["kcal"]
                $("#daily_kcal").html(daily_kcal + " Kcal")
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

function get_meal_input(){
    setTimeout(() => {

        speak(listening_a[Math.floor(Math.random() * listening_a.length)])

        get_listen_input( function(result){
        console.log(result)
        text = result
        speak("Should i save this sir ?")
        $("#todo-body").val(result)
        get_listen_input( function (result) {

            if(confirm_q.includes(result)){
                    speak(complete_a[Math.floor(Math.random() * complete_a.length)])
                    $.ajax({
                        url: "http://localhost:5000/add_meal_natural",
                        type: "POST",
                        contentType: "application/json",
                        data: JSON.stringify({"text": text})
                    }).done(function(data) {
                        if (data)
                        {
                            fill_meal_panel(data)
                        }
                        else{
                            speak("There is an "+ data["error"] + "sir")
                        }
                    });

            }else{
                speak("If you want to save it just let me know")

            }

        })
        });
    }, 2000);
}



