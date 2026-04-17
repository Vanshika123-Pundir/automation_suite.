import os
import shutil
from datetime import datetime

class FileOrganizer:

    def __init__(self, watch_folder, organized_folder):
        self.watch_folder = watch_folder
        self.organized_folder = organized_folder

        self.file_categories = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt'],
            'Images': ['.jpg', '.jpeg', '.png'],
            'Videos': ['.mp4', '.avi'],
            'Music': ['.mp3', '.wav'],
            'Code': ['.py', '.html', '.css']
        }

    def setup_folders(self):
        """Create folders if not exist"""
        if not os.path.exists(self.organized_folder):
            os.makedirs(self.organized_folder)

        for category in self.file_categories:
            path = os.path.join(self.organized_folder, category)
            if not os.path.exists(path):
                os.makedirs(path)

    def organize_files(self):
        """Main function to organize files"""

        # Check folder exists
        if not os.path.exists(self.watch_folder):
            print("❌ Watch folder not found!")
            return

        files = os.listdir(self.watch_folder)

        if not files:
            print("⚠️ Folder empty hai")
            return

        for filename in files:

            file_path = os.path.join(self.watch_folder, filename)

            # Skip folders
            if not os.path.isfile(file_path):
                continue

            ext = os.path.splitext(filename)[1].lower()
            moved = False

            for category, extensions in self.file_categories.items():

                if ext in extensions:

                    dest_folder = os.path.join(self.organized_folder, category)
                    dest_path = os.path.join(dest_folder, filename)

                    # Duplicate handling
                    if os.path.exists(dest_path):
                        base, extension = os.path.splitext(filename)
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        new_filename = f"{base}_{timestamp}{extension}"
                        dest_path = os.path.join(dest_folder, new_filename)

                    shutil.move(file_path, dest_path)
                    print(f"✅ {filename} → {category}")
                    moved = True
                    break

            # If no category matched
            if not moved:
                other_folder = os.path.join(self.organized_folder, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"📦 {filename} → Others")