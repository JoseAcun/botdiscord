## Instrucciones de instalación

1. Clona el repositorio
2. te recomiendo crear un nuevo entorno con el comando python -m venv "nombre_del_entorno" (opcional)
3. accede al entorno por medio del comando "nombre_del_entorno\Scripts\activate" si estas en Windows
en linux seria: "source nombre_del_entorno/bin/activate"
4. ejecuta "pip install -r requirements.txt" para instalar la lista de deppendencias requeriadas para el proyecto

Nota: recuerda desativar el entorno cuando no lo estes usando con el comando "deactivate" y activarlo al volver

basicamente ahora mismo se esta trabajando en una novela interactiva con varias opciones de personajes (de momento solo los 4 minimos) cada uno con cualidades que le van a dar ciertas estadisticas para afrontar la situacion, tambien se quiere implementar una base de datos que almacene todas las caracteristicas de los personajes y de la partida asi como de quien este jugando para tener un guardado de partida basico con sqlite3 el guion se escribira por partes en archivos de texto que seran llamados segun las desciciones del jugador
