import re
from models import LogEntry

ALLOWED = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
LOG_PATTERN = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"


class BaseParser:
    def parse(self, text):
        raise NotImplementedError


class LogParser(BaseParser):
    def __init__(self, filename):
        self.filename = filename

    def parse(self, text):
        match = re.match(LOG_PATTERN, text)
        if match:
            date = match.group(1)
            time = match.group(2)
            status = match.group(3)
            message = match.group(4)
            if status in ALLOWED:
                return LogEntry(date, time, status, message)
        return None

    def load_logs(self):
        logs = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    entry = self.parse(line)
                    if entry is not None:
                        logs.append(entry)
                    else:
                        print(f"skipped: {line}")
        except FileNotFoundError:
            print(f"File not found: {self.filename}")
        return logs