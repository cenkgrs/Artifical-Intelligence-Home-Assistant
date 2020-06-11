$(document).ready(function(){

    var music_names = []

    // This gets the film names from the posters folder
    $.ajax({
        url: "http://localhost:5000/get_music_list",
        type: "GET",
    }).done(function(musics)
    {
        console.log("musics are: ", musics)

        musics.forEach(function(index, music){

            music_names.append(music.replace(".mp3", ""));

        })
    });

    var music_bar = document.querySelector('.bar1');
    console.log(music_bar);

    //music_bar.addEventListener('animationiteration', changeAnimation(music_bar), false);

    var music_bars = $(".bar");
    console.log(music_bars);

    // Creating animation for all bars dynamically
    /*var bars_interval = setInterval(function() {

        $.each($(".bar"),function(index, bar){

            changeAnimation(bar);

        })

    }, 2000)*/



})

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

function changeAnimation(music_bar) {
    var startValue = getRandomInt(0, 40);
    music_bar.style.setProperty('--startValue',startValue);
    var endValue = getRandomInt(0, 40);
    music_bar.style.setProperty('--endValue',endValue);

    console.log(startValue, endValue);
}

