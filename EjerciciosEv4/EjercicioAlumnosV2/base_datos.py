import sqlite3

def conectar():
    return sqlite3.connect("alumnos.db")


def crear_tabla():
    conexion=conectar()
    cursor= conexion.cursor()
    
    # tabla alumnos
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS alumnos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        curso TEXT NOT NULL
                   )
                   """)
    
    # tabla notas
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS notas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        alumno_id INTEGER NOT NULL,
                        nota REAL NOT NULL,
                        FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
                   )
                   """)
    
    conexion.commit()
    conexion.close()
    
def agregar_alumno(nombre, curso):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO alumnos(nombre, curso)
        VALUES (?, ?)
    """, (nombre, curso))

    conexion.commit()
    conexion.close()
    
def agregar_nota_alumno(alumno_id, nota):
    conexion=conectar()
    cursor=conexion.cursor()
    
    cursor.execute("""
                   INSERT INTO notas(alumno_id, nota)
                   VALUES (?, ?)
                   """, (alumno_id,nota))
    conexion.commit()
    conexion.close()
    
def ver_notas_alumno_db(alumno_id):
    conexion=conectar()
    cursor=conexion.cursor()
    
    cursor.execute("""
                   SELECT nota
                   FROM notas
                   WHERE alumno_id = ?
                   """,(alumno_id,))
    notas=cursor.fetchall()
    conexion.close()
    return notas