import yaml

config = yaml.safe_load(open('configs\\config.yml', 'r'))

if config['gui'] == 0:
    #print('PyYoutubeDownloader. Started as terminal mode')

    import terminal
elif config['gui'] == 1:
    #print('PyYoutubeDownloader. Started as gui mode')

    import gui
else: pass