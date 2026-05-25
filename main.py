from parser import LogParser
from analyzer import LogAnalyzer
from io_utils import FileManager


def show_menu():
    print("\nLOG ANALYZER")
    print("1. Count messages by status")
    print("2. Filter by status")
    print("3. Filter by date range")
    print("4. Top N most frequent messages")
    print("5. Save current logs to JSON")
    print("6. Save current logs to CSV")
    print("0. Exit")


def print_logs(logs):
    if len(logs) == 0:
        print("No logs found.")
    else:
        for entry in logs:
            print(entry.get_info())


def main():
    filename = input("Enter log file name (default: logs.txt): ").strip()
    if filename == "":
        filename = "logs.txt"

    parser = LogParser(filename)
    logs = parser.load_logs()

    if len(logs) == 0:
        print("No valid logs loaded.")
        return

    print(f"Loaded {len(logs)} log entries.")

    analyzer = LogAnalyzer(logs)
    fm = FileManager()
    current_logs = logs

    while True:
        show_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            counts = analyzer.count_by_status()
            for status, count in counts.items():
                print(f"{status}: {count}")

        elif choice == "2":
            status = input("Enter status: ").strip()
            result = analyzer.filter_by_status(status)
            print(f"Found {len(result)} entries:")
            print_logs(result)
            current_logs = result

        elif choice == "3":
            start = input("Start date (YYYY-MM-DD): ").strip()
            end = input("End date (YYYY-MM-DD): ").strip()
            result = analyzer.filter_by_date_range(start, end)
            print(f"Found {len(result)} entries:")
            print_logs(result)
            current_logs = result

        elif choice == "4":
            try:
                n = int(input("How many top messages: ").strip())
            except ValueError:
                print("Enter a number.")
                continue
            top = analyzer.top_messages(n)
            for i, (msg, count) in enumerate(top, start=1):
                print(f"{i}. [{count}x] {msg}")

        elif choice == "5":
            out = fm.logs_to_dict(current_logs)
            fm.save_to_json(out, "results.json")

        elif choice == "6":
            fm.save_to_csv(current_logs, "results.csv")

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()
