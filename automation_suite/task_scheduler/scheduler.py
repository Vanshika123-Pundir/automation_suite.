import schedule
import time

class TaskScheduler:

    def job(self):
        print("⏰ Task running... Automation working!")

    def start(self):
        # हर 10 second में task चलेगा (test ke liye)
        schedule.every(10).seconds.do(self.job)

        print("✅ Scheduler started... (हर 10 sec में task चलेगा)\n")

        while True:
            schedule.run_pending()
            time.sleep(1)