import re
import unicodedata

def normalize(text):
    """
    Strip accents from input String.

    [in]     The input string.
    [inType] String.

    [out]     The processed String.
    [outType] String.
    """

    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    # text = text.encode('ascii', 'ignore')
    # text = text.decode("utf-8")

    return str(text)

def textToId(text):
    """
    Convert input text to id.

    [in]     The input string.
    [inType] String.

    [out]     The processed String.
    [outType] String.
    """

    text = normalize(text.lower())
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    
    return text