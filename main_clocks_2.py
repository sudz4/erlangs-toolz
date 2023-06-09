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
    # %A is the weedkday character

def update_time():
    for i, (city, tz_name) in enumerate(city_tzones.items()):
        time_labels[i]['text'] = get_local_time(tz_name)
    root.after(1000, update_time)  # schedule the next update in 1000 ms (1 second)

# configure UI
root = tk.Tk()
root.title("World Clocks")
root.configure(bg='#2D2D2D')  # set the window background color

time_labels = []

for index, (city, tz_name) in enumerate(city_tzones.items()):
    frame = tk.Frame(root, bg='#2D2D2D', highlightbackground='white', highlightthickness=1)
    frame.grid(row=index // 2, column=index % 2, padx=10, pady=10)
    
    city_label = tk.Label(frame, text=city, font=("Arial", 32, "bold"), fg='white', bg='#2D2D2D')
    city_label.pack(pady=(10, 0))
    
    time_label = tk.Label(frame, text=get_local_time(tz_name), font=("Arial", 24), fg='white', bg='#2D2D2D')
    time_label.pack(pady=(0, 10))
    
    time_labels.append(time_label)

update_time()  # start updating the time
root.mainloop()  # this runs the Tkinter event loop