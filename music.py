import urllib.request
import re
import pyfiglet
#yt download
import youtube_dl
#https://appsgeyser.com/blog/convert-python-to-apk/


print(pyfiglet.figlet_format("Music Download"))
print("-"*40)

inp = input("♫ Song name: ")
if inp == "":
    print(f"✖ Gib einen Song titiel zum download ein")
else:
    print("✔ Song wurde gefunden!\n✔ Downloading . . .")
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
    print("✔ Erfolgreich heruntergeladen\n→ Datei Name: {}".format(filename))
    input("→ Enter Taste zum beebnden drücken . . .")