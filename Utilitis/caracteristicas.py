class Personaje:
    def __init__(self, nombre, vida, energia, EstadoAnimo, destreza):
        self.nombre = nombre
        self.vida = vida
        self.energia = energia
        self.EstadoAnimo = EstadoAnimo
        self. destreza = destreza

    def Mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Energia: {self.energia}")
        print(f"Estado Animo: {self.EstadoAnimo}")
        print(f"Destreza: {self.destreza}")

    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
        return(self.vida)
    
    def usar_energia(self, cansancio):
        self.energia -= cansancio
        if self.energia < 0:
            self.energia = 0
        return(self.energia)
    
