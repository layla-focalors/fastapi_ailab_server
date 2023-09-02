def connect(database, useremail, userpassword):
    import datetime
    import pymysql
    if useremail == "" or userpassword == "":
        return "empty error! please input your email or password"
    if useremail == None or userpassword == None:
        return "empty error! please input your email or password"
    try:
        connection = pymysql.connect(host='localhost', user='root', password='root', database='login',cursorclass=pymysql.cursors.DictCursor)
    except:
        return "connection error"
    time = str(datetime.datetime.now())
    querry = f"INSERT INTO {database} VALUES({time}, {useremail}, {userpassword});"
    try:
        with connection.cursor() as cursor:
            cursor.execute(querry)
            connection.commit()
            connection.close()
            return "querry success"
    except:
        return "querry error"