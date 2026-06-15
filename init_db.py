import sqlite3

def init_db():
    connection = sqlite3.connect('school.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name VARCHAR(20), 
            surname VARCHAR(20), 
            age INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            student_id INTEGER,
            math_score INTEGER, 
            english_score INTEGER, 
            french_score INTEGER,
            FOREIGN KEY (student_id) REFERENCES student(id)
        )
    ''')
    
    connection.commit()
    connection.close()
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()

