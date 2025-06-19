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
    $('.siri-message').textillate({
        loop: true,
        in: {
            effect: "fadeInUp",
            delayScale: 1.5
        },
        out: {
            effect: "fadeOutUp",
            delayScale: 1.5
        }
    });

    //MicBtn click event
    $("#MicBtn").click(function () {
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.takecommand()((response) => {
            console.log("Command result:", response);
            if (!response) {
                console.log("No response from voice command");
            }
        });

    });

});
