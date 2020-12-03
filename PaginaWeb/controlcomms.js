function sendToNormalControlMode(){
    fetch('http://127.0.0.1:5000/normal')
    .then(function (response) {
    return response.json();
    });
}

function sendToPremiumControlMode(){
    fetch('http://127.0.0.1:5000/premium')
    .then(function (response) {
    return response.json();
    });
}

function sendToControlCancel(){
    fetch('http://127.0.0.1:5000/stop')
    .then(function (response) {
    return response.json();
    });
}

function checkInterrupt(){
    fetch('http://127.0.0.1:5000/interrupt')
    .then(function (response) {
        return response.json();
    }).then(function (interruption) {
        if(interruption.flag == 5){
            var modal = document.getElementById("myModal");
            modal.style.display = "block";
        }
        else {
            var modal = document.getElementById("myModal");
            modal.style.display = "none";
        }
    });
}