class LogAnalyzer:
    def __init__(self, logs):
        self.logs = logs

    def count_by_status(self):
        counts = {}
        for entry in self.logs:
            s = entry.status
            if s in counts:
                counts[s] += 1
            else:
                counts[s] = 1
        return counts

    def filter_by_status(self, status):
        result = []
        for entry in self.logs:
            if entry.status == status.upper():
                result.append(entry)
        return result

    def filter_by_date_range(self, start, end):
        result = []
        for entry in self.logs:
            if start <= entry.date <= end:
                result.append(entry)
        return result

    def top_messages(self, n):
        msg_count = {}
        for entry in self.logs:
            m = entry.message
            if m in msg_count:
                msg_count[m] += 1
            else:
                msg_count[m] = 1
        sorted_msgs = sorted(msg_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_msgs[:n]

    def get_unique_statuses(self):
        unique = set()
        for entry in self.logs:
            unique.add(entry.status)
        return unique
