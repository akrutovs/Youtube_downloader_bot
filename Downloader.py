from pytube import YouTube

folder = '/Users/a_krut/Desktop/Download_video_bot/videos'
def find_stream(url):

    youtube_obj = YouTube(url)
    stream = youtube_obj.streams
    stream = stream.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    return stream

def get_file_name(url):
    youtube_obj = YouTube(url)
    filename = youtube_obj.title
    return filename

def download(url,stream):
    youtube_obj = YouTube(url)
    filename = youtube_obj.title
    filename = str(filename) + 'mp4'
    stream.download(folder, filename)