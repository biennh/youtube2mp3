## Welcome to youtube2mp3 homepage

* prerequisites:
pip3 install youtube-dl
pip3 install pysimplegui
sudo apt install ffmpeg

* build:
pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' youtube_mp3.py
