from flask import Flask, render_template, request, jsonify
import sqlite3
import pandas as pd
import datetime

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA journal_mode=WAL;')  # Enable Write-Ahead Logging
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS timetable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT,
            subject TEXT,
            time TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            status TEXT,
            class_id INTEGER,
            timetable_id INTEGER,
            FOREIGN KEY (timetable_id) REFERENCES timetable(id)
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_timetable', methods=['POST'])
def add_timetable():
    day = request.form['day']
    subject = request.form['subject']
    time = request.form['time']
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO timetable (day, subject, time) VALUES (?, ?, ?)', (day, subject, time))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Timetable added successfully!'})

@app.route('/get_timetable', methods=['GET'])
def get_timetable():
    day = request.args.get('day')
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM timetable WHERE day = ?', (day,))
    classes = cursor.fetchall()
    conn.close()
    return jsonify(classes)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    try:
        data = request.json
        timetable_id = data['timetable_id']
        class_id = data.get('class_id', None)  # Optional, default to None if not provided
        date = data['date']
        status = data['status']

        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO attendance (date, status, class_id, timetable_id) VALUES (?, ?, ?, ?)',
            (date, status, class_id, timetable_id)
        )
        conn.commit()
        conn.close()

        return jsonify({'message': 'Attendance marked successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/export_attendance', methods=['GET'])
def export_attendance():
    try:
        conn = sqlite3.connect('attendance.db')
        query = '''
            SELECT t.day, t.subject, t.time, a.status, a.date, a.class_id
            FROM attendance a
            JOIN timetable t ON a.timetable_id = t.id
        '''
        df = pd.read_sql_query(query, conn)
        conn.close()

        if df.empty:
            return jsonify({'error': 'No attendance data found to export!'})

        # Generate a unique file name with a timestamp
        file_path = f"attendance_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        df.to_excel(file_path, index=False)

        # Return the file path in the response
        return jsonify({'file_path': file_path})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
