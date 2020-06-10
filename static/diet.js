$(document).ready(function(){

    var daily_kcal = ""

    // This will work when calorie button clicked -> will take the infos and calculates daily calorie needs
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
            if (data && data["success"] == true)
            {
                data = data["data"]
                console.log(data)
                speak("Thank you for trusting me about your data sir")
                speak("You can be sure that i will only use them for your health")

                daily_kcal = data["kcal"]
                $("#daily_kcal").html(data["kcal"])
                sections.not( $("#diet-section") ).css({"display": "none"})
                $("#calorie-section").fadeOut()
                $("#diet-section").fadeIn()

                get_meals()
            }
            else{
                //
            }
        });

    })

    // This will work when user starts to type a meal name into input -> will bring similar meal names
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
                if (data && data["status"] != false)
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

    // This will work when user click to one of the similar meals and fill the input with it
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

    // This will add a meal to list
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
            if (data && data["status"] != false)
            {
                fill_meal_panel(data)
            }
            else{

            }
        });
    })

    // This will get meal recipe that fits the nutrition needs for that hour
    $(document).on("click", ".meal-get-recipe-button", function(){
        speak("Just a moment sir")

        $(this).fadeOut();
        $(".meal-get-recipe-loading").fadeIn()

            $.ajax({
                url: "http://localhost:5000/get_meal_recommendation",
                type: "GET",
            }).done(function(data) {
                console.log(data)

                if(data["status"]){
                    recipes = data["data"]
                    open_recipes()

                    recipes.forEach(function(recipe, i) {

                        // Creating recipe item
                        recipe_item = document.createElement("div");
                        recipe_item.className = "recipe-item";

                        // Adding recipe name
                        recipe_name = document.createElement("div");
                        recipe_name.className = "recipe-name";
                        recipe_name.innerHTML = recipe["name"];
                        recipe_item.append(recipe_name)

                        // Adding recipe picture
                        recipe_picture = document.createElement("div");
                        recipe_picture.className = "recipe-picture";

                        picture = document.createElement("img");
                        picture.src = recipe["picture"]
                        recipe_picture.append(picture);
                        recipe_item.append(recipe_picture)

                        // Adding ingredients header
                        ingredients_header = document.createElement("h3");
                        ingredients_header.className = "recipes-sub-header";
                        ingredients_header.innerHTML = "Ingredients";
                        recipe_item.append(ingredients_header)

                        // Adding ingredients container and filling it
                        recipe_ingredients_container = document.createElement("div");
                        recipe_ingredients_container.className = "recipe-ingredients";

                        recipe_ingredients = recipe["ingredients"]

                        recipe_ingredients.forEach(function(ingredient, i) {
                            item = document.createElement("strong");
                            item.className = "ingredient";
                            item.innerHTML = "- " + ingredient;
                            recipe_ingredients_container.append(item)
                        })

                        recipe_item.append(recipe_ingredients_container)

                        // Adding directions header
                        directions_header = document.createElement("h3");
                        directions_header.className = "recipes-sub-header";
                        directions_header.innerHTML = "Directions";
                        recipe_item.append(directions_header)

                        // Adding directions container and filling it
                        recipe_directions_container = document.createElement("div");
                        recipe_directions_container.className = "recipe-directions";

                        recipe_directions = recipe["directions"]

                        recipe_directions.forEach(function(direction, i) {
                            item = document.createElement("strong");
                            item.className = "direction";
                            item.innerHTML = "- " + direction;
                            recipe_directions_container.append(item)
                        })

                        recipe_item.append(recipe_directions_container)

                        // Adding recipe item to modal
                        $(".recipe-recommendation-modal").append(recipe_item)
                    })
                }
            });
    })

})

// This is for getting meal and nutrition values from database
function get_meals(){
    $.ajax({
            url: "http://localhost:5000/get_meals",
            type: "GET",
         }).done(function(data) {
            if (data)
            {
                fill_meal_panel(data)
            }
            else{

            }
        });
}

// This function is filling panels with eaten meals and nutrition values
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

    // Get need values from json
    need_values = data[0]["needs"]

    // Get nutrition values from json
    nutrition_values = data[0]["nutrition"]

    kcal = (nutrition_values["kcal"]) ? nutrition_values["kcal"].toFixed(2) : "0.0"
    carb = (nutrition_values["carb"]) ? nutrition_values["carb"].toFixed(2) : "0.0"
    prot = (nutrition_values["prot"]) ? nutrition_values["prot"].toFixed(2) : "0.0"
    fat = (nutrition_values["fat"]) ? nutrition_values["fat"].toFixed(2) : "0.0"

    $("#nutrition-kcal").html(kcal + " / " + need_values["kcal"] + " kcal")
    $("#nutrition-carb").html(carb + " / " + need_values["carb"] + " g")
    $("#nutrition-prot").html(prot + " / " + need_values["prot"] + " g")
    $("#nutrition-fat").html(fat + " / " + need_values["fat"] + " g")

    // 100% nutrition need is 313 px

    // Calculate the height of the nutrition bars
    // Ex :  129,50(current calorie) / 2787 (target calorie) = 0.046.. * 313(full px of nutrition bar) = 14.54.. px (current height of nutrition bar)
    kcal_ratio = ((nutrition_values["kcal"] / need_values["kcal"]) * 313)
    $("#nutritional-kcal-bar").css({"height": kcal_ratio})

    prot_ratio = ((nutrition_values["prot"] / need_values["prot"]) * 313)
    $("#nutritional-prot-bar").css({"height": prot_ratio})

    carb_ratio = ((nutrition_values["carb"] / need_values["carb"]) * 313)
    $("#nutritional-carb-bar").css({"height": carb_ratio})

    fat_ratio = ((nutrition_values["fat"] / need_values["fat"]) * 313)
    $("#nutritional-fat-bar").css({"height": fat_ratio})


}

function check_cal(callback) {
    $.ajax({
        url: "http://localhost:5000/check_cal",
        type: "POST",
    }).done(function(data) {

        if(data["success"] != false){
            data = data["data"]
            daily_kcal = data["kcal"]
            daily_prot = data["prob"]
            daily_carb = data["carb"]
            daily_fat = data["fat"]

            $("#daily_kcal").html(daily_kcal + " Kcal")
            callback(true);
        }else{
            callback(false)
        }

    });
}

function get_meal_input(){
    setTimeout(() => {

        speak(listening_a[Math.floor(Math.random() * listening_a.length)])

        get_listen_input( function(result){
        text = result.split(" ");

        if(text.includes("I-81")){
            console.log(text.indexOf("I-81"))
            text[text.indexOf("I-81")] = "I ate";
        }

        text = text.join(" ");

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
                        console.log(data)
                        if (data && !data["error"])
                        {
                            fill_meal_panel(data)
                            idle_listen()
                        }
                        else{
                            speak("There is an "+ data["error"] + "error sir")
                            speak("Please tell me what did you eat again sir")
                            setTimeout(() => { get_meal_input() }, 2000);
                        }
                    });

            }else{
                speak("If you want to save it just let me know")

            }

        })
        });
    }, 2000);
}



