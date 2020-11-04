import psycopg2
import psycopg2.extras


# def connect():
#     conn = psycopg2.connect(database="postgres", user="postgres",
#                             password="postgres", host="localhost", port=5432)
#     cursor = conn.cursor()
#     cursor.execute(
#         "CREATE TABLE IF NOT EXISTS public.todo (id int NOT NULL, title varchar(32) NULL)")
#     conn.commit()
#     return {'cursor': cursor, 'conn': conn}


# if __name__ == '__main__':
#     print('Dont want to connect to DB')
# else:
#     connect()


class db:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="postgres", user="postgres", password="postgres", host="localhost", port=5432)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS public.todo (id int NOT NULL, title varchar(32) NULL)")
        self.conn.commit()
