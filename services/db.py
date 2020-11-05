import psycopg2
import psycopg2.extras


class Dbservice:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="postgres", user="postgres", password="postgres", host="localhost", port=5432)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS public.todo (id int NOT NULL, title varchar(32) NULL)")
        self.conn.commit()
