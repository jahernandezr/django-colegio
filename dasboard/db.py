from django.db import connection


def ejecutar_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)

        if cursor.description:
            columnas = [col[0] for col in cursor.description]
            filas = cursor.fetchall()

        else:
            columnas = []
            filas = []
            
    return  columnas, filas