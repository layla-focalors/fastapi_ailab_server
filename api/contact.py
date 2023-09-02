def contact(user):
    import pymysql
    import pandas as pd
    try:
        connection = pymysql.connect(host='localhost', user='root', password='root', database='url',cursorclass=pymysql.cursors.DictCursor)
    except:
        return "connection error"
    querry = f"SLECT * FROM contact_url WHERE NICKNAME = {user};"
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(querry)
            result = cursor.fetchall()
            connection.close()
            if result:
                return result
            else:
                return "raise error"
    except:
        return "querry error"