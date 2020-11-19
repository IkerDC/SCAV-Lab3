import os

class Container:
    def __init__(self):
        self.video_file = ""
        self.mono_audio = ""
        self.low_audio = ""
        self.subtitle = ""

    def create_BBB_container(self):
        #Cut 1 min
        cut1 =  "ffmpeg -ss 00:00 -i " + self.video_file+ ".mp4 -to 01:00 -c copy cut_"+self.video_file
        cut2 = "ffmpeg -i " + self.video_file + ".mp4 -ss 00:00 -to 01:00 -c copy cut_" +self.video_file
        #Take the mono
        mono1 = "ffmpeg -i cut_" +self.video_file+ ".mp4 -ac 1 mono_" +self.video_file
        mono2 = "ffmpeg -i mono_"+self.video_file+" -vn -acodec copy mono.mp3"
        #TAKE LOWER BIT RATE



a = Container()
a.video_file = "bbb.mp4"
