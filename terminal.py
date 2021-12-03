from pytube import YouTube
from pytube.cli import on_progress
import shutil, yaml, traceback
import libs.languageReader as lr
try:

    ########
    # Remove temp dir
    try: shutil.rmtree('YDv2-func-tempdir')
    except: pass
    ########

    ########
    # Loading Configs
    config = yaml.safe_load(open('configs\\config.yml', 'r'))
    
    # Load language
    language = lr.load('default.plcf')[config['language']]
    ########

    ########
    # Get link from user and check if it exist
    while True:
        link = input(language[0])
        print(language[1])
        try:
            yt = YouTube(link, on_progress_callback=on_progress)
            print(language[2])
            break
        except:
            print(language[3]+'\n')
    ########

    ########
    # Get resolutions
    resolution = []
    for i in yt.streams:
        try:
            if i.resolution == None or i.resolution == '1440p' or i.resolution == '2160p' or i.resolution == '4320p': 
                pass
            else: 
                resolution.append(int(i.resolution.replace('p', '')))
        except: pass
    resolution = sorted(set(resolution))
    tempres = []
    for i in resolution:
        tempres.append(f'{i}p') 
    resolution = tempres

    resolutions = ''
    index = 0
    for res in resolution:

        index += 1
        if index < len(resolution):
            resolutions += f'{res}:{index}, '
        else:
            resolutions += f'{res}:{index}'

    videoQuality = str(resolutions)
    audioQuality = ['48kbps:10, 128kbps:11, 160kbps:12', ['48kbps', '128kbps', '160kbps']]
    ########

    ########
    # Transform in index got resolution
    print(language[4]+'\n'+language[5]+'\n')
    print(language[7].replace('$%0',  videoQuality))
    print(language[8].replace('$%1', audioQuality[0]))

    gotQuality = False
    while not gotQuality:
        #quality = input('Quality ('+', '.join(resolution)+'): ').lower()
        # 144p:1, 240p:2, 360p:3, 480p:4, 720p:5, 1080p:6, 1440p:7, 2160p:8, 4320p:9
        quality = input(f': ').lower()
        try: 
            resolution[int(quality)-1]
            quality = resolution[int(quality)-1]
            gotQuality = True
            break
        except:
            try: 
                quality = int(quality)
                if quality == 10:
                    quality = '48kbps'
                elif quality == 11:
                    quality = '128kbps'
                elif quality == 12:
                    quality = '160kbps'
                gotQuality = True
                break
            except: 
                for res in resolution+audioQuality[1]:
                    if quality == res:
                        gotQuality = True
                        break
    ########
    print('')
    ########
    # Save streams
    streams = str(yt.streams).replace(', ', '\n').replace('[', '').replace(']', '')
    with open('files\\streams.xml', 'w') as streamf : 
        streamf.write('<?xml version="1.0" encoding="UTF-8"?>\n\n'+streams)
    ########

    ########
    # Download video (from inputs)
    import libs.download as download

    if quality == '1080p':
        if download.check(yt, '1080p', '60fps') == True:
            download.main(yt, True, '1080p', '60fps', '160kbps', False)
        else:
            download.main(yt, True, '1080p', '30fps', '160kbps', False)

    elif quality == '720p':
        if download.check(yt, '720p', '60fps') == True:
            download.main(yt, True, '720p', '60fps', '160kbps', False)
        else:
            download.main(yt, True, '720p', '30fps', '160kbps', False)

    elif quality == '480p':
        download.main(yt, True, '480p', 'default', '128kbps', False)
    
    elif quality == '360p':
        download.main(yt, True, '360p', 'default', '128kbps', False)

    elif quality == '240p':
        download.main(yt, True, '240p', 'default', '48kbps', False)
    
    elif quality == '144p':
        download.main(yt, True, '144p', 'default', '48kbps', False)

    elif quality == '48kbps':
        download.main(yt, True, None, None, '48kbps', True)

    elif quality == '128kbps':
        download.main(yt, True, None, None, '128kbps', True)

    elif quality == '160kbps':
        download.main(yt, True, None, None, '160kbps', True)
    ########
    
except:
    ########
    # If error then print it
    try: shutil.rmtree('YDv2-func-tempdir')
    except: pass
    traceback.print_exc()
    ########