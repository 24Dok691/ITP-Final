from parser import load_logs
from analyzer import count_by_status, filter_by_status, filter_by_date, top_messages


def show_logs(logs):
    if len(logs) == 0:
        print("No results.")
    for entry in logs:
        print(entry)


def main():
    filename = input("Log file (default logs.txt): ").strip()
    if filename == "":
        filename = "logs.txt"

    logs = load_logs(filename)

    if len(logs) == 0:
        print("No logs loaded.")
        return

    print(f"Loaded {len(logs)} entries.")

    while True:
        print("\n1. Count by status")
        print("2. Filter by status")
        print("3. Filter by date range")
        print("4. Top N messages")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            counts = count_by_status(logs)
            for s, c in counts.items():
                print(f"{s}: {c}")

        elif choice == "2":
            status = input("Status: ").strip()
            result = filter_by_status(logs, status)
            print(f"Found {len(result)}:")
            show_logs(result)

        elif choice == "3":
            start = input("Start date (YYYY-MM-DD): ").strip()
            end = input("End date (YYYY-MM-DD): ").strip()
            result = filter_by_date(logs, start, end)
            print(f"Found {len(result)}:")
            show_logs(result)

        elif choice == "4":
            try:
                n = int(input("How many: ").strip())
            except ValueError:
                print("Enter a number.")
                continue
            top = top_messages(logs, n)
            for i, (msg, c) in enumerate(top, 1):
                print(f"{i}. [{c}x] {msg}")

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Wrong choice.")


if __name__ == "__main__":
    main()
