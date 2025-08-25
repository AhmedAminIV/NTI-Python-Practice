"""
Exercise 4:
collect system logs every hour in a file with a name of date and hour file created.
make it elaborate.

Keyword: scheduled cron job (Linux, macOS), or Task Scheduler job (Windows)
"""
import os
import datetime
import psutil
from pathlib import Path

# Define log directory
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)  # create folder if not exists

# Get current date and hour for filename
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H")
log_file = LOG_DIR / f"system_log_{timestamp}.log"

# Collect system info
cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

# Prepare log content
log_content = f"""
===== System Log ({datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}) =====

CPU Usage: {cpu_usage}%
Memory: {memory.used / (1024**3):.2f} GB used / {memory.total / (1024**3):.2f} GB total
Disk: {disk.used / (1024**3):.2f} GB used / {disk.total / (1024**3):.2f} GB total

========================================================
"""

# Write to file (append mode if file exists)
with open(log_file, "a") as f:
    f.write(log_content)

print(f"Log written to {log_file}")
