from pytube import YouTube

folder = '/Users/a_krut/Desktop/'
def find_stream(url):

    youtube_obj = YouTube(url)
    stream = youtube_obj.streams
    stream = stream.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    #print(stream)
    return stream

def download(stream):
    stream.download(folder)