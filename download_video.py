import os
import sys
import time

import youtube_dl
from PyQt6.QtCore import QThread, pyqtSignal

from create_mp3 import create_mp3

# Global variables
SAVE_PATH = os.path.expanduser('~/Downloads')
count_percent = 0
downloaded = 0

# Hook to catch the % of downloading
def my_hook(d):
    global count_percent
    global downloaded

    # print('hjhjhjhjh')
    if d['status'] == 'finished':
        count_percent = 0
        downloaded = 1

    elif d['status'] == 'downloading':
        count_percent = int(d['_percent_str'][0:3])


ydl_video = {
    'format': 'best',
    'dumpjson': True,
    'progress_hooks': [my_hook],
    'outtmpl': SAVE_PATH + '/yuhook_videos/%(title)s.%(ext)s',
}


# Resource path
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        print(' ')
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("venv"), relative_path)


# Class to download the video file
class Download(QThread):
    signal_start_download = pyqtSignal(int)

    def __init__(self, video_url, parent=None):
        super(Download, self).__init__(parent)
        self.video_url = video_url

    def run(self):
        self.signal_start_download.emit(0)  # Start downloading
        time.sleep(2)

        # Create video folder
        video_folder = os.path.join(SAVE_PATH, 'yuhook_videos')

        if not os.path.isdir(video_folder):
            os.mkdir(video_folder)

        """Download video"""
        with youtube_dl.YoutubeDL(ydl_video) as ydlvideo:
            ydlvideo.download([self.video_url])

        self.signal_start_download.emit(1)  # End of download

        create_mp3()
        time.sleep(4)
        self.signal_start_download.emit(2)  # End of creating mp3




# Class to fill the progress bar
class Progressbar(QThread):
    signal_prgb = pyqtSignal(int)
    signal_prgb_end = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Progressbar, self).__init__(parent)

    def run(self):
        # Fill progress bar
        global count_percent

        while count_percent <= 100 and downloaded == 0:
            self.signal_prgb.emit(count_percent)

        val_end = 0
        print('finito progress bar')
        self.signal_prgb_end.emit(val_end)
