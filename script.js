document.addEventListener('DOMContentLoaded', () => {
    const timetableForm = document.getElementById('timetable-form');
    const timetableContainer = document.getElementById('timetable-container');
    const exportButton = document.getElementById('export-button');

    timetableForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(timetableForm);
        fetch('/add_timetable', {
            method: 'POST',
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => alert(data.message))
            .catch((error) => console.error(error));
    });

    const today = new Date().toLocaleString('en-us', { weekday: 'long' });
    fetch(`/get_timetable?day=${today}`)
        .then((response) => response.json())
        .then((classes) => {
            if (classes.length > 0) {
                timetableContainer.innerHTML = '';
                classes.forEach((cls) => {
                    const div = document.createElement('div');
                    div.innerHTML = `
                        <p>${cls[2]} - ${cls[1]}</p>
                        <button onclick="markAttendance(${cls[0]}, 'Present', ${cls[0]})">Present</button>
                        <button onclick="markAttendance(${cls[0]}, 'Absent', ${cls[0]})">Absent</button>
                        <button onclick="markAttendance(${cls[0]}, 'Proxy', ${cls[0]})">Proxy</button>
                    `;
                    timetableContainer.appendChild(div);
                });
            }
        });

    window.markAttendance = (timetableId, status, classId) => {
        const date = new Date().toISOString().split('T')[0];
        fetch('/mark_attendance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ timetable_id: timetableId, date, status, class_id: classId }),
        })
            .then((response) => response.json())
            .then((data) => alert(data.message))
            .catch((error) => console.error(error));
    };

    exportButton.addEventListener('click', () => {
        fetch('/export_attendance')
            .then((response) => response.json())
            .then((data) => {
                if (data.file_path) {
                    alert('Attendance exported to: ' + data.file_path);
                } else if (data.error) {
                    alert('Error: ' + data.error);
                } else {
                    alert('Unexpected response from the server.');
                }
            })
            .catch((error) => console.error(error));
    });
});
