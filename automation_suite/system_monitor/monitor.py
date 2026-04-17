import psutil

class SystemMonitor:
    def show_status(self):
        try:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('C:\\')

            print("\n🖥️ SYSTEM STATUS:\n")
            print(f"CPU Usage: {cpu}%")
            print(f"RAM Usage: {memory.percent}%")
            print(f"Disk Usage: {disk.percent}%")

        except Exception as e:
            print("❌ Error:", e)