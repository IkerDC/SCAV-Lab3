### SCAV-S3

This code is intended to satisfy the requirements of the practice 3 from the course Audio and Video Encoding Systems (University Pompeu Fabra, 2020).


<img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Logo_UPF.jpg" width="128" height="44" />

# Instalation
This code was writen in Python via IDE PyCharm (in Windows). It makes uses of **ffmpeg**, to download it acces [https://ffmpeg.org/](https://ffmpeg.org/) or install it using commands (if ffmpeg is instaled in Windows, please allow the terminal to directly execute it by adding the path to the folder where ffmpeg will be loacted). A Python interpreter is expected to already be instaled, so the code can be run. The only library that this code uses is *os*.

# Requirements
In order for the code to work, FFmpeg must be instaled. In the other hand, we have a fucntion to rename what ever file, thus a file is required. Aswell as a video or image file 
that will be used in the resize fucntion and the metadata reading fucntion.

# Operations
* **Generate new container**: This in this first part, we begin by cutting a video using the seeking operation in *ffmpeg* that we have already used in multiples practices and seminars, then aswell, we get a mono track form this video, then we do the same with the audio track at a lower bit rate, this time, this is new. To do it, we have first of all extracted the 5.1 ac3 audio file fro the video, and the copied it to a new ac3 track with a lower bit rate. Then we have downloaded the subtitles for the video. Finally, we have packaged everything into a new mp4 file using the following function. Be carfull one of the operations reencode, thus, it takes longer.
* **Automate container creation**: This fucntion as we said, is used by the one above, as the name points out, it automates the creation of mp4 containers, as it is written, it allows the user to introduce as many streams as desired of video, audio and subtitles, the correct format of them is left to the user to control. It used *ffmpeg*, the command *-i ... -c:... copy* with the respective streams (files) and *v,a,s* for video, audio and subtitles. As it is mp4, we especify a *mov_text* parameter in the subtitles, and then copy everything into a new video without reencoding. As we have already said, all the streams are left to the user, they must be in the folder and at least a video, audio and subtitle stream must be added in order for it to work at first instance. 
* **Broadcasting Standarts**: To propose a Broadcastisng standarts depending on the streams, we have to read the streams that we have and be sure that at least all of them are
in the standart, otherwise, that standart would not fit the video, or at least, the video will have some streams that are incompatible with the standart. To do this, we read all the standarts, and check if all the streams introduced or read belong to it. Otherwise, we do check if one of the streams is no compatible or neither of them it is. For exercice 3 we have direcly read the the streams of the bbb video and we get the european standart. To read them, we have used the fucntion from the last practice, but modified so we get more values, e.g. the streams.
* **Test Broadcasting Standart**: This fucntion will read input from the user and depending on the streams introduced, it will use the fucntion above to provide a standart. This function is organized as a test funtion, so what ever, and as many as desired streams can be introduced. 


# Usage

The code works by reading user input to select the exercices and diferent opertions. Whenever a file is required, it must be intorduced with its format (.txt, .mp4, etc).
Then the other inputs required are explained in the output.
As required by the practice, everything is encapsuled in a class, even tho some operations are not logical, we have still created the class and put them there to show case we can work with classes. 


## Contact

Iker Diaz Cilleruelo - iker.diaz01@estudiant.upf.edu
Project Link: [https://github.com/IkerDC/SCAV-P2](https://github.com/IkerDC/SCAV-P2)

## Acknowledgements
* [FFmpeg](https://ffmpeg.org/)
* [FFmpeg Seeking](https://trac.ffmpeg.org/wiki/Seeking)
* [FFmpeg Audio](https://trac.ffmpeg.org/wiki/Encode/AAC)
* [Broacasting standarts](https://en.wikipedia.org/wiki/Broadcast_television_systems)
