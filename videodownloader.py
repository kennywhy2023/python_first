from pytube import YouTube

PATH = "D:/workspace/python_first"

link = ["https://www.youtube.com/watch?v=p8FuTenSWPI",
        "https://www.youtube.com/watch?v=JWbnEt3xuos"]

for i in link:
    try:
        yt = YouTube(i)
    except:
        print("connection error")

    #mp4files = yt.filter('mp4')

    #d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
    try:
        d_video.download(PATH)
    except:
        print("some Error!")

print("task completed!")