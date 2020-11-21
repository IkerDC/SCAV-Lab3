### SCAV-S3

This code is intended to satisfy the requirements of the practice 2 from the course Audio and Video Encoding Systems (University Pompeu Fabra, 2020).


<img src="https://upload.wikimedia.org/wikipedia/commons/5/53/Logo_UPF.jpg" width="128" height="44" />

# Instalation
This code was writen in Python via IDE PyCharm (in Windows). It makes uses of **ffmpeg**, to download it acces [https://ffmpeg.org/](https://ffmpeg.org/) or install it using commands (if ffmpeg is instaled in Windows, please allow the terminal to directly execute it by adding the path to the folder where ffmpeg will be loacted). A Python interpreter is expected to already be instaled, so the code can be run. The only library that this code uses is *os*.

# Requirements
In order for the code to work, FFmpeg must be instaled. In the other hand, we have a fucntion to rename what ever file, thus a file is required. Aswell as a video or image file 
that will be used in the resize fucntion and the metadata reading fucntion.

# Operations
* **Broadcasting Standarts**: To propose a Broadcastisng standarts depending on the streams, we have to read the strams that we have and be sure taht at least all of them are
in the standart, otherwise, that standart would not fit the video, or at least, the video will have some streams, incompatible with the standart.To do this, we read all the standarts, and check if all the streams belong to it. Otherwise, we do check if one of the streams is no compatible or neitehr of them it is.


# Usage

The code works by reading user input to select the exercices and diferent opertion. Whenever a file is required, it must be intorduced with its format (.txt, .mp4, etc).
Then the other inputs required are explained in the output.


## Contact

Iker Diaz Cilleruelo - iker.diaz01@estudiant.upf.edu
Project Link: [https://github.com/IkerDC/SCAV-P2](https://github.com/IkerDC/SCAV-P2)

## Acknowledgements
* [FFmpeg](https://ffmpeg.org/)
* [FFmpeg Scaling](https://trac.ffmpeg.org/wiki/Scaling)
* [FFmpeg Codec AV1](https://trac.ffmpeg.org/wiki/Encode/AV1)
* [FFmpeg Audio](https://trac.ffmpeg.org/wiki/Encode/AAC)
