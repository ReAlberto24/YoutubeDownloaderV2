libs = {
    'standards.tab': '	',
    'standards.space': ' ',
    'standards.space.default': 4,
}

def unify(lines:list) -> list:
    try:
        version = 0
        if lines[0].replace(' ', '').split(':')[0] == '#!Version': version = int(lines[0].replace(' ', '').split(':')[1].replace('.', ''))
        else: version = 100
        if version == 200:
            unifiedLines = []
            search = 0
            for i, line in enumerate(lines):
                linews = line.replace(' ', '')
                if search > 0:
                    search -= 1
                    continue
                if linews[len(linews)-1] == '[':
                    find = False
                    while not find:
                        search += 1
                        if lines[i+search][0] == ']':
                            find = True
                    unifiedLines.append(''.join(lines[i:i+search+1]))
                elif linews[len(linews)-1] == '{':
                    find = False
                    while not find:
                        search += 1
                        if lines[i+search][0] == '}':
                            find = True
                    unifiedLines.append(''.join(lines[i:i+search+1]))
                else:
                    # try:
                    #     linews.split('=')[0]
                    #     unifiedLines.append(line.split())
                    # except: unifiedLines.append(linews)
                    unifiedLines.append(linews)

            return unifiedLines
        elif version == 100:
            return lines

        else: return -1

    except: raise SyntaxError('Error while normalizing and unifing code')

def parse(unifiedLines:list) -> list:
    try:
        parsedVersion = 0
        plist = []
        if unifiedLines[0].split(':')[0] == '#!Version': parsedVersion = int(unifiedLines[0].split(':')[1].replace('.', ''))
        else: parsedVersion = 100
        if parsedVersion == 200: 
            tabType, tabSize = 0, 0
            plist.append(parsedVersion)
            for i, uline in enumerate(unifiedLines):
                if uline[0] == '#' and uline[1] != '!': continue
                elif ''.join(uline[0:1]) == '#!':
                    for suline in uline.replace('#!').split(','):
                        if suline == '': continue
                        if suline.split(':')[0] == 'TabType':
                            try: tabType = libs[suline.split(':')[1]]
                            except: tabType = suline.split(':')[1]
                        elif suline.split(':')[0] == 'TabSize':
                            try: tabSize = libs[suline.split(':')[1]]
                            except: tabSize = suline.split(':')[1]
                elif '=' in uline:
                    plist.append(('var', '=', uline.split('=')[0], uline.split('=')[1]))
                elif 'languageArray' in uline or 'languageList' in uline:
                    plist.append(('ll', uline.replace('languageArray', '').replace('languageList', '').split(':', 1)[0][1::], uline.replace('languageArray', '').replace('languageList', '').split(':', 1)[1]))
                elif 'languageJson' in uline or 'languageDict' in uline:
                    plist.append(('ld', uline.replace('languageJson', '').replace('languageDict', '').split(':', 1)[0][1::], uline.replace('languageJson', '').replace('languageDict', '').split(':', 1)[1]))
                else:
                    if ''.join(uline[0:2]) == '#!': pass
                    else:
                        raise TypeError(f'Error while parsing line: \n  {uline}\n  id: {i}')

            return plist
        elif parsedVersion == 100:
            language = []
            language.append(parsedVersion)
            readlanguage = False

            for line in unifiedLines:
                                                                                                        
                if line.replace('\n', '').replace(' ', '') == '#l!':

                    readlanguage = True
                    continue
                
                elif line.replace('\n', '').replace(' ', '') == '#l?':

                    readlanguage = False

                if readlanguage == True:

                    language.append(line.replace('\n', ''))

            return language

        else: return -1

    except: raise SyntaxError('Error while parsing normalized and unified code')

def read(parsedLines:list) -> dict:
    try:
        import json
        language = {}
        version = 0
        for i, pline in enumerate(parsedLines):
            if i == 0:
                version = pline
                continue
            if version == 200:
                if pline[0] == 'var':
                    language[pline[2]] = pline[3]
                elif pline[0] == 'll':
                    language[pline[1]] = json.loads(('{"t": '+pline[2].replace("'", '"')+'}'))['t']
                elif pline[0] == 'ld':
                    language[pline[1]] = json.loads(('{"t": '+pline[2].replace("'", '"')+'}'))['t']
            elif version == 100:
                dplines = parsedLines
                del dplines[0]
                return dplines
        return language
    except Exception as e: raise SyntaxError(f'Error while reading normalized, unified and parsed code')