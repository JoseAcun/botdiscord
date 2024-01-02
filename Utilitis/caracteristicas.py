class Personaje:
    def __init__(self, nombre, vida, energia):
        self.nombre = nombre
        self.vida = vida
        self.energia = energia

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0