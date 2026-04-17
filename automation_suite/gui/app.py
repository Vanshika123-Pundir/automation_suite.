import sys
import os

# FIX: parent folder path add karna
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox, ttk
import threading

from file_organizer.organizer import FileOrganizer
from web_scraper.scraper import WebScraper
from email_automation.email_sender import EmailSender
from system_monitor.monitor import SystemMonitor
from task_scheduler.scheduler import TaskScheduler

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Automation Suite")
root.geometry("600x500")

# ---------------- STATUS ----------------
status_text = tk.StringVar()
status_text.set("Ready")

tk.Label(root, text="Automation Suite", font=("Arial", 16)).pack(pady=10)
tk.Label(root, textvariable=status_text).pack(pady=5)

# ---------------- THREAD FUNCTION ----------------
def run_thread(func):
    threading.Thread(target=func).start()

# ---------------- FUNCTIONS ----------------
def run_file_organizer():
    try:
        status_text.set("Running File Organizer...")
        organizer = FileOrganizer("watch_folder", "organized_folder")
        organizer.organize_files()
        status_text.set("File Organizer Done ✅")
        messagebox.showinfo("Success", "Files Organized")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def run_web_scraper():
    try:
        status_text.set("Running Web Scraper...")
        scraper = WebScraper()
        scraper.scrape()
        status_text.set("Web Scraper Done ✅")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def send_email():
    try:
        status_text.set("Sending Email...")
        sender = EmailSender()
        sender.send_email()
        status_text.set("Email Sent ✅")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def system_status():
    try:
        status_text.set("Checking System...")
        monitor = SystemMonitor()
        monitor.show_status()
        status_text.set("System Checked ✅")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def start_scheduler():
    try:
        status_text.set("Starting Scheduler...")
        scheduler = TaskScheduler()
        scheduler.start()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- WORKFLOW ----------------
steps = ["File Organizer", "Web Scraper", "Send Email", "System Monitor"]
selected_steps = []

def add_step():
    step = combo.get()
    if step:
        selected_steps.append(step)
        listbox.insert(tk.END, step)

def run_workflow():
    for step in selected_steps:
        if step == "File Organizer":
            run_file_organizer()
        elif step == "Web Scraper":
            run_web_scraper()
        elif step == "Send Email":
            send_email()
        elif step == "System Monitor":
            system_status()
    messagebox.showinfo("Done", "Workflow Completed")

# ---------------- UI ----------------
combo = ttk.Combobox(root, values=steps)
combo.pack(pady=5)

tk.Button(root, text="Add Step", command=add_step).pack(pady=5)
tk.Button(root, text="Run Workflow", command=lambda: run_thread(run_workflow)).pack(pady=5)

listbox = tk.Listbox(root, height=5)
listbox.pack(pady=10)

tk.Button(root, text="File Organizer", width=25, command=lambda: run_thread(run_file_organizer)).pack(pady=5)
tk.Button(root, text="Web Scraper", width=25, command=lambda: run_thread(run_web_scraper)).pack(pady=5)
tk.Button(root, text="Send Email", width=25, command=lambda: run_thread(send_email)).pack(pady=5)
tk.Button(root, text="System Monitor", width=25, command=lambda: run_thread(system_status)).pack(pady=5)
tk.Button(root, text="Start Scheduler", width=25, command=lambda: run_thread(start_scheduler)).pack(pady=5)

# ---------------- RUN ----------------
root.mainloop()