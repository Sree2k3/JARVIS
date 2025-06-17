$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceIn",
        },
    });

    //Siri configuration

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        speed: 0.3,
        amplitude: 1,
        autostart: true
    });

    //Siri message animation
    $('.text1').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeIn",
            sync: true,
        },
        out: {
            effect: "fadeOut",
            sync: true,
        },

    });

    //MicBtn click event
    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.takecommand();
    });

});
