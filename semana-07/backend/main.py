from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
from classes.robot import Robotlaura
from datetime import datetime

app = Flask(__name__)

db = TinyDB("db/logs.json")

comandos_table = db.table("logs")

agora = datetime.now()


robo = Robotlaura()

from flask import jsonify 

@app.route('/mover', methods=['POST'])
def mover():
    dados = request.json

    x = dados.get('x')
    y = dados.get('y')
    z = dados.get('z')

    robo.mover_para(x, y, z)

    print(f'movendo para a posição {x}, {y}, {z}')


    evento = agora.strftime("%d/%m/%Y %H:%M:%S")
    db.insert({"comando": "movimento", "evento": evento})
    return jsonify({'message': f'Movendo para a posição {x}, {y}, {z}'}), 200

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/atuador', methods=['POST']) 
def atuador():
    flag = request.json
    flagStatus = flag.get('flagStatus')

    if flagStatus == 0:
        robo.ativar_ferramenta()
        evento = agora.strftime("%d/%m/%Y %H:%M:%S")
        db.insert({"comando": "ligar atuador", "evento": evento})
        print("ativando o atuador")
        return jsonify({'message': 'Atuador ativado'}), 200
    elif flagStatus == 1:
        robo.desativar_ferramenta()
        evento = agora.strftime("%d/%m/%Y %H:%M:%S")
        db.insert({"comando": "desligar atuador", "evento": evento}) 
        print("desligando ferramenta")
        return jsonify({'message': 'Atuador desativado'}), 200

@app.route('/home', methods=['POST'])
def home():
    home = request.json
    goHome = home.get('home')

    if goHome == 1:
        robo.mover_para(243.84, 5.12, 157.94, 0)
        evento = agora.strftime("%d/%m/%Y %H:%M:%S")
        db.insert({"comando": "indo para casa", "evento": evento})
        print('indo para casa')
        return jsonify({'message': 'Indo para casa'}), 200
    else:
        evento = agora.strftime("%d/%m/%Y %H:%M:%S")
        db.insert({"comando": "não fui para casa", "evento": evento})
        print('não foi possível voltar para casa')
        return jsonify({'message': 'Não foi possível voltar para casa'}), 400

@app.route('/logs', methods=['GET'])
def mostrar_logs():
    logs = db.all()
    return render_template('logs.html', logs=logs)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
