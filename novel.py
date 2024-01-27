import random
class game:
    def __init__(self, historia, oportunidad, final, hora, tiempoActual) -> None:
        self.historia = historia
        self.oportunidad = oportunidad
        self.final = final
        self.hora = hora
        self.tiempoActual = tiempoActual

    def novela(self):
        pass

    def Tiempo(self, hora):
        self.tiempoActual += hora

    def roll(dice = 6):
        return random.randint(1, dice)
    
