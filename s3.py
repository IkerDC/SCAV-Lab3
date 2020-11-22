import os

class Container:
    def __init__(self, filename):
        self.video_file = filename
        self.tracks = self.read_stream()

    def read_stream(self):
        cmd = "ffmpeg -i " + self.video_file + " 2> metadata.txt"
        os.system(cmd)
        retrive = ["Stream #0:0(und)", "Stream #0:1(und)", "Stream #0:2(und)"]
        data = []
        with open('metadata.txt', 'rt') as myfile:
            contents = myfile.read()  # Read the entire file to a string
            for value in retrive:
                if (1 + contents.find(value)):  # If it doesnt exist it returns -1 = 1-1 = 0 = False
                    pos = contents.find(value)
                    start_pos = pos + len(value) + 9 # For the : Video:  or : Audio: part with len 9 always
                    end_pos = contents.find(' ', start_pos)  # Find the next space, so where codec ends
                    result = contents[start_pos:end_pos]  # Read from ...= to the next line
                    data.append(result)
        os.remove("metadata.txt")  # Remove the file we created
        return data

    def create_BBB_container(self):

        #Cut 1 min
        cut1 =  "ffmpeg -ss 00:00 -i " + self.video_file+ " -to 01:00 -c copy cut_"+self.video_file
        cut2 = "ffmpeg -i " + self.video_file + " -ss 00:00 -to 01:00 -c copy cut_" +self.video_file
        os.system(cut1)
        os.system(cut2)

        #Take the mono
        mono1 = "ffmpeg -i cut_" +self.video_file+ " -ac 1 mono_" +self.video_file
        mono2 = "ffmpeg -i mono_"+self.video_file+" -vn -acodec copy mono.aac"
        os.system(mono1)
        os.system(mono2)

        #Take lower bit rate
        audio = "ffmpeg -i cut_"+self.video_file+" -vn -acodec copy audio.ac3"
        low_bit = "ffmpeg -i audio.ac3 -codec:a libmp3lame -b:a 56k low_audio.ac3"
        os.system(audio)
        os.system(low_bit)

        os.remove("audio.ac3") #temporal elements
        os.remove("mono_bbb.mp4")#temporal elements
        self.pack_to_BBB_container()

    def pack_to_BBB_container(self):
        stream = []
        print("Introduce streams to pack (for exercice 1 is: cut_bbb.mp4, mono.aac, low_audio.ac3, subtitles.srt) and 0 to pack everything")
        cmd = ""
        a = True
        while (a):
            x = input()
            if (x == "0"):
                a = False
            else:
                stream.append(x)
        for track in stream:
            cmd = cmd+" -i "+track
        os.system("ffmpeg"+cmd+" -c:v copy -c:a copy -c:s mov_text new_video.mp4")

    def broadcasting(self, brd_std, streams ):
        possible_std = []
        print("Streams of the video:", streams)
        for key in brd_std:
            if(all(elem in brd_std[key]  for elem in streams)):
                possible_std.append(key)
                print("Possible standart:", key)
        if not possible_std:
            print("ERROR: The given streams don't belong to any standart, or not all of them the stream are compatible with one same standart")
        return  possible_std

    def test_broadcasting(self, brd_std):
        streams = []
        print("Introduce streams (as many as you want) or 0 to test:")
        a = True
        while(a):
            x = input()
            if (x == "0"):
                a = False
            else:
                streams.append(x)
        self.broadcasting(brd_std, streams)




vid = Container("bbb.mp4")
video_audio_std = dict([
    ("DVBT-T", ["mpeg2","h264","aac","ac3","mp3"]),
    ("ISBD-T", ["mpeg2","h264","aac"]),
    ("ATSC", ["mpeg2","h264","ac3"]),
    ("DTMB", ["avs","avs+","mpeg2","h264","dra","aac","mp2","mp3"])
])
#MENU---------------------------------------------------------------------
def switch(ex):
    if(ex == "1"):
        vid.create_BBB_container()
        return True
    elif(ex == "2"):
        vid.pack_to_BBB_container()
        return True
    elif(ex == "3"):
        vid.broadcasting(video_audio_std, vid.tracks)
        return True
    elif(ex== "4"):
        vid.test_broadcasting(video_audio_std)
        return True
    else:
        return False
#------------SELECT
menu = True
while(menu):
    print("Select opreation:\n1: Cut BBB, get audios and subtitle and package in new mp4\n"
          "2:Package given files to .mp4 container\n"
          "3:Recomend broadcast for bbb video\n"
          "4:Recoment broadcast for given streams\n"
          "0: Exit")
    x = input()
    menu = switch(x)








