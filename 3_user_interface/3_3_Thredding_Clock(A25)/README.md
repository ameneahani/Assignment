# ⏰ PySide6 Clock App 🕒

A simple GUI application made with Python and PySide6.  
It includes a **world clock 🌍**, **stopwatch ⏱️**, **timer ⏲️**, and **alarms 🔔**.

## Features ✨

- Display current time for different cities (IR 🇮🇷, DE 🇩🇪, US 🇺🇸).  
- Stopwatch with start, stop, and reset functions ⏱️.  
- Timer with settable hours, minutes, and seconds ⏲️.  
- Add, delete, and manage alarms stored in a local SQLite database 🔔.  
- Custom digital font (Seven Segment) for display 💻.  

## Requirements ⚙️

- Python 3.10+  
- PySide6  
- sqlite3 (built-in with Python)  

Install PySide6 using pip if needed:

```bash
pip install PySide6
How to Run ▶️
bash
Copy code
python test.py
test.py is the main program file.

Notes 📝
The app uses a database file alarm.db to store alarms.

The digital font Seven Segment.ttf is used for labels and timers.

When converting to an exe with PyInstaller, both alarm.db and the font file are included automatically.

Building an exe 🛠️
To create a standalone exe:

bash
Copy code
pyinstaller --onefile --windowed --add-data "Seven Segment.ttf;." --add-data "alarm.db;." test.py
--onefile → all files bundled into one exe.

--windowed → no console window.

--add-data → include font and database.

After building, run the exe and the app works without Python installed ✅.
