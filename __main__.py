import yaml

config = yaml.safe_load(open('configs\\config.yml', 'r'))

if config['gui'] == 0:
    import terminal

    print('PyYoutubeDownloader. Started as terminal mode')
    terminal.main()
elif config['gui'] == 1:
    import gui

    print('PyYoutubeDownloader. Started as gui mode')
    gui.main()
else: pass