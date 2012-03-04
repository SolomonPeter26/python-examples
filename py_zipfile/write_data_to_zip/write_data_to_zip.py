#------------------------------------------------------------------------------
#           Name: write_data_to_zip.py
#         Author: Kevin Harris
#  Last Modified: 02/13/04
#    Description: This Python script demonstrates how to use zipfile to write
#                 some raw data into a zip archive.
#------------------------------------------------------------------------------

import os
import time
import zipfile

myZipFile = zipfile.ZipFile( "my_data.zip", "w" )

# Get the current date and time
now = time.localtime( time.time() )[:6]

for fileName in ( "data_file1.txt", "data_file2.txt", "data_file3.txt" ):
    info = zipfile.ZipInfo( fileName )
    info.date_time = now
    info.compress_type = zipfile.ZIP_DEFLATED
    print "Writing... " + fileName
    myZipFile.writestr( info, "my_data, "*100 )

myZipFile.close()

print ""

# Open the file again, to read out the data
myZipFile = zipfile.ZipFile( "my_data.zip", "r" )

for info in myZipFile.infolist():
    print "Reading...", info.filename, info.date_time, info.file_size, info.compress_size

raw_input( '\n\nPress Enter to exit...' )
