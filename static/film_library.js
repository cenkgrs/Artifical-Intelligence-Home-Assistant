$(document).ready(function () {

    film_names = []

    $.ajax({
        url: "http://localhost:5000/get_film_list",
        type: "GET",
    }).done(function(data)
    {
        console.log(data)
        film_names = data
        fill_library(data)
    });

    $(document).on("click", ".film-scroll-right",function () {
        var x = 0;
        var intervalID = setInterval(function () {

           document.getElementById("films-container").scrollLeft += 20;

           if (++x === 30) {
               window.clearInterval(intervalID);
           }
        }, 10);
    });

    $(document).on("click", ".film-scroll-left",function () {
        var x = 0;
        var intervalID = setInterval(function () {

           document.getElementById("films-container").scrollLeft -= 20;

           if (++x === 30) {
               window.clearInterval(intervalID);
           }
        }, 10);
    });

    $(document).on("click", ".film-item", function() {
        film_name = $(this).attr("id");
        film_name = film_name.replace("film-", "");

        open_video(film_name);
    })

    $(".film-search-input").keyup(function( event ) {
        inp = $(this).val()
        var films = $(".film-item");

        if (inp.length >= 1){
            film_names.forEach(function(film_name,i){

                var re = new RegExp(inp, 'g');

                if ( film_name.match( film_name.match(re) ) ){
                    alert("matched:" + film_name)
                    $("#film-"+ film_name).fadeIn()
                }else{
                    film_item = "#film-"+ film_name
                    alert("unmatched:" + film_name)
                    $(film_item).fadeOut()
                }

            })
        }else{
            films.fadeIn()
        }
    });

});

function fill_library(data){
    $(".films-container").append("<button class='film-scroll-left'></button>");

    data.forEach(function(film_name, i) {
        film_name = film_name.split(".")[0]
        film_names[i] = film_name
        film = document.createElement("div");
        film.className = "film-item";
        film.id = "film-" + film_name;
        film.innerHTML = "<img src='static/posters/"+ film_name +".jpg' align='middle' />";
        $(".films-container").append(film)
    })
    console.log(film_names)
    $(".films-container").append("<button class='film-scroll-right'></button>");

}
