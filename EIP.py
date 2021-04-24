import os
import string


def usage():
	print "Usage : ", sys.argv[0], " <nombre> [string]"
	print "    <nombre> est la taille du buffer à générer."
	print "    [string] chaîne de charactères optionnelle à chercher dans le buffer"
	print ""
	print "    ISi [string] est trouvé, le buffer n'est pas affiché mais juste sa position"
	print "   ou la chaîne de charactères débutedans le buffer. Cette recherche st sensible à la casse."

	sys.exit()


try:
	dummy = int(sys.argv[1])
except:
	usage()

if len(sys.argv) > 3:
	usage()
if len(sys.argv) == 3:
	search = "TRUE"
	search_string = sys.argv[2]
else:
	search = "FALSE"

stop = int(sys.argv[1]) / 3 + 1
patend = int(sys.argv[1])
patrange = range(0, stop, 1)
first = 65
second = 97
third = 0
item = ""