#!/usr/bin/env python

# Begin colour definitions
redBG = '\x1b[0;37;41m'
redFG = '\x1b[0;31;40m'
greBG = '\x1b[0;37;42m'
greFG = '\x1b[0;32;40m'
yelBG = '\x1b[0;37;43m'
yelFG = '\x1b[0;33;40m'
bluBG = '\x1b[0;37;44m'
bluFG = '\x1b[0;34;40m'
purBG = '\x1b[0;37;45m'
purFG = '\x1b[0;35;40m'
escSQ = '\x1b[0m'
# Define printc function
def printc(c, t):
	print(c + t + escSQ)
# End colour definitions

# Print examples
print('Colour text with Python\n')

print('Text with background colours:\n')
printc(c=redBG, t='Red background')
printc(c=greBG, t='Green background')
printc(c=yelBG, t='Yellow background')
printc(c=bluBG, t='Blue background')
printc(c=purBG, t='Purple background')

print('\nText with foreground colours:\n')
printc(c=redFG, t='Red foreground')
printc(c=greFG, t='Green foreground')
printc(c=yelFG, t='Yellow foreground')
printc(c=bluFG, t='Blue foreground')
printc(c=purFG, t='Purple foreground')
