import os

book_freq = {}
for f in os.listdir(os.getcwd()):
    print "#################################"
    print ""
    print f
    print ""
    print "#################################"
    print ""
        
    if (f == 'g.py'):
        continue
    s = open(f,'r').read()
    s = s.split()
    l = len(s)
    freq = {}
    for x in s:
        if x.lower() in freq:
            freq[x.lower()] = freq[x.lower()] + 1
        else:
            freq[x.lower()] = 1
            
    fl = []
    for x in freq:
        freq[x] = float(freq[x]) / l
        fl.append([freq[x],x])
    
    book_freq[f] = freq
    
    fl.sort()
 
    print "#################################"
    
s = "the"
for i in book_freq:
    if (s in book_freq[i]):
        print(i + " " + str(book_freq[i][s]))