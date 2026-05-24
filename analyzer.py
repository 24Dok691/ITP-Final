def count_by_status(logs):
    counts = {}
    for entry in logs:
        s = entry.status
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    return counts


def filter_by_status(logs, status):
    result = []
    for entry in logs:
        if entry.status == status.upper():
            result.append(entry)
    return result


def filter_by_date(logs, start, end):
    result = []
    for entry in logs:
        if start <= entry.date <= end:
            result.append(entry)
    return result


def top_messages(logs, n):
    counts = {}
    for entry in logs:
        m = entry.message
        if m in counts:
            counts[m] += 1
        else:
            counts[m] = 1
    sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[:n]
