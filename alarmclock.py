import time
alarm = input("Set the alarm time in HH:MM:SS format: ")
while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time)
    if current_time == alarm:
        print("Wake up! It's time!")
        break
    time.sleep(1)