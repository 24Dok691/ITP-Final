import unittest
from models import LogEntry
from parser import LogParser
from analyzer import LogAnalyzer


class TestLogEntry(unittest.TestCase):
    def test_create_entry(self):
        e = LogEntry("2026-01-01", "10:15:32", "ERROR", "Something failed")
        self.assertEqual(e.status, "ERROR")
        self.assertEqual(e.message, "Something failed")

    def test_get_info(self):
        e = LogEntry("2026-01-01", "10:00:00", "INFO", "Started")
        info = e.get_info()
        self.assertIn("INFO", info)
        self.assertIn("Started", info)


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = LogParser("logs.txt")

    def test_valid_line(self):
        line = "2026-01-01 10:15:32 ERROR Failed to connect"
        result = self.parser.parse(line)
        self.assertIsNotNone(result)
        self.assertEqual(result.status, "ERROR")
        self.assertEqual(result.message, "Failed to connect")

    def test_invalid_line(self):
        line = "this is not a log line"
        result = self.parser.parse(line)
        self.assertIsNone(result)

    def test_unknown_status(self):
        line = "2026-01-01 10:15:32 VERBOSE some message"
        result = self.parser.parse(line)
        self.assertIsNone(result)


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.logs = [
            LogEntry("2026-01-01", "10:00:00", "ERROR", "DB failed"),
            LogEntry("2026-01-01", "10:01:00", "INFO", "Service started"),
            LogEntry("2026-01-02", "09:00:00", "ERROR", "DB failed"),
            LogEntry("2026-01-02", "09:05:00", "WARNING", "Low memory"),
            LogEntry("2026-01-03", "08:00:00", "CRITICAL", "Crash"),
        ]
        self.analyzer = LogAnalyzer(self.logs)

    def test_count_by_status(self):
        counts = self.analyzer.count_by_status()
        self.assertEqual(counts["ERROR"], 2)
        self.assertEqual(counts["INFO"], 1)

    def test_filter_by_status(self):
        result = self.analyzer.filter_by_status("ERROR")
        self.assertEqual(len(result), 2)

    def test_filter_empty_status(self):
        result = self.analyzer.filter_by_status("DEBUG")
        self.assertEqual(len(result), 0)

    def test_filter_by_date_range(self):
        result = self.analyzer.filter_by_date_range("2026-01-01", "2026-01-02")
        self.assertEqual(len(result), 4)

    def test_top_messages(self):
        top = self.analyzer.top_messages(1)
        self.assertEqual(top[0][0], "DB failed")
        self.assertEqual(top[0][1], 2)

    def test_empty_logs(self):
        a = LogAnalyzer([])
        counts = a.count_by_status()
        self.assertEqual(counts, {})


if __name__ == "__main__":
    unittest.main()
