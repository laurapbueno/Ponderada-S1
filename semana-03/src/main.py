import inquirer 
from pydobot import Dobot
import typer
import sys
from serial.tools.list_ports import comports as list_ports

app = typer.Typer()

class robotLaura:
    def __init__(self):
        available_ports = list_ports()
        print(f'available ports: {[x.device for x in available_ports]}')
        port = available_ports[0].device
        device = Dobot(port=port, verbose=False)
        device.speed(100, 100)
        self.robo = device
        print("Iniciando o robô")

    def mover(self, x, y, z, r, wait=True):
        self.robo.move_to(x, y, z, r)
        print(f"Movendo {x, y, z}")

    def ligar_suck(self):
        self.robo.suck(True)
        print(f"Ligando Atuador")
        
    def desligar_suck(self):
        self.robo.suck(False)
        print(f"Desligando Atuador")

    def coordenadas(self):
        return self.robo.pose()

@app.command(name="CLI")
def CLI():
    roboLaura = robotLaura()
    opcoes = ["casa", "mover", "coordenadas atuais", "ligar suck", "desligar suck", "sair do programa"]
    while True:
        escolhas = [
            inquirer.List("CLI", message="Escolha uma opção:", choices=opcoes)
        ]
        alternativas = inquirer.prompt(escolhas)

        executar(alternativas, roboLaura)

def executar(alternativas, roboLaura):
    alternativas = alternativas["CLI"]
    
    if alternativas == "casa":
        roboLaura.mover(190.41, 33.90, 2.21, 0)
       
    elif alternativas == "mover":
        x = float(typer.prompt("X: "))
        y = float(typer.prompt("Y: "))
        z = float(typer.prompt("Z: "))
        roboLaura.mover(x, y, z, 0, wait=True)
    
    elif alternativas == "coordenadas atuais":
        coordenadas_atuais = roboLaura.coordenadas()
        print(coordenadas_atuais)

    elif alternativas == "ligar suck":
        roboLaura.ligar_suck()

    elif alternativas == "desligar suck":
        roboLaura.desligar_suck()

    elif alternativas == "sair do programa":
        sys.exit()

if __name__ == "__main__":
    app()
