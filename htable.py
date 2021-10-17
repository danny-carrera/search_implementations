"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    
    table = []
    
    for x in range(nbuckets):
        table.append([])
    
    return table
    

def hashcode(o): 
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    
    # IF INTEGER, SET HASH TO INTEGER VALUE
    if isinstance(o, int) == True:
        hash = o
    
    # IF STRING, SET HASH EQUAL TO "RANDOM" SUM OF ORDINAL VALUES OF EACH CHARACTER
    elif isinstance(o, str) == True:
        h = 0
        
        for x in o:
            h = (h*31) + (ord(x))
            
        hash = h
    
    # IF NOT INT NOR STR, SET HASH EQUAL TO NONE
    else:
        hash = None
    
    return hash
        

def htable_put(table, key, value): 
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    
    # DETERMINE WORD'S BUCKET
    h = hashcode(key) 
    bucket = h % len(table)
    
    # CREATE ASSOCIATION BETWEEN KEY AND VALUE
    assoc = (key, value)
    
    # INITIALIZE VARIABLES TO FALSE, IF WORD IS ALREADY IN TABLE, THEN THESE VARIABLE WILL BE CHANGED TO TRUE
    found = False
    here = 0
    
    for loc, x in enumerate(table[bucket]):
        
        if key == x[0]:
            found = True
            here = loc
            
        else:
            pass
        
    # IF WORD ALREADY IN BUCKET, REPLACE WITH NEW ASSOCIATION  
    if found == True:
        table[bucket][here] = assoc
    
    # IF WORD NOT ALREADY IN BUCKET, THEN ADD ASSOCATION TO BUCKET
    else:
        table[bucket].append(assoc)
        

def htable_get(table, key): 
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    
    valuelist = []
    
    for word in key:
                
        # CALCULATE ITS BUCKET
        h = hashcode(word)
        bucket = h % len(table)
        
        # ITERATE THROUGH ASSOCIATIONS IN THAT BUCKET
        for assoc in table[bucket]:

            if assoc[0] == word:
                
                for a in assoc[1]:
                    valuelist.append(a)
            else:
                pass
            
    return valuelist




