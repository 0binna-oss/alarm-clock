import time 
import os 

# get the alarm time from the user 
def alarm_clock():
    alarm_time = input("Enter the time to set the alarm(HH:MM:SS):")
    print(f"Alarm set for{alarm_time}")

# get the current time 
    while True:
        current_time=time.strftime("%H:%M:%S")

        # check if the current time matches the alarm time 
        if current_time == alarm_time:
            print("Wake up")

        #play a sound or show a notification 
        if os.name == 'posix':
            os.system('say "Wake up"')
        else:
            os.system('msg * "wake up"')
        break 

# wait for 1 second before checking the time again
time.sleep(1)

if __name__=="__main__":
    alarm_clock()