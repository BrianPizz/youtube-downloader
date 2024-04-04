from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try: 
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        

    except Exception as e:
        print(e)