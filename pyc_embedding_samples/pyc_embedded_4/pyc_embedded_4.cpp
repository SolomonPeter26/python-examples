//------------------------------------------------------------------------------
//           Name: pyc_embedded_4.cpp
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
    // Create a new namespace dictionary and set the typical built-in values
	// or variables.
	//

    PyObject *pDictionary = PyDict_New();
    PyDict_SetItemString( pDictionary, "__builtins__", PyEval_GetBuiltins() );

	//
	// Create a new variable in the namespace dictionary called "y" and set
	// its value to 5.
	//

    PyDict_SetItemString( pDictionary, "y", PyInt_FromLong(5) );

	//
	// Using our new namespace dictionary to run two python statements.
	// Note how the new variable "y" gets used.
	//

    PyRun_String( "x = 100", file_input, pDictionary, pDictionary );
    PyRun_String( "x = x + y", file_input, pDictionary, pDictionary );

	//
	// Pull the variable "x" from the namespace dictionary and convert the 
	// resulting PyObject to a native C/C++ type by parsing out its value as 
	// an integer.
	//

    PyObject *pResult = PyDict_GetItemString( pDictionary, "x" );

	int nValue;
    PyArg_Parse( pResult, "i", &nValue );
    cout << nValue << endl;

	//
	// Finally, release everything by decrementing their reference counts.
	//

	Py_DECREF( pResult );
    Py_DECREF( pDictionary );

	Py_Finalize();
}
