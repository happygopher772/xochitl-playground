import os

def run_menu():
    while True:
        print("\nTime Library")
        print("1. Countdown Timer")
        print("2. Stopwatch")
        print("3. Timestamp Logger")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            os.system("python countdown_timer.py")
        elif choice == "2":
            os.system("python stopwatch.py")
        elif choice == "3":
            os.system("python timestamp_logger.py")
        elif choice == "4":
            print("じゃねー")
            break
        else:
            print("ehrm, pick something different bro")

if __name__ == "__main__":
    run_menu()
