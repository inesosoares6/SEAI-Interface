function getPrices(){
    fetch('http://127.0.0.1:5000/prices')
    .then(function (response) {
        return response.json();
    }).then(function (price) {
        document.getElementById("precoNormal").innerHTML = price.normal;
        document.getElementById("precoRapido").innerHTML = price.premium;
    });
}

function charge(mode){
    id = getURLparam();
    if(mode==1){
        location.replace("RapidoCarregamento.html?id="+id);
    }
    else if(mode==2){
        location.replace("NormalCarregamento.html?id="+id);
    }
}

function sendToNormalControlMode(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/normal/'+id)
    .then(function (response) {
    return response.json();
    });
    location.replace("Carregando.html?id="+id);
}

function sendToPremiumControlMode(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/premium/'+id)
    .then(function (response) {
    return response.json();
    });
    location.replace("Carregando.html?id="+id);
}

function goBackWelcomePage(){
    id = getURLparam();
    location.replace("WelcomePage.html?id="+id);
}

function goBackCharging(){
    id = getURLparam();
    location.replace("Carregando.html?id="+id);
}

function stopCharge(){
    id = getURLparam();
    location.replace("Cancelamento.html?id="+id);
}

function goOpeningPage(){
    id = getURLparam();
    location.replace("OpeningPage.html?id="+id);
}

function sendToControlCancel(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/stop/'+id)
    .then(function (response) {
    return response.json();
    });
    location.replace("Terminado.html?id="+id);
}

function checkInterrupt(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/interrupt/'+id)
    .then(function (response) {
        return response.json();
    }).then(function (interruption) {
        if(interruption.flag == 1){
            var modal = document.getElementById("myModal");
            modal.style.display = "block";
        }
        else {
            var modal = document.getElementById("myModal");
            modal.style.display = "none";
        }
    });
}

function checkConnection(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/connection/'+id)
    .then(function (response) {
        return response.json();
    }).then(function (connection) {
        console.log(connection.flag);
        if(connection.flag == 144){
            location.replace("WelcomePage.html?id="+id);
        }
    });
}

function load(){
    var dots = window.setInterval( function() {
        var wait = document.getElementById("wait");
        if ( wait.innerHTML.length > 3 ) 
            wait.innerHTML = "";
        else 
            wait.innerHTML += ".";
        }, 400);
}

function getURLparam(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const id = urlParams.get('id');
    return id;
}