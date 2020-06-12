music_state = "pause";

$(document).ready(function(){
    let last_music_index = 0;
    var music_names = []
    var music_playlist = []
    var music_bars = $(".bar");

    // This gets the film names from the posters folder
    $.ajax({
        url: "http://localhost:5000/get_music_list",
        type: "GET",
    }).done(function(musics)
    {
        musics.forEach(function(music, index){
            music_names.push(music.replace(/\-/g, ' ').replace(".mp3", ""));

            music_playlist.push("../static/audio/"+ music)

        })
    });

    // This will open or close the music list
    $(document).on("click", "#open_music_list", function(){

        // If music list open set class closed
        if ($('.player_music_list').css('opacity') == 1){
            $(".player_music_list").addClass("closed-list")
            $(".player_music_list").removeClass("opened-list");
            return;
        }

        // If music list is closed, open it
        $(".player_music_list").addClass("opened-list")
        $(".player_music_list").empty()

        // For every music that got from files add a music item
        music_names.forEach(function(music, index){
            let song_icon = document.createElement("i");
            song_icon.className= "fa fa-music";

            let music_name = document.createElement("strong");
            music_name.innerHTML = music;

            let music_item = document.createElement("div");
            music_item.className = "music-item";

            music_item.appendChild(song_icon);
            music_item.appendChild(music_name);


            $(".player_music_list").append(music_item);
        })
    })

    // When music from music list selected
    $(document).on("click", ".music-item", function(){
        $("audio").empty()

        // Get the text value of music item
        selected_music = $(this)[0].children[1].textContent

        // Set last index to this music
        last_music_index = music_names.indexOf(selected_music)

        // Get music's path from array created earlier
        music_path = music_playlist[last_music_index]

        // Set state to resume
        music_state = "resume"

        play_music(music_path, selected_music)

    })

    $(document).on("click", ".music_play_button", function(){
        $("audio").empty()

        button_type = $(this).data("type")
        if (button_type == "next_music"){
            inc = 1
        }else if(button_type == "previous_music"){
            inc = -1
        }else{
            pause_play(music_state)
            return;
        }

        // Getting last music's index and adding/removing 1 index to/from it
        last_music_index = last_music_index + inc
        music_path = music_playlist[(last_music_index)]

        // Getting that music's name
        index = music_playlist.indexOf(music_path)
        selected_music = music_names[index]

        // Set state to resume
        music_state = "resume"

        play_music(music_path, selected_music)

    })

    // Creating animation for all bars dynamically
    /*var bars_interval = setInterval(function() {

        $.each($(".bar"),function(index, bar){

            changeAnimation(bar);

        })

    }, 2000)*/

})

// This is for playing music with music path and music's name parameters
function play_music(music_path, selected_music){

    if (!music_path && !selected_music){
        alert("played")
        $(".audio-stop").fadeIn();
        $(".my_audio").trigger('play');

        return;
    }

    $(".my_audio").trigger('pause');
    $(".my_audio").prop("currentTime",0);

    $('.my_audio').append("<source id='sound_src' src=" + music_path + " type='audio/mpeg'>");
    $(".my_audio").trigger('load');
    $(".audio-stop").fadeIn();

    $(".my_audio").trigger('play');

    $(".info__album").html( (selected_music.split(" "))[0] + " " + (selected_music.split(" "))[1])
    $(".info__song").html(selected_music)
    $(".info__artist").html( (selected_music.split(" "))[0] + " " + (selected_music.split(" "))[1])

}

// This function will resume or pause the music, depending on the state
function pause_play(music_state){
    alert(music_state)
    if (music_state == "resume"){
        $(".audio-stop").fadeToggle();
        $(".my_audio").trigger('pause');

        music_state = "pause"
    }else{
        play_music(null, null)
    }
}

// This will return random numner from given interval
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}

// This will change the animation of bars in music player
function changeAnimation(music_bar) {
    var startValue = getRandomInt(0, 40);
    music_bar.style.setProperty('--startValue',startValue);
    var endValue = getRandomInt(0, 40);
    music_bar.style.setProperty('--endValue',endValue);

    console.log(startValue, endValue);
}

