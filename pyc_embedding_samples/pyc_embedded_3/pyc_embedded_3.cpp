//------------------------------------------------------------------------------
//           Name: pyc_embedded_3.cpp
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

#include <iostream>
using namespace std;

#include <Python.h>

void main( void )
{
    Py_Initialize();

	//
	// Get the "string" module and retrieve the "uppercase" attribute. 
	// The attribute will be returned as a pointer to a PyObject.
	// Once we have it, we can retrieve its current string value, which 
	// should be "ABCDEFGHIJKLMNOPQRSTUVWXYZ" when parsed.
	//
	// This is the same as the following Python script:
	//
	// import string
	// string.uppercase
	//

    PyObject *pModule        = PyImport_ImportModule( "string" );
    PyObject *pAttrUppercase = PyObject_GetAttrString( pModule, "uppercase" );

	//
	// Convert the resulting PyObject to a native C/C++ type by parsing out its
	// value as a string.
	//

	char *cStr;
	PyArg_Parse( pAttrUppercase, "s", &cStr );
    cout << cStr << endl;

	//
	// From the "string" module, we'll also retrieve the "lower" attribute.
    // Once we have it, we'll call it as a method and parse out the resulting
	// new lower-case string.
	//
	// This is the same as the following Python script:
	//
	// string.lower( "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
	//

    PyObject *pAttrLower = PyObject_GetAttrString( pModule, "lower" );
    PyObject *pArguments = Py_BuildValue( "(s)", cStr );

    PyObject *pResult = PyEval_CallObject( pAttrLower, pArguments );

    PyArg_Parse( pResult, "s", &cStr );
    cout << cStr << endl;

	//
	// Finally, release everything by decrementing their reference counts.
	//

	Py_DECREF( pResult );
	Py_DECREF( pAttrUppercase );
	Py_DECREF( pAttrLower );
	Py_DECREF( pArguments );
    Py_DECREF( pModule );

	Py_Finalize();
}
