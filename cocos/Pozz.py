import sys
#import gi
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk

from DataFromInput import *
#from DataFromWeb import *
from MkTable import *
from Recommended import *

if __name__ == '__main__' :

    max_attrs = 999
    filename = ""
    if len(sys.argv) >= 2 :
        input_data = ReadAttributes(sys.argv[1])
        filename = sys.argv[1]
        if len(sys.argv) == 3:
            max_attrs = int(sys.argv[2])
            print(max_attrs)
        #
        del sys.argv[1]
    else :
        input_data = ReadAttributes()

    tab = Table(input_data, max_attrs)

    l = "Head Concept: "+ tab.h_conc+"\tModifier Concept: "+tab.m_conc
        
    rec = recommended(tab)

    if rec != [] :
        l += '\nRecommended scenario(s) N°:'
        for x in rec :
           l += ' '+str(x)+' '

        f = open(filename, "a")
        s = str(tab.sorted_table[x])
        s = s.replace('[', "")
        s = s.replace(']', "")
        f.write("\nResult : " + s)
        f.close()
    else :  
    	l += '\nNO recommended scenarios!'

    print ("\n\n Result: ",l)

else:

	print ("Unknown error at the very beginning...")