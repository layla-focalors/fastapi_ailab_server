def rank(user):
    import pymysql
    import pandas as pd
    try:
        connection = pymysql.connect(host='localhost', user='root', password='root', database='rank',cursorclass=pymysql.cursors.DictCursor)
    except:
        return "connection error"
    if user == None:
        querry = f"SLECT * FROM rank;"
        df = pd.read_sql(querry, connection)
    else:
        querry = f"SLECT * FROM rank WHERE NICKNAME = {user};"
        df = pd.read_sql(querry, connection)
    return df