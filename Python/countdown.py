import time
count = int(input("Enter the countdown time in seconds: "))
while count >= 0:
    print(count)
    count -= 1
    time.sleep(1)
print("Countdown finished!")