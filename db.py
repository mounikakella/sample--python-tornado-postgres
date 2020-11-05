import psycopg2
import psycopg2.extras
import os


class db:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.environ.get('DATABASE'), user=os.environ.get('USER'), password=os.environ.get('PASSWORD'), host=os.environ.get('HOST'), port=os.environ.get('PORT')
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS public.todo (id int NOT NULL, title varchar(32) NULL)")
        self.conn.commit()
