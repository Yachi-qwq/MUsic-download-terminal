import urllib.request
import re
import pyfiglet
import youtube_dl

print(pyfiglet.figlet_format("Music Download"))
print("-"*40)

inp = input("♫ Song name: ")
if inp == "":
    print(f"✖ give a song name to download")
else:
    print("✔ Song found!\n✔ Downloading . . .")
    print("\n")
    inp_out = inp.replace(" ", "+")
    html = urllib.request.urlopen(f'https://www.youtube.com/results?search_query={inp_out}')
    song_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print(song_ids[0])

    #downloading
    video_url = f"https://www.youtube.com/watch?v={song_ids[0]}"
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("\n")
    print("✔ Downloaded\n→ File name: {}".format(filename))
    input("→ Press enter key to exit . . .")
