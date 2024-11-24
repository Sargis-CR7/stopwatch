import time
def start_stopwatch():
    start_time=time.time()
    input("stopwatch started press enter to stop")
    end_time=time.time()
    elapset_time=end_time-start_time 
    print(elapset_time)

print("welkome to thle python stopwatch")

while True:
    print("\n 0 options")
    print("1 start syopwatch")
    print("2 exit")

    choice=input("enter your choice 1-2")
    if choice=="1":
        print(f"elapseet time{start_stopwatch()}")
    elif choice=="2":
        print("exiting the stopwatch.goodbye")
        break
    else:
        print("invalid choice. pleaze enter")
