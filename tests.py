import unittest
from models import LogEntry, ErrorEntry
from parser import parse_line
from analyzer import count_by_status, filter_by_status, filter_by_date, top_messages


class TestModels(unittest.TestCase):
    def test_log_entry(self):
        e = LogEntry("2026-01-01", "10:00:00", "INFO", "started")
        self.assertEqual(e.status, "INFO")

    def test_error_entry_status(self):
        e = ErrorEntry("2026-01-01", "10:00:00", "db failed")
        self.assertEqual(e.status, "ERROR")


class TestParser(unittest.TestCase):
    def test_valid(self):
        e = parse_line("2026-01-01 10:00:00 INFO started")
        self.assertIsNotNone(e)
        self.assertEqual(e.status, "INFO")

    def test_invalid(self):
        e = parse_line("not a log line")
        self.assertIsNone(e)


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.logs = [
            LogEntry("2026-01-01", "10:00:00", "ERROR", "db failed"),
            LogEntry("2026-01-01", "11:00:00", "INFO", "started"),
            LogEntry("2026-01-02", "09:00:00", "ERROR", "db failed"),
            LogEntry("2026-01-02", "10:00:00", "WARNING", "low memory"),
        ]

    def test_count(self):
        counts = count_by_status(self.logs)
        self.assertEqual(counts["ERROR"], 2)

    def test_filter_status(self):
        result = filter_by_status(self.logs, "ERROR")
        self.assertEqual(len(result), 2)

    def test_filter_date(self):
        result = filter_by_date(self.logs, "2026-01-01", "2026-01-01")
        self.assertEqual(len(result), 2)

    def test_top(self):
        top = top_messages(self.logs, 1)
        self.assertEqual(top[0][0], "db failed")


if __name__ == "__main__":
    unittest.main()
