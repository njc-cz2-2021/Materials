# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational materials repository for H2 Computing students at NJCCZ (by Han Jiseong). It contains Jupyter Notebooks, exercises, and notes — not a traditional software project. There is no build system, test runner, or linting pipeline.

## Running Materials

Launch Jupyter Notebook to work with any `.ipynb` file:
```bash
jupyter notebook
```

Run Flask web servers found in the Notes directory:
```bash
python <server_file>.py
# Then open localhost:8080 in Chrome (configured in .vscode/launch.json)
```

Install required dependencies (no requirements.txt — install individually):
```bash
pip install flask==2.2.5 pymongo==4.6.1 notebook==6.5.6
```

## Full Repository Structure

```
Materialss/
├── .vscode/
│   ├── launch.json               # Chrome debugger → localhost:8080
│   └── settings.json
├── LICENSE
├── README.md
│
├── 365-Days-of-H2-Computing/
│   ├── Day_001.ipynb – Day_031.ipynb   # 31 progressive daily lessons
│   ├── Empty_Day_004 copy.ipynb
│   ├── img/                            # 150+ images (PNG, JPG, GIF, SVG)
│   └── resources/                      # CSVs, TXTs, JSONs, DBs, HTML/CSS
│
├── Exercises/
│   ├── Exercise_05_File_IO.ipynb
│   ├── Exercise 12/                    # Web form project
│   │   └── WebForm1/
│   │       ├── static/
│   │       └── templates/
│   ├── Exercise-15-Object-Oriented-Programming-part-Deux.ipynb
│   ├── Exercise-16-SQL-Databases.ipynb
│   ├── Exercise-17-Fundamental-Algorithms.ipynb
│   ├── Exercise-18-Fundamental-Algorithms-part-two copy.ipynb
│   ├── Exercise-19-Data-And-Information.ipynb
│   ├── Exercise-20-Abstract_Data_Types.ipynb
│   ├── Exercise-21 More Abstract Data Type.ipynb
│   ├── Exercise-22-Even More Abstract Data Type and More.ipynb
│   ├── Exercise-23_NoSQL_Database.ipynb
│   ├── Exercise-24-Networking.ipynb
│   ├── img/
│   ├── resources/
│   └── web_stuff/
│       ├── Chapter_07_Files/
│       │   └── templates/
│       ├── img/
│       └── styles/
│
├── Notes/
│   ├── Chp02_ProgrammingConstructs/
│   ├── Chp03_DataStructures/
│   ├── Chp04_Functions/
│   ├── Chp06_ErrorTesting/
│   ├── Chp07_HTML&CSS/
│   │   └── EXERCISE_7_4/
│   │       ├── resources/
│   │       └── templates/
│   ├── Chp08_Algorithmic_Representation/
│   ├── Chp09_OOP/
│   │   └── resources/
│   ├── Chp10_SQL/
│   │   ├── Exercise10.5/
│   │   ├── Exercise10.6/
│   │   ├── resources/
│   │   └── templates/
│   ├── Chp11_Algorithm/
│   ├── Chp12_DataAndInfo/
│   ├── Chp14_ADT/
│   ├── Chp15_NoSQL/
│   ├── Chp16_Networking/
│   ├── archived/                       # Legacy/old versions of notes
│   ├── images/
│   ├── resources/
│   ├── sucky_web_server/               # Flask server for web chapter
│   │   └── templates/
│   ├── templates/
│   └── web_stuff/
│       ├── img/
│       └── styles/
│
└── Working Folder/
    └── Order or Growth.ipynb           # Algorithm complexity analysis
```

## Notes Chapter Coverage

| Chapter | Topic |
|---------|-------|
| Chp02 | Programming Constructs |
| Chp03 | Data Structures |
| Chp04 | Functions |
| Chp06 | Error Testing & Validation |
| Chp07 | HTML & CSS (Flask web dev) |
| Chp08 | Algorithmic Representation |
| Chp09 | Object-Oriented Programming |
| Chp10 | SQL Databases |
| Chp11 | Fundamental Algorithms |
| Chp12 | Data & Information |
| Chp14 | Abstract Data Types |
| Chp15 | NoSQL Databases (MongoDB) |
| Chp16 | Networking |

## Key Resource Files

- **SQLite databases**: `poly.db`, `school.db`, `Task4.db` (in `Notes/Chp10_SQL/`)
- **Data files**: CSV, TXT, JSON files in various `resources/` folders
- **Web assets**: HTML/CSS in `templates/` and `web_stuff/` directories
- **Flask servers**: Python `.py` scripts in `Notes/` and `Exercises/Exercise 12/`

## Notebook Conventions

- All notebooks are designed to run top-to-bottom sequentially
- Many notebooks include Google Colab `Open in Colab` badges
- The `365-Days-of-H2-Computing/` series is a self-paced daily progression
- Exercise notebooks may have intentionally incomplete cells for students to fill in
