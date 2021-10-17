import sys

from linear_search import linear_search
from index_search import index_search, create_index
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, filenames

"""
Run with

$ python -m pytest --durations=0 -v test_searches.py ~/data/berlitz1

"""

rootdir = sys.argv[len(sys.argv) - 1]
print("testing with dir", rootdir)


def dotest(terms, expected, which):
    files = filelist(rootdir)
    terms = words(terms)

    if which == 0:
        linear_docs = linear_search(files, terms)
        # print(filenames(linear_docs))
        names = filenames(linear_docs)
        names.sort()
        expected.sort()	
        #assert filenames(linear_docs) == expected
        assert names == expected, "found "+str(names)+" != expected "+str(expected)
    elif which == 1:
        index = create_index(files)
        index_docs = index_search(files, index, terms)
        # print(filenames(index_docs))
        names = filenames(index_docs)
        names.sort()
        expected.sort()
        #assert filenames(index_docs) == expected
        assert names == expected, "found "+str(names)+" != expected "+str(expected)
    else:
        index = myhtable_create_index(files)
        index_docs = myhtable_index_search(files, index, terms)
        # print(filenames(index_docs))
        names = filenames(index_docs)
        names.sort()
        expected.sort()
        #assert filenames(index_docs) == expected
        assert names == expected, "found "+str(names)+" != expected "+str(expected)


def test_lisbon_linear():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'], which=0)

def test_lisbon_index():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'], which=1)

def test_lisbon_myhtable():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'], which=2)
