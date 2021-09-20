import os
import sys



from PyQt6.QtCore import QThread, pyqtSignal

SAVE_PATH = os.path.expanduser('~/Downloads')


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        print(' ')
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("venv"), relative_path)


# pycharm exe
ffmpeg_path = ".\\ffmpeg\\ffmpeg.exe"

# .exe
#ffmpeg_path = "./ffmpeg/ffmpeg.exe"

# Create audio folder
audio_folder = os.path.join(SAVE_PATH, 'yuhook_music')

if not os.path.isdir(audio_folder):
    os.mkdir(audio_folder)


# video folder path
video_path = os.path.expanduser('~\Downloads\yuhook_videos')

# List of videos in video path
arr_webm = [x for x in os.listdir(video_path) if x.endswith(".webm") or x.endswith(".m4a") or x.endswith(".mp4")]


# Class to extract mp3 from videos
class Create_mp3(QThread):
    signal_cmp3_start = pyqtSignal(int)
    signal_cmp3_end = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Create_mp3, self).__init__(parent)


    def run(self):
        self.signal_cmp3_start.emit(1)
        for file in arr_webm:

            # Format file name before extrang mp3 music
            filename_old = file
            filename_new = filename_old.replace("&", "_")
            filename_new = filename_new.replace(" ", "_")
            filename_new = filename_new.replace("•", "_")

            os.rename(video_path + '\\' + filename_old, video_path + '\\' + filename_new)

            # pycharm exe
            os.system(ffmpeg_path + ' -i ' + video_path + '\\' + filename_new +
                      ' -vn -ar 44100 -ac 2 -ab 192k -f mp3 ' + audio_folder + '\\' + filename_new[:-5] + '.mp3')


            # exe
            #os.system(resource_path(ffmpeg_path) + ' -i ' + audio_path + '\\' + filename_new +
            #          ' -vn -ar 44100 -ac 2 -ab 192k -f mp3 ' + audio_path + '\\' + filename_new[:-5] + '.mp3')

            #os.remove(video_path + '\\' + filename_new)

        self.signal_cmp3_end.emit(1)
