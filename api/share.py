def sharelink(room_id, USER):
    import pymysql
    import pandas as pd
    try:
        connection = pymysql.connect(host='localhost', user='root', password='root', database='skills',cursorclass=pymysql.cursors.DictCursor)
    except:
        return "connection error"
    query = f"INSERT INTO share VALUES({room_id}, {USER});"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            connection.close()
            return "querry success"
    except:
        return "querry error"