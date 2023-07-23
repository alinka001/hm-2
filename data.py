import sqlite3

class Database():
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, name TEXT)''')
        self.conn.commit()

    def insert_record(self, id, name):
        self.cursor.execute('''INSERT INTO mytable (id, name) VALUES (?, ?)''', (id, name))
        self.conn.commit()

    def execute_query(self, request):
        self.cursor.execute(request)
        self.conn.commit()

    def print_records(self):
        self.cursor.execute('''SELECT * FROM mytable''')
        out = self.cursor.fetchall()
        print(out)

db = Database()
db.insert_record(1, "John")
db.print_records()
db.execute_query('''UPDATE mytable SET name='Mike' WHERE id=1''')
db.print_records()