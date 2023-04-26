from moviepy.editor import *

mp4_file = "Neenaade Naa Video Song -Yuvarathnaa (Kannada)  Puneeth Rajkumar Santhosh Ananddram Hombale Films.mp4"

mp3_file = "Neenaade Naa Video Song -Yuvarathnaa (Kannada)  Puneeth Rajkumar Santhosh Ananddram Hombale Films.mp3"


videoClip = VideoFileClip(mp4_file)

audioclip = videoClip.audio

audioclip.write_audiofile(mp3_file)

audioclip.close()

videoClip.close()
import pafy

# opening the text file which contains all the links
file = open('list.txt', 'r')

# loop through each link in the file
for line in file:

    # Assign link to "url" variable
    url = line

    try:
        # Passing link to pafy
        video = pafy.new(url)

        # extracting the best available audio
        bestaudio = video.getbestaudio()
        print(video.title)

        # downloading the extracted audio
        bestaudio.download()

    # move to next link if the video is removed in the youtube platform
    except:
        pass

# close the text file
file.close()