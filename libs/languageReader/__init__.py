# class lang:
#     def __init__(self, file:str, *args, **kwargs) -> None:
#         '''
#         Set language loader and parser initial variables.\n
#         ---------
#         [in]    file:str, [args, kwargs]\n
#         [out]   None
#         '''
#         import os
# 
#         if os.path.exists(file):
#             self.file = file
#         else:
#             raise FileNotFoundError(f'File "{file}" was not found')
#     
#     def load(self, *args, **kwargs) -> dict:
#         '''
#         Return readed and parsed language from file. \n
#         ---------
#         [in]    None\n
#         [out]   language:dict
#         '''
#         fileLines = []
#         from .. import normalizer
# 
#         with open(self.file, 'r') as file:
#             for line in file.readlines():
#                 if line.replace(' ', '') == '\n':
#                     pass
#                 else:
#                     # .replace('	', '').replace(' ', '').replace('_', ' ')
#                     fileLines.append(normalizer.normalize(line.replace('\n', '')))
# 
#         from . import parser
#         
#         unifiedLines = parser.unify(fileLines)
#         parsedLines = parser.parse(unifiedLines)
#         language = parser.read(parsedLines)
# 
#         return language
    
def load(file:str, *args, **kwargs) -> dict:
    '''
    Return readed and parsed language from file. \n
    ---------
    [in]    File\n
    [out]   language:dict
    '''
    fileLines = []
    from .. import normalizer

    with open(file, 'r') as file:
        # fileLines = ['' if line.replace(' ', '') == '\n' else normalizer.normalize(line.replace('\n', '')) for line in file.readlines()]
        # fileLines.remove('')
        for line in file.readlines():
            if line.replace(' ', '') == '\n':
                pass
            else:
                # .replace('	', '').replace(' ', '').replace('_', ' ')
                fileLines.append(normalizer.normalize(line.replace('\n', '')))

    from . import parser
    
    unifiedLines = parser.unify(fileLines)
    parsedLines = parser.parse(unifiedLines)
    language = parser.read(parsedLines)

    return language

def compile(infile:str, outfile:str, *args, **kwargs) -> None:
    '''
    Compile file in a faster readable file. \n
    ---------
    [in]    File\n
    [out]   OutFile
    '''