# Introduction:

YouTube is the world’s most common video sharing site, and you can experience a situation as a hacker where you want to script something to download videos. For this, We present Pytube to you.

1. Pytube is a lightweight, Python-written library. It does not have third-party dependencies and strives to be extremely secure.
2. Pytube also simplifies pipelining, allowing you to define callback functionality for various download events, such as progress or completion.
3. Finally, pytube also provides a command-line feature that allows you to stream videos directly from the terminal easily.

To import pytube, we can use the commands according to the python version.

> pip3 install pytube

To save the audio file, we are using the os module and import by using the command given below :

> pip install os_sys

# Procedure:

1. First, we need to import the required (pytube and os) module.
2. Then we take input from the user i.e; the link of the YouTube video.
3. As, we need only an audio file from that video, so we use the filter method.
4. Now we need to set the output path of the audio file, which we will do by using the os module.
5. Now finally we can change the audio extension to MP3 and play our audio.
