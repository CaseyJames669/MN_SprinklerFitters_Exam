import shutil
import os

src = os.path.join('H:', 'Google Drive', 'MN_SprinklerFitters_Exam', 'visualization', 'docs', 'grok4.wav')
dest = os.path.join('H:', 'Google Drive', 'MN_SprinklerFitters_Exam', 'visualization', 'grok4.wav')

if os.path.exists(src):
    shutil.move(src, dest)
    print(f"Moved {src} to {dest}")
else:
    print(f"Source file not found: {src}")