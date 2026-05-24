class LogEntry:
    def __init__(self, date, time, status, message):
        self.date = date
        self.time = time
        self.status = status
        self.message = message

    def __str__(self):
        return f"{self.date} {self.time} [{self.status}] {self.message}"


class ErrorEntry(LogEntry):
    def __init__(self, date, time, message):
        super().__init__(date, time, "ERROR", message)

    def __str__(self):
        return f"[ERROR] {self.date} {self.time} - {self.message}"
