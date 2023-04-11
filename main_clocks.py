"""Clocks - where is my team?"""
# think about also doing a jupyter notebook here and plotting on a map
# or exlore map gui stuff with tkinter

#libs
import tkinter as tk
import datetime
from dateutil import tz

# time zones 
time_zones = [
    'America/New_York',
    'Europe/London',
    'Asia/Tokyo',
    'Australia/Sydney'
]

def get_local_time(tz_name):
    timezone = tz.gettz(tz_name)
    local_time = datetime.datetime.now(timezone)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

def update_time():
    for i, tz_name in enumerate(time_zones):
        time_labels[i]['text'] = f"{tz_name}: {get_local_time(tz_name)}"
    root.after(1000, update_time)  # schedule the next update in 1000 ms (1 second)

root = tk.Tk()
root.title("World Clocks")

time_labels = []
for tz_name in time_zones:
    time_label = tk.Label(root, text=f"{tz_name}: {get_local_time(tz_name)}", font=("Helvetica", 14))
    time_label.pack(pady=5)
    time_labels.append(time_label)

update_time()  # start updating the time
root.mainloop()  # run the Tkinter event loop