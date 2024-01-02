import sqlite3

con = sqlite3.connect("juego.db")
cur = con.cursor()

cur.execute('''
            create table if not exists jugador (
            id integer primary key,
            nombre varchar(45),
            partida int
            )
            ''')