import pymysql
class conexion:
    
    @classmethod
    def ejecutar(self, sql, parametros = ()):
        with pymysql.connect(host="localhost", user="root", passwd="", db="base") as con:
            cursor = con.cursor()
            resultado = cursor.execute(sql, parametros)
            con.commit
        if sql.upper().startswith('SELECT',0):
            data = cursor.fetchall()
            
            return data
        else:
            
            return resultado
