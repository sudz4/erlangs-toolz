"""Clocks - where is my team?"""
# think about also doing a jupyter notebook here and plotting on a map
# or exlore map gui stuff with tkinter

#libs
import tkinter as tk
import datetime
from dateutil import tz

# city names and time zones
city_tzones = {
    'San Diego': 'America/Los_Angeles',
    'Phoenix': 'America/Phoenix',
    'Denver': 'America/Denver',
    'Dallas': 'America/Chicago',
    'Charlotte': 'America/New_York',
    'Pune': 'Asia/Kolkata',
    'Bengaluru': 'Asia/Kolkata',
    'London': 'Europe/London',
    'Naples': 'Europe/Rome',
    'Melbourne': 'Australia/Melbourne',
    'Buenos Aires': 'America/Argentina/Buenos_Aires',
    'Hong Kong': 'Asia/Hong_Kong',
    'Tokyo': 'Asia/Tokyo'
}

def get_local_time(tz_name):
    timezone = tz.gettz(tz_name)
    local_time = datetime.datetime.now(timezone)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')

def update_time():
    for i, (city, tz_name) in enumerate(city_tzones.items()):
        time_labels[i]['text'] = f"{city}: {get_local_time(tz_name)}"
    root.after(1000, update_time)  # schedule the next update in 1000 ms (1 second)

root = tk.Tk()
root.title("World Clocks")

time_labels = []
for city, tz_name in city_tzones.items():
    time_label = tk.Label(root, text=f"{city}: {get_local_time(tz_name)}", font=("Helvetica", 14))
    time_label.pack(pady=5)
    time_labels.append(time_label)

update_time()  # start updating the time
root.mainloop()  # this runs the Tkinter event loop