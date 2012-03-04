#------------------------------------------------------------------------------
#           Name: read_from_zip.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to use zipfile to read
#                 from a zipped archive.
#------------------------------------------------------------------------------

import zipfile

myZipFile = zipfile.ZipFile( "test.zip", "r" )

for fileName in myZipFile.namelist():
    data = myZipFile.read(fileName)
    print fileName, len(data), repr(data[:50])

raw_input( '\n\nPress Enter to exit...' )
