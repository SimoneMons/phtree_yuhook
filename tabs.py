import sys
import os
import datetime

import PIL

from PIL import Image

from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QProgressBar
from PyQt6.QtCore import QThread

from PyQt6 import QtGui
from PyQt6.QtGui import QPixmap

from download_video import Download, Progressbar

from validate_link import validate_link

# Resource path
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        print(' ')
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("venv"), relative_path)


class youdwnl_tabs(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)


        # Label
        self.label = QLabel(self)
        self.label.setStyleSheet('color: black')
        self.label.setFont(QtGui.QFont('Arial', 10))
        self.label.setText("Download music and video from youtube")
        self.label.setGeometry(60, 35, 300, 20)

        # Link text
        self.linktextbox = QLineEdit(self)
        self.linktextbox.setText("Copy link to download")
        self.linktextbox.setGeometry(60, 65, 360, 18)
        self.linktextbox.returnPressed.connect(self.oh_no_download)

        # Download button
        self.dwl_button = QPushButton('Download', self)
        self.dwl_button.setToolTip('Click here to start the download')
        self.dwl_button.setFont(QtGui.QFont('Arial', 10))
        self.dwl_button.setGeometry(95, 100, 90, 25)
        self.dwl_button.clicked.connect(self.oh_no_download)

        # Progress bar
        self.pgbar = QProgressBar(self)
        self.pgbar.setGeometry(70, 145, 370, 12)
        self.pgbar.setValue(0)

        # Message text
        self.textmessage_info = QLabel(self)
        self.textmessage_info.setStyleSheet('color: black')
        self.textmessage_info.setText("Click here to start the download")
        self.textmessage_info.setFont(QtGui.QFont('Arial', 10))
        self.textmessage_info.setGeometry(200, 104, 300, 20)

        # Message text signal
        self.textmessage = QLabel(self)
        self.textmessage.setStyleSheet('color: black')
        self.textmessage.setText("Ready to download")
        self.textmessage.setFont(QtGui.QFont('Arial', 10))
        self.textmessage.setGeometry(95, 170, 300, 20)

        img = Image.open('./images/cappuccino-removebg-preview.png')  # image extension *.png,*.jpg
        new_width = 40
        new_height = 40
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save('./images/aaaa.png')  # format may what you want *.png, *jpg, *.gif


        # photo
        self.photo_label = QLabel(self)
        photo_path = './images/aaaa.png'

        # Pycharm
        pixmap = QPixmap(photo_path)

        # Exe
        #pixmap = QPixmap(resource_path(photo_path))

        self.photo_label.setPixmap(pixmap)
        self.photo_label.setGeometry(455, 340, 40, 40)

        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")

        message_mons = "By Mons {}".format(year)


        # Label
        self.label_mons = QLabel(self)
        self.label_mons.setStyleSheet('color: black')
        self.label_mons.setFont(QtGui.QFont('Arial', 7))
        self.label_mons.setText(message_mons)
        self.label_mons.setGeometry(505, 355, 100, 20)


        '''
        self.tab3.info = QPlainTextEdit(self.tab3)
        self.tab3.info.setGeometry(25, 35, 750, 450)
        self.tab3.info.setFont(QtGui.QFont('Arial', 12))
        self.tab3.info.insertPlainText(
            "\n" + 'Download Music and Videos from Youtube and Nostalgia Machine' + "\n" + "\n" + "\n")

        self.tab3.info_details = QPlainTextEdit(self.tab3)
        self.tab3.info_details.setGeometry(25, 80, 750, 450)
        self.tab3.info_details.setFont(QtGui.QFont('Arial', 10))
        self.tab3.info_details.insertPlainText("\n" +
                                               'You can search your music (free text) or to introduce the link of your favorite video' + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            'Examples:' + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            'https://www.youtube.com/watch?v=RB-RcX5DS5A' + "\n" + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            'https://www.youtube.com/watch?v=Z9AmPSXAOFw&list=RDRB-RcX5DS5A&index=7' + "\n" + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            'or a Playlist:' + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            'https://www.youtube.com/playlist?list=RDEMDHx1mzcs_wPqWOntgHDScQ' + "\n" + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            'Check files in:' + "\n" + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            '       ~\Downloads\yuhook_music' + "\n" + "\n" + "\n")
        self.tab3.info_details.insertPlainText(
            '       ~\Downloads\yuhook_videos' + "\n" + "\n" + "\n")
        '''

    def set_text_message_download(self, val):
        if val == 0:
            message = "Downloading"
            self.textmessage.setText(message)
        if val == 1:
            message = "Download ended, creating mp3 file"
            self.textmessage.setText(message)
        if val == 2:
            message = "MP3 file created, ready to downoad a new video"
            self.textmessage.setText(message)
            self.linktextbox.setText("Copy link to download")



    def set_ProgressBar(self, val):
        self.pgbar.setValue(val)

    def reset_ProgressBar(self):
        self.pgbar.setValue(0)


    def oh_no_download(self):
        link_to_dwl = self.linktextbox.text()

        # Validate link to download
        valid_link = validate_link(link_to_dwl)

        if valid_link == 1:
            message = "Not valid link"
            self.textmessage.setText(message)
        else:
            message = "Video available, starting download"
            self.textmessage.setText(message)

            print('Holaaaaaaa', link_to_dwl)

            self.dwnl_thread = Download(link_to_dwl)
            self.dwnl_thread.signal_start_download.connect(self.set_text_message_download)
            self.dwnl_thread.start()

            self.pgbar_thread = Progressbar()
            self.pgbar_thread.signal_prgb.connect(self.set_ProgressBar)
            self.pgbar_thread.signal_prgb_end.connect(self.reset_ProgressBar)
            self.pgbar_thread.start()




