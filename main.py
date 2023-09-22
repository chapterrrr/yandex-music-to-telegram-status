import os

import yandex_music
import asyncio
import pyrogram
from pyrogram.raw import functions
import time


client = yandex_music.Client('').init()
api_id = 
api_hash = ""

app = pyrogram.Client("my_account", api_id=api_id, api_hash=api_hash)


def catch_track():
    try:
        queues = client.queues_list()
        last_queue = client.queue(queues[0].id)
        track_id = last_queue.get_current_track()
        track = track_id.fetch_track()
        return track
    except Exception as e:
        return 0

def catch_label():
    try:
        track = catch_track()
        artists = ', '.join(track.artists_name())
        title = track.title
        return "Сейчас слушает: " + f"{artists} - {title}"
    except Exception as e:
        return 'Сплю или афк...'

current = catch_label()

def set_status():
        time.sleep(15)
        with pyrogram.Client("my_account") as app:
            app.update_profile(bio=catch_label() + "\n\n by.chapter")

while True:
   if catch_label() != current: 
        set_status()
