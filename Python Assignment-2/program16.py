from re import match
 
name = raw_input('input: ')
m = match('.+\s.+', name)  #Or '\ b \ w + \ w + \ b'
if m is not None:
    print m.group()
else:
    print 'not match'