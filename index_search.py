from collections import defaultdict  # https://docs.python.org/2/library/collections.html
from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    wordindex = {}
    
    # ITERATE THROUGH LIST OF FILE PATHS
    for loc,x in enumerate(files):
        
        # GET STRING OF TEXT FROM FILE
        filestring = get_text(x)
        
        # GET LIST OF NORMALIZED WORDS FROM STRING
        listfiles = words(filestring)
        
        # GET UNIQUE VALUES FROM LIST
        listfiles = set(listfiles)
        
        # ITERATE THROUGH UNIQUE VALUES
        for word in listfiles:
            
            # IF WORD NOT IN DICT, ADD INDEX OF FILE AS VALUE, ELSE APPEND INDEX OF FILE             
            if word not in wordindex:
                wordindex[word] = {loc}

            else:
                wordindex[word].add(loc)
                
    return wordindex


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """    
    # CREATE EMPTY LIST
    indexlist = []
    
    # ITERATE THROUGH USER INPUT WORDS
    for word in terms:
        
        # CHECK IF USER INPUT WORDS ARE IN INDEX
        if word not in index:
            pass
        
        # GRAB VALUES IF WORDS IN INDEX
        else:
            values = index[word]
            
            # ITERATE THROUGH VALUES AND APPEND THE ELEMENT EACH VALUE REFERS TO IN FILES
            for loc in values:
                indexlist.append(files[loc])                    
    
    # CHECK THAT ARTICLES RETURNED CONTAIN ALL WORDS INPUT                          
    containsall = []
    
    for file in indexlist:

        # ITERATE THROUGH FILE NAMES, IF COUNT OF FILENAME IN LIST MATCHES THE COUNT OF WORDS INPUT, APPEND TO LIST        
        if indexlist.count(file) == len(terms):
            if file not in containsall:
                containsall.append(file)
            else:
                pass
        else:
            pass
    
    return containsall  
