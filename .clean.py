import yaml, shutil, os

ymlFile = yaml.safe_load(open('configs\\clean.yml', 'r'))

files = ymlFile['files']
if files == None: files = []
dirs = ymlFile['dirs']
if dirs == None: dirs = []

if len(files) > 0:
    for file in files:
        try: os.remove(file)
        except: pass

if len(dirs) > 0:
    for Dir in dirs:
        try: shutil.rmtree(Dir)
        except: pass
