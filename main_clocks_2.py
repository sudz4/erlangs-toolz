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
    'Melbourne': 'Australia/Melbourne'
    'Buenos Aires': 'America/Argentina/Buenos_Aires',
    'Hong Kong': 'Asia/Hong_Kong',
    'Tokyo': 'Asia/Tokyo
}

def get_local_time(tz_name):
    timezone = tz.gettz(tz_name)
    local_time = datetime.datetime.now(timezone)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')