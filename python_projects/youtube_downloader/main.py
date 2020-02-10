from pytube import *


url = "https://www.youtube.com/watch?v=FQSpfS7zHdg"
save_path = "C:\\Users\\Katlic\\Desktop"

obj = YouTube(url)

strms = obj.streams.all()

strms = strms.split(',')

print(strms)