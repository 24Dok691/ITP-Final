import re
from models import LogEntry

ALLOWED = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"


def parse_line(line):
    match = re.match(pattern, line)
    if match:
        date = match.group(1)
        time = match.group(2)
        status = match.group(3)
        message = match.group(4)
        if status in ALLOWED:
            return LogEntry(date, time, status, message)
    return None


def load_logs(filename):
    logs = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                entry = parse_line(line)
                if entry is not None:
                    logs.append(entry)
                else:
                    print(f"skipped: {line}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return logs
