//setTimeout(() => { play_intro_music() }, 2000);


var oracleType = "index" // oracleType is a global variable that oracle using to understand where he commands come from
var clockAvailable = false
var didClocked = false
showTime();
showWeather();
get_last_emails();

check_cal(function(result){
    return;
})

clockAvailable = checkClock()

// If we are not in special hour like morning, evening
if ( ! clockAvailable ){

    //speak(greetings_a[Math.floor(Math.random() * greetings_a.length)]);
}else{
    didClocked = true
    if( 6 <= h < 10 ){ speak("It is currently " + h + " o'clock sir" );  speak(morning_a[Math.floor(Math.random() * morning_a.length)]); }
    else if ( h == 12 ) { speak("It is currently " + h + " o'clock sir" ); speak(afternoon_a[Math.floor(Math.random() * afternoon_a.length)]); }
    else if ( h == 18 ) { speak("It is currently " + h + " o'clock sir" ); speak(evening_a[Math.floor(Math.random() * evening_a.length)]); }

}

setInterval(function(){
    clockAvailable = checkClock() // Returns hour if there is a special message for current hour

    if(clockAvailable && !didClocked){
        didClocked = true
        if( h == 9 ){ speak("It is currently " + h + " o'clock sir" );  speak(morning_a[Math.floor(Math.random() * morning_a.length)]); }
        else if ( h == 12 ) { speak("It is currently " + h + " o'clock sir" ); speak(afternoon_a[Math.floor(Math.random() * afternoon_a.length)]); }
        else if ( h == 18 ) { speak("It is currently " + h + " o'clock sir" ); speak(evening_a[Math.floor(Math.random() * evening_a.length)]); }


    }

}, 300000)


update_waketime()

idle_listen()
//speak("If you want anything for me to do just click one of the links and i'll do the rest");

//speak("For starters hour is " + h + " " + m)
//speak("And today is " + day + " " + month)
//speak("If you need anything i'm here sir ")



