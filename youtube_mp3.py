from __future__ import unicode_literals
import PySimpleGUI as sg
import youtube_dl
import sys
import os


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

# collect arguments from GUI

sg.ChangeLookAndFeel('GreenTan')

form = sg.FlexForm('Everything bagel', default_element_size=(40, 1))

layout = [
    [sg.Text('Youtube video/playlist url:')],
    [sg.InputText('')],
    [sg.Text('_'  * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
    sg.InputText(os.getcwd()), sg.FolderBrowse()],
    [sg.Download(), sg.Cancel()]
    ]

window = sg.Window('Youtube mp3 Downloader', layout)
while True:
    event, values = window.read()
    #sg.Popup(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    else if event == 'Download':
        if values[0] == '':
            sg.Popup("Please input youtube url!")
            continue
        else:
            ydl_opts = {
                'outtmpl': values[1] + '/%(title)s.%(ext)s',
                'nooverwrites': 'true',
                'ignoreerrors': 'true',
                'nocheckcertificate': 'true',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'logger': MyLogger(),
                'progress_hooks': [my_hook],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([values[0]])
            sg.Popup("Downloading done!")

window.close()
