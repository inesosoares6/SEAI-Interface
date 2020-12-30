function getPrices(){
    id = getURLparam();    
    fetch('http://127.0.0.1:5000/prices/'+id)
    .then(function (response) {
        return response.json();
    }).then(function (price) {
        document.getElementById("precoNormal").innerHTML = price.normal;
        document.getElementById("precoRapido").innerHTML = price.premium;
        document.getElementById("precoVerde").innerHTML = price.green;
    });
}

function getTotalPrice(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/finalprice/'+id)
    .then(function (response) {
        return response.json();
    }).then(function (price) {
        document.getElementById("precoTotal").innerHTML = price.total;
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
    else if(mode==3){
        location.replace("VerdeCarregamento.html?id="+id);
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

function sendToGreenControlMode(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/green/'+id)
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

function goEndMenu(){
    id = getURLparam();
    location.replace("OpeningPage.html?id="+id);
}

function checkInterrupt(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/interrupt/'+id)
    .then(function (response) {
        return response.json();
    }).then(function (interruption) {
        if(interruption.flag == true){
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
        if(connection.flag == 1){
            location.replace("WelcomePage.html?id="+id);
        }
    });
}

function checkFinish(){
    id = getURLparam();
    fetch('http://127.0.0.1:5000/finish/'+id)
    .then(function (response) {
        return response.json();
    }).then(function (finish) {
        if(finish.flag == 1){
            location.replace("Terminado.html?id="+id);
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