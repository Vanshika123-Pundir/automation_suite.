from file_organizer.organizer import FileOrganizer
from web_scraper.scraper import WebScraper

# ---------------- FILE ORGANIZER ----------------
watch_folder = "test_folder"
organized_folder = "organized_files"

organizer = FileOrganizer(watch_folder, organized_folder)
organizer.setup_folders()
organizer.organize_files()

# ---------------- WEB SCRAPER ----------------
url = "https://news.ycombinator.com"

scraper = WebScraper(url)
scraper.scrape_titles()
from email_automation.email_sender import EmailSender

# ---------------- EMAIL AUTOMATION ----------------
sender_email = "pundirvanshika44@gmail.com"
app_password = "xngcxydhulueubyt"
receiver_email = "pundirvanshika44@gmail.com"

email = EmailSender(sender_email, app_password)

email.send_email(
    receiver_email,
    "Automation Test",
    "Hello! Ye automated email hai 🚀"
)
from system_monitor.monitor import SystemMonitor

# ---------------- SYSTEM MONITOR ----------------
monitor = SystemMonitor()
monitor.show_status()
from task_scheduler.scheduler import TaskScheduler

# ---------------- TASK SCHEDULER ----------------
scheduler = TaskScheduler()
scheduler.start()