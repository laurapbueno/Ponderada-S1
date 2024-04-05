from pydobot import Dobot
from serial.tools.list_ports import comports

class Robotlaura:
    # Iniciando o robô
    def __init__(self):
        available_ports = list_ports()
        print(f'available ports: {[x.device for x in available_ports]}')
        port = available_ports[0].device
        device = Dobot(port=port, verbose=False)
        device.speed(100, 100)
        self.robo = device
        print("Iniciando o robô")

    # Identificar a posição atual do robô
    def posição_atual(self):
        return self.robo.pose()

    # Mover o robô para uma posição definida
    def mover_para(self, x, y, z, r, wait=True):
        self.robo.move_to(x, y, z, r)

    # Ligar a ferramenta
    def ativar_ferramenta(self):
        self.robo.suck(True)
    
    # Desligar a ferramenta 
    def desativar_ferramenta(self):
        self.robo.suck(False)