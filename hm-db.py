import sqlite3


class Data:
    def __init__ (self, data):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        

    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE tab(id INTEGER PRIMARY KEY, name TEXT)''')
            self.conn.commit()                                   
        except (sqlite3.OperationalError) :
            print('Таблица уже существует')

    def insert(self, id, name):
        try:
            self.cursor.execute('''INSERT INTO tab(id, name) VALUES (? , ?)''', (id, name))
            self.conn.commit()
        except (sqlite3.IntegrityError):
            print("Такой id уже существует")
    
    def update(self, id, name):
        self.cursor.execute('''UPDATE tab SET name = (?) WHERE id = (?) ''', (name,id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('''DELETE FROM tab WHERE id = (?)''', (id,))  
        self.conn.commit()

    def out(self):
        self.cursor.execute('''SELECT * FROM tab''')
        o = self.cursor.fetchall()  
        return o

    def delete_all(self):
        self.cursor.execute('''DELETE FROM tab''')
        self.conn.commit()

data = Data('data.db')
data.create_table()
data.insert(1, "alina")
data.insert(2, "nastya")
print(data.out(), "создали две записи")

#data.insert(1, "katya")

data.update(1, "katya")
print(data.out(), "заменили первую запись")

data.delete(2)
print(data.out(), "удалили вторую запись")

data.delete_all()
print(data.out(), "удалили всё")

