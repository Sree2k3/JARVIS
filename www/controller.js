$(document).ready(function () {
    // Display Speak Message
    eel.expose(Displaymessage)
    function Displaymessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('Start');
    }
    // Display hood
    eel.expose(Showhood)
    function Showhood() {
       $("#Oval").attr("hidden", false);
       $("##Siriwave").attr("hidden", true);
       
    }
    
});

