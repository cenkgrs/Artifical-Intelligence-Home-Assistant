$(document).ready(function () {

    film_names = []

    // This gets the film names from the posters folder
    $.ajax({
        url: "http://localhost:5000/get_film_list",
        type: "GET",
    }).done(function(data)
    {
        film_names = data
        fill_library(data)
    });

    // If scroll right button clicked
    $(document).on("click", ".film-scroll-right",function () {
        var x = 0;
        var intervalID = setInterval(function () {

           document.getElementById("films-container").scrollLeft += 20;

           if (++x === 30) {
               window.clearInterval(intervalID);
           }
        }, 10);
    });

    // If scroll left button clicked
    $(document).on("click", ".film-scroll-left",function () {
        var x = 0;
        var intervalID = setInterval(function () {

           document.getElementById("films-container").scrollLeft -= 20;

           if (++x === 30) {
               window.clearInterval(intervalID);
           }
        }, 10);
    });

    // If film poster clicked open the video of this film
    $(document).on("click", ".film-item", function() {
        film_name = $(this).attr("data-film");

        open_video(film_name);
    })

    // When film search input changed
    $(".film-search-input").keyup(function( event ) {
        inp = $(this).val().toLowerCase()
        var films = $(".film-item");

        if (inp.length >= 1){
            film_names.forEach(function(film_name,i){

                var re = new RegExp(inp, 'g');

                if ( film_name.match( film_name.match(re) ) ){
                    $("#film-"+ film_name.replace(/\s/g,'')).fadeIn()
                }else{
                    film_item = "#film-"+ film_name.replace(/\s/g,'')
                    $(film_item).fadeOut()
                }

            })
        }else{
            films.fadeIn()
        }
    });

});

// This function fills film_names array and fill the container with film posters
function fill_library(data){
    $(".films-container").append("<button class='film-scroll-left'></button>");

    data.forEach(function(film_name, i) {
        film_name = film_name.split(".")[0]
        film_names[i] = film_name.toLowerCase()
        film = document.createElement("div");
        film.className = "film-item";
        film.setAttribute("data-film", film_name)
        film.id = "film-" + film_name.replace(/\s/g,'').toLowerCase()
        film.innerHTML = "<img src='static/posters/"+ film_name +".jpg' align='middle' />";
        $(".films-container").append(film)
    })

    $(".films-container").append("<button class='film-scroll-right'></button>");

}

function check_film(text){
    text = text.toLowerCase().split(" ")
    text = text.filter(e => e !== "open");

    isAvailable = false

    text.forEach(function(text_element, i) {

         var re = new RegExp(text_element, 'g');

        film_names.forEach(function(film_name, i) {
            if ( film_name.match( film_name.match(re) ) ){
                isAvailable = true
                film = film_name
                $("#film-"+ film_name.replace(/\s/g,'')).fadeIn()
            }else{
                film_item = "#film-"+ film_name.replace(/\s/g,'')
                $(film_item).fadeOut()
            }
        })
    })

    // If there is a match open the film
    if (isAvailable) {
        speak("This is the film that matches your description sir")
        setTimeout(() => {  speak("I'm opening it now"); open_video(film); }, 4000);
    }else{
        speak("I couldn't find any match for your description sir")
        $(".film-item").fadeIn()
    }
}
