import psycopg2


def execute_sql(db_name, sql):
    if db_name is None:
        conn = psycopg2.connect(user="postgres", password="1", host="127.0.0.1")
    else:
        conn = psycopg2.connect(dbname=db_name, user="postgres", password="1", host="127.0.0.1")

    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(sql)

    try:
        data = cursor.fetchall()
    except:
        data = ''

    cursor.close()
    conn.close()

    return data
