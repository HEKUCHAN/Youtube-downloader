import os
import youtube_dl

download_url = 'https://www.youtube.com/watch?v=9MjAJSoaoSo'
output_file_name = 'abe'

ydl_opts = {
    'format': 'bestaudio[ext = mp3]/bestaudio[ext = m4a]/bestaudio',
    'outtmpl':  os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Desktop\\" + '%(title)s-%(id)s.%(ext)s',
}

ydl = youtube_dl.YoutubeDL(ydl_opts)
result = ydl.extract_info(download_url, download=True)
