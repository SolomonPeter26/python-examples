#------------------------------------------------------------------------------
#           Name: write_files_to_zip.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to use zipfile to write
#                 some files into a zip archive.
#------------------------------------------------------------------------------

import os
import zipfile

# List all files in the current directory
allFileNames = os.listdir( os.curdir )

# Open the zip file for writing, and write some files to it
myZipFile = zipfile.ZipFile( "spam_skit.zip", "w" )

# Write each file present into the new zip archive, except the python script
for fileName in allFileNames:
    (name, ext) = os.path.splitext( fileName )
    if ext != ".py":
        print "Writing... " + fileName
        myZipFile.write( fileName, os.path.basename(fileName), zipfile.ZIP_DEFLATED )

myZipFile.close()

print ""

# Open the file again, to see what's in it
myZipFile = zipfile.ZipFile( "spam_skit.zip", "r" )

for info in myZipFile.infolist():
    print "Reading...", info.filename, info.date_time, info.file_size, info.compress_size

raw_input( '\n\nPress Enter to exit...' )
