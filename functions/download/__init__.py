def printif(check=False, stp='Hello World!'):

    if check == True:

        print(stp)
        return True
    
    else: return False

def renderer(youtube=None, verbose=True, res=None, fps=None, audqual=None):

    # from pydub import AudioSegment
    # import moviepy.editor as mpe
    from getpass import getuser
    import os, shutil, yaml, subprocess

    printif(verbose, 'Loading configs. (videos.yml, config.yml)')
    data = yaml.safe_load(open('files\\videos.yml', 'r'))
    config = yaml.safe_load(open('configs\\config.yml', 'r'))

    printif(verbose, 'Getting configs.')
    vidid = data[res][fps]
    audid = data['audio'][audqual][0]
    audtype = data['audio'][audqual][1]

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

    printif(verbose, 'Loading streams. (streams.xml)')
    video = youtube.streams.get_by_itag(vidid)
    audio = youtube.streams.get_by_itag(audid)

    printif(verbose, 'Creating temporary directory.')
    os.mkdir('temp')
    os.chdir('temp')

    printif(verbose, 'Getting video name.')
    illegalChars = config['illegalChars']
    yttitle = youtube.title
    for illegalChar in illegalChars:
        yttitle = yttitle.replace(illegalChar, '')

    printif(verbose, 'Downloading video. (video.mp4)')
    video.download(filename='video.mp4')
    # os.rename(f'{yttitle}.mp4', f'video.mp4')
    
    printif(verbose, f'Downloading audio. (audio.{audtype})                                                 ')
    audio.download(filename=f'audio.{audtype}')
    # os.rename(f'{yttitle}.{audtype}', f'audio.{audtype}.')

    printif(verbose, f'Trasforming audio.{audtype} to audio.mp3.                                            ')

    # audiof = AudioSegment.from_file(f'audio.{audtype}', format=audtype)
    # audiof.export('audio.mp3', format='mp3')
    subprocess.run(f'ffmpeg -i audio.{audtype} audio.mp3', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    printif(verbose, 'Adding video.mp4 and audio.mp3.')
    # videof = mpe.VideoFileClip('video.mp4')
    # audiof = mpe.AudioFileClip('audio.mp3')

    # outvideo = videof.set_audio(audiof)

    printif(verbose, f'Saving video. ({yttitle}.mp4)')
    os.chdir('..')

    subprocess.run(fr'ffmpeg -i temp\video.mp4 -i temp\audio.mp3 -c copy "{downloadDir}\{yttitle}.mp4"', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # outvideo.write_videofile(f'{yttitle}.mp4', logger='bar', verbose=False)

    shutil.rmtree('temp') 

def audio(youtube=None, verbose=True, audio=None):

    # from pydub import AudioSegment
    # import moviepy.editor as mpe
    from getpass import getuser
    import os, shutil, yaml, subprocess

    printif(verbose, 'Loading configs. (videos.yml, config.yml)')
    data = yaml.safe_load(open('files\\videos.yml', 'r'))
    config = yaml.safe_load(open('configs\\config.yml', 'r'))

    printif(verbose, 'Getting configs.')
    audid = data['audio'][audio][0]
    audtype = data['audio'][audio][1]

    try:
        downloadDir = int(config['downloadDir'])
        if downloadDir == 0:
            downloadDir = fr'C:\Users\{getuser()}\Downloads'
        elif downloadDir == 1:
            downloadDir = r'.\downloads'
    except:
        downloadDir = str(config['downloadDir'])
        downloadDir = downloadDir.replace('%u', getuser())

    printif(verbose, 'Loading streams. (streams.xml)')
    audio = youtube.streams.get_by_itag(audid)

    printif(verbose, 'Creating temporary directory.')
    os.mkdir('temp')
    os.chdir('temp')

    printif(verbose, 'Getting video name.')
    illegalChars = config['illegalChars']
    yttitle = youtube.title
    for illegalChar in illegalChars:
        yttitle = yttitle.replace(illegalChar, '')
    
    printif(verbose, f'Downloading audio. (audio.{audtype})                                                 ')
    audio.download()
    os.rename(f'{yttitle}.{audtype}', f'audio.{audtype}.')

    printif(verbose, f'Trasforming audio.{audtype} to audio.mp3.                                            ')

    os.chdir('..')
    subprocess.run(fr'ffmpeg -i temp\audio.{audtype} "{downloadDir}\{yttitle}.mp3"', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    shutil.rmtree('temp') 

def check(youtube=None, res=None, fps=None):

    import yaml

    data = yaml.safe_load(open('files\\videos.yml', 'r'))

    vidid = data[res][fps]

    check = youtube.streams.get_by_itag(vidid)
    if check != None: return True
    else: return False

def main(youtube=None, verbose=True, res=None, fps=None, audqual=None, jaudio=False):

    if jaudio == False:
        renderer(youtube, verbose, res, fps, audqual)
    else:
        audio(youtube, verbose, audqual)