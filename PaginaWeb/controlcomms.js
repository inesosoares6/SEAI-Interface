function sendToNormalControlMode(){
    fetch('http://localhost:5000/start_normal')
    .then(function (response) {
        return response.json();
    });
}

function sendToPremiumControlMode(){
    fetch('http://localhost:5000/start_premium')
    .then(function (response) {
        return response.json();
    });
}

function sendToControlCancel(){
    fetch('http://localhost:5000/stop')
    .then(function (response) {
        return response.json();
    });
}



