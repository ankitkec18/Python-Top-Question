from re import match
 
word = raw_input('input: ')
m = match('^[bh][aiu]t$', word)
if m is not None:
    print m.group()
else:
    print 'not match'