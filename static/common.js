function speak(text){
    const msg = new SpeechSynthesisUtterance(text);
    msg.volume = 1; // 0 to 1
    msg.rate = 1; // 0.1 to 10
    msg.pitch = 0.8; // 0 to 2

    const voice = speaks[0]; //47
    console.log(`Voice: ${voice.name} and Lang: ${voice.lang}`);
    msg.voiceURI = voice.name;
    msg.lang = voice.lang;


    speechSynthesis.speak(msg);
}

function listen(){
    //recognition = window.speechRecognition || window.webkitSpeechRecognition;

    window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
    let finalTranscript = '';
    let recognition = new window.SpeechRecognition();

    recognition.interimResults = true;
    recognition.maxAlternatives = 10;
    recognition.continuous = true;

    recognition.onresult = (event) => {
      let interimTranscript = '';
      for (let i = event.resultIndex, len = event.results.length; i < len; i++) {
        let transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          finalTranscript += transcript;
        } else {
          interimTranscript += transcript;
        }
      }
       document.getElementById('user-input').innerHTML = finalTranscript + '<i style="color:#ddd;">' + interimTranscript + '</>';
    }
    recognition.start();
    setTimeout(() => {  recognition.stop }, 4000);

    recognition.onspeechend = function() {
      recognition.stop();
      console.log(finalTranscript);

      speak("You said" + finalTranscript);
    }

}