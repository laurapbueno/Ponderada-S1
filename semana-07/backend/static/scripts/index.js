function movimentar() {
    var x;
    var y;
    var z; 

    x = prompt("Digite o valor de x: ");
    y = prompt("Digite o valor de y: ");
    z = prompt("Digite o valor de z: ");


    var dados = {
        x: x,
        y: y,
        z: z
    };

    fetch('/mover', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados),
    })
    alert("Dados para a movimentação enviados com sucesso, confira os logs")
}

function atuadorOn() {
    var flag = {
        flagStatus: 0
    }

    fetch('/atuador', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(flag)
    })
    alert("Dados para ligar o atuador enviados com sucesso, confira os logs")
}

function atuadorOff() {
    var flag = {
        flagStatus: 1
    }

    fetch('/atuador', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(flag)
    })
    alert("Dados para desligar o atuador enviados com sucesso, confira os logs")
}

function home(){
    var home = {
        home: 1
    }

    fetch('/home', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(home)
    })
    alert("Dados para a movimentação até a casa do robo enviados com sucesso, confira os logs")
}
