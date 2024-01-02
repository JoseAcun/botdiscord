# Importa la clase Personaje desde el módulo 'caracteristicas'
from caracteristicas import Personaje

# Crear una instancia de la clase Personaje
jugador1 = Personaje(nombre="José", vida=100, energia=100)

# Elección del jugador (corregir la variable 'choice')
choice = "hurt"

# Verifica la elección del jugador y realiza la acción correspondiente
if choice == "hurt":
    jugador1.vida = jugador1.recibir_daño(20)
    # Muestra la vida después de recibir daño
    print(jugador1.vida)