//------------------------------------------------------------------------------
//           Name: pyc_embedded_1.cpp
//         Author: Kevin Harris
//  Last Modified: 01/19/07
//    Description: This sample demonstrates one of the many ways that Python 
//                 can be embedded and used within a C/C++ application. 
//                 The sample was inspired by a series of C samples that 
//                 accompanies the book, "Programming Python, 2nd Edition" 
//                 by Mark Lutz.
//
//                 http://www.oreilly.com/catalog/python2/index.html
//
// Note:
//
// To compile this project, you'll need to install Python 2.5. I downloaded and 
// used "python-2.5.msi", which I downloaded from here:
//
// http://www.python.org/download/
//
// Note:
//
// With certain versions of Python, the Debug build may fail to link because it 
// can't find "python25_d.lib". In that case, you'll need to stick with the 
// Release build, or download and build a debug version of the Python library 
// from the source, so you can link it in.
//------------------------------------------------------------------------------

#include <Python.h>

void main( void )
{
    Py_Initialize();

	//
	// Execute a Python script - one line at a time...
	//

	PyRun_SimpleString( "import string" );
	PyRun_SimpleString( "print string.uppercase" );
	PyRun_SimpleString( "x = string.uppercase" );
	PyRun_SimpleString( "print string.lower(x)" ); 

	Py_Finalize();
}
