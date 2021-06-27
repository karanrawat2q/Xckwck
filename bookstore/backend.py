import sqlite3

class Database:
    
    
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor() # now this is an attribute of class
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER )")
        self.conn.commit()

    def insert(self, title, author, year, isbn):       
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()

    def view(self):       
        self.cur.execute("SELECT * FROM book") # cur is attribute of object Database class
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""): # each variable is assign to an empty string if user ask for a author name it will either search for empty string or author name and doesnt give any error
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()


    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):  # So before script exist this method will executed
        self.conn.close()

# insert("The Maggi", "imman inzuaza", 1911, 123455175)
# delete(2)
# update(4, "The Moon", "John Smooth", 1879, 12345678)
# print(view())

# print(search(author="Misd inzuaza"))