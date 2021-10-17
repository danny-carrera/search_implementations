import os
import re
import string
from pathlib import Path


def filelist(root):
    """
    Given a folder, return a list of file paths. 
    """
    filepath = []

    pathroot = "/" + root
    access = Path(pathroot)
    
    # iterate through directory
    for x in access.iterdir():
        
        # if text file, append to list
        if x.suffix == '.txt':
            filepath.append(x)
        
        # if directory, iterate through
        elif x.is_dir():
    
            x = str(x)
            pathx = "./" + x
            access2 = Path(pathx)
            
            for x in access2.iterdir():
                if x.suffix == '.txt':
                    filepath.append(x)
    
        else:
            pass
        
    return filepath


def get_text(fileName):
    """
    Gets text from a file.
    """
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    return words


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]
