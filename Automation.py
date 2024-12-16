import schedule
import time


def my_task():
    print("The task is being triggered!")

# Schedule the task to run at a specific time
schedule.every().day.at("22:16").do(my_task)


while True:
    schedule.run_pending()
    time.sleep(1)

