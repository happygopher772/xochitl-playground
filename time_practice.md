🕒 1. Countdown Timer

Goal:
Create a timer that counts down from a user-given number of seconds, showing the remaining time each second.

What you’ll practice:

Getting user input

Using time.sleep() for delays

Basic arithmetic with time

Printing dynamic output

🧩 Instructions

Ask the user how many seconds to count down from.

Use a while loop to display the remaining seconds every second.

When it reaches 0, print "Time's up!".

(Optional) Add a little beep or ASCII animation.

💻 Starter Code
import time

def countdown_timer():
    total_seconds = int(input("Enter countdown time in seconds: "))

    while total_seconds > 0:
        print(f"Time remaining: {total_seconds} seconds", end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("\nTime's up!")

if __name__ == "__main__":
    countdown_timer()

⏱️ 2. Simple Stopwatch

Goal:
Create a stopwatch that starts timing when you press Enter and stops when you press Enter again.

What you’ll practice:

Recording timestamps with time.time()

Doing time differences

Formatting elapsed time

🧩 Instructions

Wait for user input to start the timer.

When started, record the start time.

Wait again for input to stop.

Calculate and print how long it ran.

💻 Starter Code
import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start = time.time()

    input("Press Enter to stop the stopwatch...")
    end = time.time()

    elapsed = end - start
    print(f"Elapsed time: {elapsed:.2f} seconds")

if __name__ == "__main__":
    stopwatch()

🧾 3. Timestamp Logger

Goal:
Log every time a user presses Enter — showing real-world timestamps — and save them to a file.

What you’ll practice:

Getting the current date/time with time.strftime()

Writing to and reading from files

Combining time and file operations

🧩 Instructions

Create (or open) a file called timestamps.txt.

Every time the user presses Enter, record the current time.

Format it nicely (e.g. 2025-10-23 14:32:05).

Type "exit" to stop the program.

💻 Starter Code
import time

def timestamp_logger():
    with open("timestamps.txt", "a") as file:
        while True:
            user_input = input("Press Enter to log time, or type 'exit' to quit: ")
            if user_input.lower() == "exit":
                break

            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")
            print(f"Logged: {timestamp}")

if __name__ == "__main__":
    timestamp_logger()
