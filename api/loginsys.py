def login(database, useremail, userpassword):
    import datetime
    import pymysql
    query = f"SELECT * FROM {database} WHERE useremail = '{useremail}' AND userpassword = '{userpassword}';"
    if useremail == "" or userpassword == "":
        return "empty error! please input your email or password"
    if useremail == None or userpassword == None:
        return "empty error! please input your email or password"
    try:
        connection = pymysql.connect(host='localhost', user='root', password='root', database='login',cursorclass=pymysql.cursors.DictCursor)
    except:
        return "connection error"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            connection.close()
            if result:
                return True
            else:
                return False
    except:
        return "querry error"