import pymysql.cursors

def createConnectionDB()->any:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Tech1208$tar",
        database="flaskapp",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def insertNewPerson(persona):
    connection = createConnectionDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO 'flaskapp'.'users' ('name','email') VALUES(%s,%s);"
            cursor.execute(sql, (0, persona.name,persona.email))
        connection.commit()
        