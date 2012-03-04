//------------------------------------------------------------------------------
//           Name: pyc_embedded_python_threads.cpp
//         Author: Kevin Harris
//  Last Modified: 01/19/07
//    Description: This sample demonstrates how to embed Python into a C++ 
//                 application where the Python script spawns a worker thread 
//                 which allows it to run alongside the main application thread. 
//                 While the threads work independently, they can still share 
//                 data by calling into one another to set values.
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
#include <fstream>
#include <string>
using namespace std;

#include <Python.h>

//------------------------------------------------------------------------------
// Extend Python by creating a C/C++ function which will allow Python to SET an 
// int value in the application. 
//------------------------------------------------------------------------------

PyObject* myCppFunction( PyObject* self, PyObject* args )
{
    int nValue;

    if( PyArg_ParseTuple( args, "i", &nValue ) )
    {
        cout << "Python thread - Script called myCppFunction and passed: " << nValue << endl;
    }

    Py_INCREF( Py_None );
    return Py_None;
}

//------------------------------------------------------------------------------
// Define a function which will allow a Python script to set a call-back for 
// the application to use.
//------------------------------------------------------------------------------

PyObject *g_pythonCallback = NULL;

static PyObject* setCallback( PyObject* self, PyObject* args )
{
    PyObject *result = NULL;
    PyObject *temp   = NULL;

    if( PyArg_ParseTuple( args, "O", &temp ) )
    {
        if( !PyCallable_Check( temp ) ) 
        {
            PyErr_SetString( PyExc_TypeError, "parameter must be callable" );
            Py_INCREF( Py_None );
            return Py_None;
        }

        Py_XINCREF( temp );              // Ref the new call-back
        Py_XDECREF( g_pythonCallback );  // Unref the previous call-back
        g_pythonCallback = temp;         // Cache the new call-back
    }

    Py_INCREF( Py_None );
    return Py_None;
}

//------------------------------------------------------------------------------
// Make Python aware of our special C++ functions above.
//------------------------------------------------------------------------------

PyMethodDef g_methodDefinitions[] =
{
    { "myCppFunction", myCppFunction, METH_VARARGS, "Sets an int value" },
    { "setCallback", setCallback, METH_VARARGS, "Sets a call-back function in Python" },
    {NULL, NULL}
};

//-----------------------------------------------------------------------------
// Name: readPythonScript()
// Desc: 
//-----------------------------------------------------------------------------
string *readPythonScript( string fileName )
{
    ifstream pythonFile;

    pythonFile.open( fileName.c_str() );

    if ( !pythonFile.is_open() ) 
    {
        cout << "Cannot open Python script file, \"" << fileName << "\"!" << endl;
        return NULL;
    }
    else
    {
        // Get the length of the file
        pythonFile.seekg( 0, ios::end );
        int nLength = pythonFile.tellg();
        pythonFile.seekg( 0, ios::beg );

        // Allocate  a char buffer for the read.
        char *buffer = new char[nLength];
        memset( buffer, 0, nLength );

        // read data as a block:
        pythonFile.read( buffer, nLength );

        string *scriptString = new string;
        scriptString->assign( buffer );

        delete [] buffer;
        pythonFile.close();

	    return scriptString;
    }
}

//------------------------------------------------------------------------------
// Name: main()
// Desc: Application's main entry point.
//------------------------------------------------------------------------------
void main( void )
{
    //
    // Setup Python to be embedded...
    //

	Py_Initialize();

    //
    // Define our custom module called "extendAndEmbedTest"...
	//

    PyImport_AddModule( "threadTest" );
    Py_InitModule( "threadTest", g_methodDefinitions );

	//
	// Access the "__main__" module and its name-space dictionary.
	//

	PyObject *pMainModule     = PyImport_AddModule( "__main__" );
	PyObject *pMainDictionary = PyModule_GetDict( pMainModule );

    //
    // Exercise embedding by calling a Python script from a C++ application.
    //

    string *pythonScript = readPythonScript( "test_thread.py" );

    if( pythonScript != NULL )
    {
	    PyRun_String( pythonScript->c_str(), Py_file_input, 
                      pMainDictionary, pMainDictionary );

	    delete pythonScript;
    }

    //
    // If the script set the call-back function, call it...
    //

	int arg = 0;
	PyObject *arglist = NULL;
	PyObject *result  = NULL;

	if( g_pythonCallback != NULL )
	{
		for( int i = 0; i < 100; ++i )
		{
			++arg;
			arglist = Py_BuildValue( "(i)", arg );
			result  = PyEval_CallObject( g_pythonCallback, arglist );
			Py_DECREF( arglist );

			if( result != NULL )
				Py_DECREF( result );
		}
	}

    //
    // Cleanup after Python...
    //

	Py_Finalize();
}
