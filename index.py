import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("times up")

def main():
    try:
        minuts = int(input("enter the countdown time in minuts : "))
        seconds = minuts * 60
        countdown_timer(seconds)
    except ValueError:
        print("plese enter a valid number : ")

if __name__ == "__main__":
    main()

