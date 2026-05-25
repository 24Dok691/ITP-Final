# Log Analyzer

A simple Python program that reads system log files and shows statistics.

## Team

- Team 6
- Temirzakhov Adilzhan
- Zholdygali Azat
- Niyalov Yerkebulan

## What it does

- Reads a `.txt` log file
- Parses each line using regular expressions
- Counts log messages by status type (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Filters logs by status
- Filters logs by date range
- Shows Top N most frequent messages
- Saves results to JSON or CSV

## Log file format

Each line must follow this format:

```
YYYY-MM-DD HH:MM:SS STATUS message
```

Example:
```
2026-01-01 10:15:32 ERROR Failed to connect to database
2026-01-01 10:15:35 INFO Service started
```

## How to run

Make sure you have Python 3 installed.

1. Put your log file in the project folder (default name: `logs.txt`)
2. Run the program:

```
python main.py
```

3. Enter the log file name or press Enter to use `logs.txt`
4. Use the menu to explore your logs

## How to run tests

```
python tests.py
```

## Project structure

```
log_analyzer/
├── main.py       - entry point, menu
├── models.py     - LogEntry, BaseEntry, CriticalEntry classes
├── parser.py     - reads file, parses lines with regex
├── analyzer.py   - counting, filtering, top N
├── io_utils.py   - save to JSON or CSV
├── tests.py      - unit tests
├── logs.txt      - example log file
└── README.md
```
