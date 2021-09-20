from tkinter import filedialog
import os
import youtube_dl
import sys
import tkinter as tk
import json
import tkinter.ttk as ttk


def check_file(path):
    return os.path.isfile(path)

app = tk.Tk()

app.title("Komakoma専用YouTubeダウンローダー")
app.geometry("400x200")
app.resizable(False, False)

dir = os.path.abspath('./')
file_dir = os.path.expanduser('~')

if not check_file(os.getcwd() + "user.json"):
    file = open(os.getcwd() + "/user.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
else:
    file = open(os.getcwd() + "/user.json", "w", encoding="utf-8")
    app_data = {'path': os.path.expanduser('~')}
    data = json.dump(app_data, file, indent=4)
    file.close()
    file = open(os.getcwd() + "/user.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()

def path_slect_btn():
    global fld
    fld = filedialog.askdirectory(initialdir=dir)
    txt.delete(0, tk.END)
    txt.insert(tk.END, fld)

lbl = tk.Label(text='ダウンロード先フォルダー')
lbl.place(x=30, y=15)
txt = tk.Entry(width=40)
txt.place(x=30, y=42)
txt.insert(tk.END, data['path'])

url_lbl = tk.Label(text='URL')
url_lbl.place(x=30, y=60)
url = tk.Entry(width=40)
url.place(x=30, y=80)
url.insert(tk.END, "")

path_select = tk.Button(
    app,
    text="path選択",
    command=path_slect_btn
)
path_select.place(x=290, y=38)

select = ['mp3', 'mp4']

combo_lbl = tk.Label(text='拡張子')
combo_lbl.place(x=30, y=100)

combo = ttk.Combobox(app, state='readonly')
combo["values"] = ("mp4", "mp3")
combo.current(0)
combo.place(x=30, y=120)

def encode_audio(url, path):
    ydl_opts = {
        'format': 'bestaudio[ext = mp3]/bestaudio[ext = m4a]/bestaudio',
        'outtmpl':  path + '/%(title)s.%(ext)s',
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    result = ydl.extract_info(url, download=True)

def encode_video(url, path):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl':  path + '/%(title)s-%(id)s.%(ext)s',
    }

    ydl = youtube_dl.YoutubeDL(ydl_opts)
    result = ydl.extract_info(url, download=True)


def encode_btn():
    data["path"] = txt.get()
    file = open(os.getcwd() + "/user.json", "w", encoding="utf-8")
    saved_file = json.dump(data, file, indent=4)
    file.close()

    if combo.get() == "mp3":
        encode_audio(url.get(), txt.get())
    else:
        encode_video(url.get(), txt.get())

encode = tk.Button(
    app,
    text="エンコード",
    command=encode_btn
)
encode.place(x=30, y=160)

app.mainloop()

# download_url = 'https://www.youtube.com/watch?v=9MjAJSoaoSo'
# output_file_name = 'abe'

# ydl_opts = {
#     'format': 'mp4',
#     'outtmpl':  os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop\\" + '%(title)s-%(id)s.%(ext)s',
# }

# ydl = youtube_dl.YoutubeDL(ydl_opts)
# result = ydl.extract_info(download_url, download=True)
