class BaseEntry:
    def __init__(self, date, time, message):
        self.date = date
        self.time = time
        self.message = message

    def get_info(self):
        return f"{self.date} {self.time} {self.message}"


class LogEntry(BaseEntry):
    def __init__(self, date, time, status, message):
        super().__init__(date, time, message)
        self.status = status

    def get_info(self):
        return f"{self.date} {self.time} [{self.status}] {self.message}"

    def __str__(self):
        return self.get_info()


class CriticalEntry(LogEntry):
    def __init__(self, date, time, message):
        super().__init__(date, time, "CRITICAL", message)

    def get_info(self):
        return f"!!! CRITICAL !!! {self.date} {self.time} - {self.message}"