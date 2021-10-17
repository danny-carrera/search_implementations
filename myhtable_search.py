# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words, filelist


def myhtable_create_index(files): # RETURN AN H-TABLE
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    
    # GET TABLE WITH N BUCKETS
    n = 4011
    ntable = htable(n)
    
    
    # ITERATE THROUGH FILE PATHS
    for loc,x in enumerate(files):
        
        # GET STRING OF TEXT FROM FILE
        filestring = get_text(x)
        
        # GET LIST OF NORMALIZED WORDS FROM STRING
        listfiles = words(filestring)
        
        # GET UNIQUE VALUES FROM LIST
        listfiles = set(listfiles)
        
        
        for word in listfiles:
            
            val = []
            val.append(loc)
            
            wordlist = []
            wordlist.append(word)
            
            existing = htable_get(ntable, wordlist)

            vals = val + existing
            
            htable_put(ntable, word, vals)
            
    return ntable 


def myhtable_index_search(files, index, terms): # RETURN LIST OF FILE NAMES WITH TERMS
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    
    htablelist = []
    
    indices = htable_get(index, terms)
    
    indices = set(indices)
    
    for x in indices:
        htablelist.append(files[x])
        
        
    # CHECK THAT ARTICLES RETURNED CONTAIN ALL WORDS INPUT     
    containsall = []
    for file in htablelist:
        
        # ITERATE THROUGH FILE NAMES, IF COUNT OF FILENAME IN LIST MATCHES THE COUNT OF WORDS INPUT, APPEND TO LIST        
        if htablelist.count(file) == len(terms):            
            if file not in containsall:
                containsall.append(file)
                
            else:
                pass
        else:
            pass

    return containsall
    