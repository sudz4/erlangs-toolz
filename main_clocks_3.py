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
    return local_time.strftime('%A %Y-%m-%d\n%H:%M:%S')

def update_time():
    for i, (city, tz_name) in enumerate(city_tzones.items()):
        time_labels[i]['text'] = get_local_time(tz_name)
    root.after(1000, update_time)

root = tk.Tk()
root.title("World Clocks")
root.configure(bg='#15202b')

time_labels = []

for index, (city, tz_name) in enumerate(city_tzones.items()):
    frame = tk.Frame(root, bg='#15202b', highlightbackground='#657786', highlightthickness=1)
    frame.grid(row=index // 2, column=index % 2, padx=20, pady=20, sticky="nsew")
    
    city_label = tk.Label(frame, text=city, font=("Arial", 32, "bold"), fg='#ffffff', bg='#15202b')
    city_label.pack(pady=(10, 0))
    
    time_label = tk.Label(frame, text=get_local_time(tz_name), font=("Arial", 24), fg='#ffffff', bg='#15202b')
    time_label.pack(pady=(0, 10))
    
    time_labels.append(time_label)

# ascii art signature
ascii_art = """
a program by,
  ___ _   _ ___ _____ _  
 / __| | | |   \_  / | | 
 \__ \ |_| | |) / /|_  _|
 |___/\___/|___/___| |_| 
                                    
"""
ascii_art_frame = tk.Frame(root, bg='#15202b')
ascii_art_frame.grid(row=6, column=1, padx=20, pady=20, sticky="nsew")
ascii_art_label = tk.Label(ascii_art_frame, text=ascii_art, font=("Courier", 20), fg='#ffffff', bg='#15202b')
ascii_art_label.pack()

for i in range(3):
    root.grid_columnconfigure(i, weight=1, uniform="col")
    root.grid_rowconfigure(i, weight=1, uniform="row")

update_time()
root.mainloop()