import os
import sys
filename = sys.argv[1]
os.system("pdflatex "+filename)
os.system("pdflatex "+filename)
os.system("bibtex "+filename[:-4])
os.system("pdflatex "+filename)
os.system("open "+filename[:-4]+".pdf")
