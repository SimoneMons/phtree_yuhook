import os
import sys

SAVE_PATH = os.path.expanduser('~/Downloads')


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        print(' ')
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("venv"), relative_path)


# Function to extract mp3 from videos
def create_mp3():
    # pycharm exe
    ffmpeg_path = ".\\ffmpeg\\ffmpeg.exe"

    # .exe
    # ffmpeg_path = "./ffmpeg/ffmpeg.exe"

    # Create audio folder
    audio_folder = os.path.join(SAVE_PATH, 'yuhook_music')

    if not os.path.isdir(audio_folder):
        os.mkdir(audio_folder)

    # video folder path
    video_path = os.path.expanduser('~\Downloads\yuhook_videos')

    # music folder path
    audio_path = os.path.expanduser('~\Downloads\yuhook_music')

    # List of videos in video path
    list_of_videos = [x for x in os.listdir(video_path) if x.endswith(".webm") or x.endswith(".m4a") or x.endswith(".mp4")]

    print(list_of_videos)

    # List of music in audio path
    list_of_audios = [x for x in os.listdir(audio_path) if x.endswith(".mp3")]

    list_of_audios_no_extension = []

    for file in list_of_audios:
        index_point_type = file.rfind('.')
        file_name_no_typeresult = file[:index_point_type]
        list_of_audios_no_extension.append(file_name_no_typeresult)


    print(list_of_audios_no_extension)

    for file in list_of_videos:
        # Format file name before extrang mp3 music
        filename_old = file
        filename_new = filename_old.replace("&", "_")
        filename_new = filename_new.replace(" ", "_")
        filename_new = filename_new.replace("•", "_")

        os.rename(video_path + '\\' + filename_old, video_path + '\\' + filename_new)

        index_point_type = filename_new.rfind('.')
        file_name_no_typeresult = filename_new[:index_point_type]

        if file_name_no_typeresult not in list_of_audios_no_extension:
            print('aquiiiiiiii', file_name_no_typeresult)

            # pycharm exe
            os.system(ffmpeg_path + ' -i ' + video_path + '\\' + filename_new +
                      ' -vn -ar 44100 -ac 2 -ab 192k -f mp3 ' + audio_path + '\\' + filename_new[:-4] + '.mp3')


            # exe
            #os.system(resource_path(ffmpeg_path) + ' -i ' + audio_path + '\\' + filename_new +
            #          ' -vn -ar 44100 -ac 2 -ab 192k -f mp3 ' + audio_path + '\\' + filename_new[:-4] + '.mp3')

            #os.remove(video_path + '\\' + filename_new)


