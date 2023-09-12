import sqlite3
class conexion:
    db_name = "base.db"

    @classmethod
    def ejecutar(self, sql, parametros = ()):
        with sqlite3.connect(self.db_name) as con:
            cursor = con.cursor()
            resultado = cursor.execute(sql, parametros)
            con.commit
        if sql.upper().startswith('SELECT',0):
            data = cursor.fetchall()
            con.close()
            return data
        else:
            con.close()
            return resultado
