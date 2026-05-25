import json
import csv


class FileManager:
    def save_to_json(self, data, filename):
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            print(f"Saved to {filename}")
        except Exception as e:
            print(f"Error: {e}")

    def save_to_csv(self, logs, filename):
        try:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "time", "status", "message"])
                for entry in logs:
                    writer.writerow([entry.date, entry.time, entry.status, entry.message])
            print(f"Saved to {filename}")
        except Exception as e:
            print(f"Error: {e}")

    def logs_to_dict(self, logs):
        result = []
        for entry in logs:
            result.append({
                "date": entry.date,
                "time": entry.time,
                "status": entry.status,
                "message": entry.message
            })
        return result
