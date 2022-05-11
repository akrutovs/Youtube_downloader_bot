from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=ROoo1eoOOvg'
folder = '/Users/a_krut/Desktop/'
youtube_obj = YouTube(video_url)
stream = youtube_obj.streams

stream = stream.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

print(stream)
stream.download(folder)