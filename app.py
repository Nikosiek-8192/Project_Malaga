from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_FILE = 'school.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    
    query = '''
        SELECT s.id, s.name, s.surname, s.age, 
               (g.math_score + g.english_score + g.french_score) / 3.0 AS overall_average
        FROM student s
        JOIN grades g ON s.id = g.student_id
    '''
    students_list = conn.execute(query).fetchall()
    
    total = len(students_list)
    
    avg_row = conn.execute('''
        SELECT AVG((math_score + english_score + french_score) / 3.0) as sys_avg 
        FROM grades
    ''').fetchone()
    system_average = round(avg_row['sys_avg'], 2) if avg_row['sys_avg'] else 0
    
    excellent = 0
    fail = 0
    for s in students_list:
        if s['overall_average'] > 79:
            excellent += 1
        elif s['overall_average'] < 50:
            fail += 1

    searched_student = None
    search_error = request.args.get('search_error')
    search_id = request.args.get('search_id')
    
    if search_id:
        search_query = '''
            SELECT s.name, s.surname, g.math_score, g.english_score, g.french_score,
                   ((g.math_score + g.english_score + g.french_score) / 3.0) as avg
            FROM student s
            JOIN grades g ON s.id = g.student_id
            WHERE s.id = ?
        '''
        searched_student = conn.execute(search_query, (search_id,)).fetchone()

    conn.close()
    
    return render_template(
        "SMS.html", 
        students=students_list, 
        total=total, 
        excelent=excellent, 
        fail=fail, 
        average=system_average,
        searched_student=searched_student,
        search_error=search_error
    )

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form.get('name')
    surname = request.form.get('surname')
    age = request.form.get('age')
    math = request.form.get('math_score')
    english = request.form.get('english_score')
    french = request.form.get('french_score')
    
    if name and surname and age:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute(
            'INSERT INTO student (name, surname, age) VALUES (?, ?, ?)',
            (name, surname, int(age))
        )

        student_id = cursor.lastrowid
        
        cursor.execute(
            'INSERT INTO grades (student_id, math_score, english_score, french_score) VALUES (?, ?, ?, ?)',
            (student_id, int(math), int(english), int(french))
        )
        
        conn.commit()
        conn.close()
        
    return redirect(url_for('home'))

@app.route('/search_student', methods=['POST'])
def search_student():
    search_name = request.form.get('search_name', '').strip()
    
    conn = get_db_connection()
    row = conn.execute('SELECT id FROM student WHERE name = ?', (search_name,)).fetchone()
    conn.close()
    
    if row:
        return redirect(url_for('home', search_id=row['id']))
    else:
        return redirect(url_for('home', search_error=f"Student '{search_name}' not found."))

@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM grades WHERE student_id = ?', (student_id,))
        
        cursor.execute('DELETE FROM student WHERE id = ?', (student_id,))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred during deletion: {e}")
        conn.rollback()
    finally:
        conn.close()
        
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)


