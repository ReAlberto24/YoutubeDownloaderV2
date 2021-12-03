from pytube import YouTube
from pytube.query import StreamQuery
import yaml, os, subprocess, shutil

class video:

    def getInfo(link=None):
        '''
        Get video info from link,
        
        in: link
        out: struct 
        '''

        yt = YouTube(link)

        infos = {
            'title': yt.title,
            'description': yt.description,
            'lenght': yt.length,
            'views': yt.views,
            'raitings': yt.rating,
            'age_restricted': yt.age_restricted,
            'author': yt.author,
            'thumbnail_url': yt.thumbnail_url,
            'keywords': yt.keywords
            }

        return infos

    def getStreams(link=None) -> StreamQuery:
        '''
        Return Streamquery from link,

        in: link
        out: StreamQuery
        '''

        yt = YouTube(link)

        return yt.streams

    def loadDefaultSavedStreams():
        '''
        Load saved Default Streams id,

        in: None
        out: struct
        '''

        data = yaml.safe_load(open('files\\videos.yml', 'r'))
        
        return data

class download:

    def video(youtube=None, res=None, fps=None, audqual=None, downloadDir=None) -> None:
        '''
        Download requested video,

        in: kwargs{youtube, res, fps, audqual, downloadDir}
        out: None
        fileOut: (videoName).mp4
        '''

        data = yaml.safe_load(open('files\\videos.yml', 'r'))
        config = yaml.safe_load(open('configs\\config.yml', 'r'))

        vidid = data[res][fps]
        audid = data['audio'][audqual][0]
        audtype = data['audio'][audqual][1]

        video = youtube.streams.get_by_itag(vidid)
        audio = youtube.streams.get_by_itag(audid)

        os.mkdir('YDv2-api-tempdir')
        os.chdir('YDv2-api-tempdir')

        illegalChars = config['illegalChars']
        yttitle = youtube.title
        for illegalChar in illegalChars:
            yttitle = yttitle.replace(illegalChar, '')

        video.download(filename='video.mp4')
        
        audio.download(filename=f'audio.{audtype}')

        subprocess.run(f'ffmpeg -i audio.{audtype} audio.mp3', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        os.chdir('..')
        subprocess.run(fr'ffmpeg -i YDv2-api-tempdir\video.mp4 -i YDv2-api-tempdir\audio.mp3 -c copy "{downloadDir}\{yttitle}.mp4"', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        shutil.rmtree('YDv2-api-tempdir') 

    def audio(youtube=None, audqual=None, downloadDir=None) -> None:
        '''
        Download requested audio,

        in: kwargs{youtube, audqual, downloadDir}
        out: None
        fileOut: (videoName).mp3
        '''

        data = yaml.safe_load(open('files\\videos.yml', 'r'))
        config = yaml.safe_load(open('configs\\config.yml', 'r'))

        audid = data['audio'][audqual][0]
        audtype = data['audio'][audqual][1]

        audio = youtube.streams.get_by_itag(audid)

        os.mkdir('YDv2-api-tempdir')
        os.chdir('YDv2-api-tempdir')

        illegalChars = config['illegalChars']
        yttitle = youtube.title
        for illegalChar in illegalChars:
            yttitle = yttitle.replace(illegalChar, '')
        
        audio.download(filename=f'audio.{audtype}')

        os.chdir('..')
        subprocess.run(fr'ffmpeg -i YDv2-api-tempdir\audio.{audtype} {downloadDir}\audio.mp3', shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        shutil.rmtree('YDv2-api-tempdir') 