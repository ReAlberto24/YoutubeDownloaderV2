def printif(check:bool=False, stp:str='Hello World!') -> None:
    if check == True: print(stp)

def renderer(youtube=None, verbose=True, res=None, fps=None, audqual=None):

    # from pydub import AudioSegment
    # import moviepy.editor as mpe
    from getpass import getuser
    import os, shutil, yaml, subprocess, traceback, libs.languageReader as lr

    try:

        ########
        # Loading Configs
        config = yaml.safe_load(open('configs\\config.yml', 'r'))
        
        # Load language
        language = lr.load('default.plcf')[config['language']]
        
        # Load videos tags
        printif(verbose, language[9])
        data = yaml.safe_load(open('files\\videos.yml', 'r'))
        ########

        ########
        # Get video and audio tags from file using func vars 
        # printif(verbose, language[10])
        vidid = data[res][fps]
        audid = data['audio'][audqual][0]
        audtype = data['audio'][audqual][1]
        ########

        ########
        # Set download dir
        try:
            downloadDir = int(config['downloadDir'])
            if downloadDir == 0:
                downloadDir = fr'C:\Users\{getuser()}\Downloads'
            elif downloadDir == 1:
                try: os.mkdir(r'.\downloads')
                except: pass
                downloadDir = r'.\downloads'
        except:
            downloadDir = str(config['downloadDir'])
            downloadDir = downloadDir.replace('%u', getuser())
        ########

        ########
        # Get streams from tags
        printif(verbose, language[11])
        video = youtube.streams.get_by_itag(vidid)
        audio = youtube.streams.get_by_itag(audid)
        ########

        ########
        # Create and enter temp dir
        printif(verbose, language[12])
        os.mkdir('YDv2-func-tempdir')
        os.chdir('YDv2-func-tempdir')
        ########

        ########
        # Get video name without illegal chars
        printif(verbose, language[13])
        illegalChars = config['illegalChars']
        yttitle = youtube.title
        for illegalChar in illegalChars:
            yttitle = yttitle.replace(illegalChar, '')

        videoName = 'video.mp4'
        audioName = f'audio.{audtype}'
        ########

        ########
        # Download audio and video files
        printif(verbose, language[14])
        video.download(filename='video.mp4')
        # os.rename(f'{yttitle}.mp4', f'video.mp4')
        
        printif(verbose, language[15].replace('$%3', audioName))
        audio.download(filename=f'audio.{audtype}')
        # os.rename(f'{yttitle}.{audtype}', f'audio.{audtype}.')
        ########

        ########
        # Transform audio file from [current fromat] to mp3 using ffmpeg
        printif(verbose, language[16].replace('$%3', audioName))

        # audiof = AudioSegment.from_file(f'audio.{audtype}', format=audtype)
        # audiof.export('audio.mp3', format='mp3')
        subprocess.run(f'ffmpeg -i audio.{audtype} audio.mp3', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        ########

        ########
        # Last will unify audio and video together
        printif(verbose, language[17])
        # videof = mpe.VideoFileClip('video.mp4')
        # audiof = mpe.AudioFileClip('audio.mp3')

        # outvideo = videof.set_audio(audiof)

        printif(verbose, language[18].replace('$%2', yttitle+'.mp4'))
        os.chdir('..')

        subprocess.run(fr'ffmpeg -i YDv2-func-tempdir\video.mp4 -i YDv2-func-tempdir\audio.mp3 -c copy "{downloadDir}\{yttitle}.mp4"', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        # outvideo.write_videofile(f'{yttitle}.mp4', logger='bar', verbose=False)
        ########

        # Then remove temp dir
        shutil.rmtree('YDv2-func-tempdir') 

    except:
        ########
        # If error then print it
        try: shutil.rmtree('YDv2-func-tempdir')
        except: pass
        traceback.print_exc()
        ########

def audio(youtube=None, verbose=True, audqual=None):

    # from pydub import AudioSegment
    # import moviepy.editor as mpe
    from getpass import getuser
    import os, shutil, yaml, subprocess, traceback, libs.languageReader as lr

    try:

        ########
        # Loading Configs
        config = yaml.safe_load(open('configs\\config.yml', 'r'))
        
        # Load language
        language = lr.load('default.plcf')[config['language']]
        
        # Load videos tags
        printif(verbose, language[9])
        data = yaml.safe_load(open('files\\videos.yml', 'r'))
        ########

        ########
        # Get video and audio tags from file using func vars 
        # printif(verbose, language[10])
        audid = data['audio'][audqual][0]
        audtype = data['audio'][audqual][1]
        ########

        ########
        # Set download dir
        try:
            downloadDir = int(config['downloadDir'])
            if downloadDir == 0:
                downloadDir = fr'C:\Users\{getuser()}\Downloads'
            elif downloadDir == 1:
                try: os.mkdir(r'.\downloads')
                except: pass
                downloadDir = r'.\downloads'
        except:
            downloadDir = str(config['downloadDir'])
            downloadDir = downloadDir.replace('%u', getuser())
        ########

        ########
        # Get streams from tags
        printif(verbose, language[11])
        audio = youtube.streams.get_by_itag(audid)
        ########

        ########
        # Create and enter temp dir
        printif(verbose, language[12])
        os.mkdir('YDv2-func-tempdir')
        os.chdir('YDv2-func-tempdir')
        ########

        ########
        # Get video name without illegal chars
        printif(verbose, language[13])
        illegalChars = config['illegalChars']
        yttitle = youtube.title
        for illegalChar in illegalChars:
            yttitle = yttitle.replace(illegalChar, '')

        audioName = f'audio.{audtype}'
        ########

        ########
        # Download audio file
        
        printif(verbose, language[15].replace('$%3', audioName))
        audio.download(filename=f'audio.{audtype}')
        # os.rename(f'{yttitle}.{audtype}', f'audio.{audtype}.')
        ########

        ########
        # Transform audio file from [current fromat] to mp3 using ffmpeg
        printif(verbose, language[16].replace('$%3', audioName))

        os.chdir('..')
        # audiof = AudioSegment.from_file(f'audio.{audtype}', format=audtype)
        # audiof.export('audio.mp3', format='mp3')
        subprocess.run(f'ffmpeg -i YDv2-func-tempdir\\audio.{audtype} {downloadDir}\\audio.mp3', stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        ########

        # Then remove temp dir
        shutil.rmtree('YDv2-func-tempdir') 

    except:
        ########
        # If error then print it
        try: shutil.rmtree('YDv2-func-tempdir')
        except: pass
        traceback.print_exc()
        ########

def check(youtube=None, res=None, fps=None):
    import yaml

    # Get tags
    data = yaml.safe_load(open('files\\videos.yml', 'r'))
    # Get video tag
    vidid = data[res][fps]
    # Check if it exist
    check = youtube.streams.get_by_itag(vidid)
    # Return
    if check != None: return True
    else: return False

def main(youtube=None, verbose=True, res=None, fps=None, audqual=None, jaudio=False):

    if jaudio == False:
        renderer(youtube, verbose, res, fps, audqual)
    else:
        audio(youtube, verbose, audqual)