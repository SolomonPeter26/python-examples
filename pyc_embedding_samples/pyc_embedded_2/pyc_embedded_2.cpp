//------------------------------------------------------------------------------
//           Name: pyc_embedded_2.cpp
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
#include <graminit.h>

void main( void )
{
    Py_Initialize();

	//
    // Get the "string" module and execute its "uppercase" method, which is 
	// stored in its dictionary object. The result will be returned as a
	// pointer to a PyObject.
	//
	// This is the same as the following Python script:
	//
	// import string
	// string.uppercase
	//

    PyObject *pModule     = PyImport_ImportModule( "string" );
    PyObject *pDictionary = PyModule_GetDict( pModule );
    PyObject *pResult     = PyRun_String( "uppercase", eval_input, pDictionary, pDictionary );

	//
	// Convert the resulting PyObject to a native C/C++ type by parsing out its
	// value as a string.
	//

    char *cStr;
    PyArg_Parse( pResult, "s", &cStr );
    cout << cStr << endl;

	//
    // Now, add a new a variable called "x" to the module's namespace and
	// assign it the value of our earlier result.
	//
	// This is the same as the following Python script:
	//
	// x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	//
	// Where "ABCDEFGHIJKLMNOPQRSTUVWXYZ" is the resulting value we got earlier
	// from calling the "uppercase" method of the "string" module.
	//

    PyObject_SetAttrString( pModule, "x", pResult );

	//
	// Now, call the "lower" method of the "string" module on the new "x"
	// variable to make it lower-case and print out the resulting new string.
	//
	// This is the same as the following Python script:
	//
	// print string.lower(x)
	//

    PyRun_String( "print lower(x)", file_input, pDictionary, pDictionary );

	//
	// Finally, release everything by decrementing their reference counts.
	//

	Py_DECREF( pResult );
	Py_DECREF( pDictionary );
    Py_DECREF( pModule );

	Py_Finalize();
}
