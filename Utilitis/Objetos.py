class objetos:
    def __init__(self, nombre, multiplicador, descripcion, estado, destrezaReq):
            self.nombre = nombre
            self.multiplicador = multiplicador
            self.descripcion = descripcion
            self.estado = estado
            self.destrezaReq = destrezaReq

    @classmethod
    def crearObjeto(cls, nombre, multiplicador, descripcion, estado, destrezaReq):
        return cls(nombre, multiplicador, descripcion, estado, destrezaReq)  
    
    def usarObjeto(self, destreza, roll):
         if destreza < self.destrezaReq:
            if roll == 1:
                self.estado = "Inservible"
            else:
                self.estado = "Dañado"
         return self.estado, roll
        



