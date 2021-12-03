# Required system
 - Windows 7/8/10/11..
 - Stable internet connection
 - A little knowledge of a computer

<br>


# How to use
First locate file called "..start" or "..start.bat" the double click and will open a black window then will says: " (Project) Start "

After you will paste the link from youtube

<br>

Then it will ask the quality and use for example

to download a video at 240p quality use "2" or to download an audio use "11"

after this will download the requested video/audio

<br>

# How to change configuration
In configs/config.yml you will find:
```yaml
# %u = User Name
# 0 = Default Windows Download 
# 1 = Project Download
# Example: C:\Users\%u\Desktop\
downloadDir: 1

# Language used
# Usable languages: de, en, es, fr, it
# de: German, Deutsch
# en: English
# es: Spanish, Español
# fr: French, Français
# it: Italian, Italiano
language: en

# DO NOT CHANGE
gui: 0

# SAME
illegalChars: ['\\', '/', ':', '*', '?', '<', '>', '|', '.', ',', "'", '"', '%', '$', '~']
```
To change donload directory just follow instructions and change "downloadDir"

And same for language

The rest leave as it is can break the program if changed