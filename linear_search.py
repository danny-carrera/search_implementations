# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    contains = []
    
    # iterate through files
    for x in files:
        
        # get text of file
        filestring = get_text(x)
        
        # normalize text
        listfiles = words(filestring)
        
        # get unique words
        listfiles = set(listfiles)
        
        for word in listfiles:
            if word in terms:
                contains.append(x)
            else:
                pass
                        
    # check that all terms were found          
    containsall = []
    for file in contains:
        
        if contains.count(file) == len(terms):
            if file not in containsall:
                containsall.append(file)
            else:
                pass
        else:
            pass
       
    return containsall
