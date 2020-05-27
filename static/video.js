$(document).ready(function() {

    var video = document.querySelector(".video");
    var juice = document.querySelector(".white-juice");
    var btn = document.getElementById("play-pause");
    var fullscreen = document.getElementById("fullscreen");

    function togglePlayPause() {
        if(video.paused){
            btn.className="pause";
            video.play();
        }else{
            btn.className="play";
            video.pause();
        }
    }

    $(btn).on("click", function(){
        togglePlayPause()
    });

    $(fullscreen).on("click", function() {
        video.requestFullscreen();
    });


    video.addEventListener("timeupdate", function() {
        var juicePos = video.currentTime / video.duration;
        juice.style.width = juicePos * 100 + "%";

        if(video.ended){
            btn.className = "redo";
        }
    });


})
