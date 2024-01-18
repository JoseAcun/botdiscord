import sqlite3

con = sqlite3.connect("juego.db")
cur = con.cursor()

cur.execute('''
            create table if not exists jugador (
            id integer primary key,
            nombre varchar(45),
            );
            ''')

cur.execute('''CREATE TABLE Objetos (
    ID INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Descripcion TEXT
);''')

cur.execute('''CREATE TABLE Personajes (
    ID INTEGER PRIMARY KEY,
    ID_Jugador INTEGER,
    Nombre TEXT NOT NULL,
    Vida INTEGER NOT NULL,
    Energia INTEGER NOT NULL,
    EstadoAnimo FLOAT NOT NULL,
    FOREIGN KEY (ID_Jugador) REFERENCES Jugador(id)
    );''')

cur.execute('''CREATE TABLE ProgresoJugador (
    ID_Jugador INTEGER,
    ID_Personaje INTEGER,
    Progreso INTEGER,
    FOREIGN KEY (ID_Jugador) REFERENCES Jugadores(id),
    FOREIGN KEY (ID_Personaje) REFERENCES Personajes(ID),
    PRIMARY KEY (ID_Jugador, ID_Personaje));
    ''')
cur.execute('''
CREATE TABLE PersonajeObjeto (
    ID_Jugador INTEGER,
    ID_Personaje INTEGER,
    ID_Objeto INTEGER,
    Cantidad INTEGER,
    FOREIGN KEY (ID_Jugador) REFERENCES Jugadores(ID_Jugador),
    FOREIGN KEY (ID_Personaje) REFERENCES Personajes(ID),
    FOREIGN KEY (ID_Objeto) REFERENCES Objetos(ID),
    PRIMARY KEY (ID_Jugador, ID_Personaje, ID_Objeto)
    );''')

cur.execute('''create table personajesbase(
                ID INTEGER PRIMARY KEY,
                Nombre TEXT NOT NULL,
                Vida INTEGER NOT NULL,
                Energia INTEGER NOT NULL,
                EstadoAnimo FLOAT NOT NULL,
)''')