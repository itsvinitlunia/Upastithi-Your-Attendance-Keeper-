# Upastithi - Your Attendance Keeper

Upastithi is a lightweight and user-friendly web application designed to help users manage timetables and track attendance seamlessly. Built with Python (Flask) and SQLite, it allows users to mark attendance, export records to Excel, and handle schedules efficiently.

## Features

### Timetable Management
- Add, view, and manage daily schedules.
- Dynamically fetch and display the timetable for the current day.

### Attendance Marking
- Mark attendance with statuses like "Present," "Absent," and "Proxy."
- Store attendance history for future reference.

### Attendance Export
- Export attendance records to an Excel file.
- Include details such as date, subject, time, and attendance status in the exported file.

### Database Integration
- Use SQLite for lightweight, efficient storage.
- Maintain data consistency with foreign key relationships.

### Error Handling and Notifications
- Provide user-friendly alerts for errors such as database locks or invalid inputs.
- Ensure smooth user experience with appropriate feedback mechanisms.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/itsvinitlunia/Upastithi-Your-Attendance-Keeper
   ```

2. **Set Up the Environment**:
   - Install Python 3.10 or higher.
   - Create a virtual environment and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows: venv\Scripts\activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:
   - The app uses SQLite for data storage. Run the app once to create the necessary tables:
     ```bash
     python app.py
     ```

5. **Run the Application**:
   ```bash
   flask run
   ```
   Access the application at `http://127.0.0.1:5000/` in your browser.

## Usage

### Adding Timetable Entries
- Use the "Add Timetable" section to input the day, subject, and time for each lecture.

### Marking Attendance
- The "Mark Attendance" section displays the timetable for the current day.
- Click "Present," "Absent," or "Proxy" to mark attendance for each lecture.

### Exporting Attendance
- Click the "Export to Excel" button to generate an Excel file containing all attendance records.

## Database Schema

### Timetable Table
| Column   | Type    | Description         |
|----------|---------|---------------------|
| id       | INTEGER | Primary Key         |
| day      | TEXT    | Day of the week     |
| subject  | TEXT    | Lecture subject     |
| time     | TEXT    | Time of the lecture |

### Attendance Table
| Column        | Type    | Description                   |
|---------------|---------|-------------------------------|
| id            | INTEGER | Primary Key                   |
| timetable_id  | INTEGER | Foreign Key (timetable.id)    |
| date          | TEXT    | Date of attendance            |
| status        | TEXT    | Attendance status (e.g., Present, Absent, Proxy) |

## Skills Demonstrated
- **Frontend Development**: HTML, CSS, JavaScript
- **Backend Development**: Python (Flask Framework)
- **Database Management**: SQLite
- **Data Processing**: Pandas for Excel export
- **Error Handling**: Graceful handling of database and user input errors
- **Version Control**: Git

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or feedback, please reach out to luniavinit@gmail.com .# Upastithi-Your-Attendance-Keeper-
