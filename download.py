from yt_dlp import YoutubeDL
import json
from history import *



ydl_opts = {
    'ffmpeg_location' : "X:\MyPrograms\\ffmpeg\\bin",
    'format': 'bestaudio/best',  # Select best audio quality
    'outtmpl': 'download/%(title)s.%(ext)s',  # Save file with the title of the video
    'postprocessors': [{  # Add post-processor to convert to mp3
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',  # Set quality (bitrate) to 192 kbps
    }],
}

def download_list(data_list):
    URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']
    with YoutubeDL(ydl_opts) as ydl:
        i = 0
        for key in data_list.keys():
            if (data_list[key]['downloaded'] != True):
                try:
                    ydl.download(key)
                except:
                    pass
                data_list[key]['downloaded'] = True
            i += 1
            if i % 10 == 9:
                update_json(data_list)
    update_json(data_list)