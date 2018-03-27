#!/APSshare/anaconda/x86_64/bin/python2.7

# This python script for the GSD-192 uses the c++ data parser (defined by parserPath)
# to generate .mca and .tdc files for ALL .dat files in a folder (defined by datFiles).
#
# author: Russ Woods
#   date: 3/16/2018

import glob
from subprocess import call

# C++ binary file parser
parserPath = '/home/beams/RWOODS/Germanium/GSD-192_GUI/gsd_parse.out'

# Raw data files String (*.dat)
datFiles = '/home/beams/RWOODS/Germanium/gsd_192/data/*.dat'

# Generate a list containing the raw data files (*.dat)
datFileList = glob.glob(datFiles)
print datFileList

# Call c++ parser and provide input and output file names
for count, item in enumerate(datFileList):
    print '...Parsing ' + str(count)
    call([parserPath, item, item.replace('.dat', '')])

print '\nFinished parsing .dat files!\n'

