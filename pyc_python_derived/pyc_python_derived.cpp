//------------------------------------------------------------------------------
//           Name: pyc_python_derived.cpp
//         Author: Kevin Harris
//  Last Modified: 01/19/07
//    Description: This sample demonstrates how a C++ class, exposed to Python 
//                 via the Boost.Python library, can be used to derive a new 
//                 Python class. It then brings the concept full-circle by 
//                 demonstrating how instances of that Python derived class can
//                 be created and used back in the C++ application.
//
//                 This sample is a modified version of a sample by 
//                 Dirk Gerrits
//                 http://www.boost.org/libs/python/test/embedding.cpp
//
//                 Read this to learn more about Boost.Python:
//                 http://www.boost-consulting.com/writing/bpl.html
// Note:
//
// To compile this project, you'll need to install Python 2.5. I downloaded and 
// used "python-2.5.msi", which I downloaded from here:
//
// http://www.python.org/download/
//
// You'll also need the Boost.Python library (v2), which is part of the larger 
// Boost libraries (v1.33.1)
//
// http://www.boost.org/
//
// More information on Boost.Python can be found here:
// http://www.boost.org/libs/python/doc/index.html
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

#include <boost/python.hpp>
namespace python = boost::python;

// An abstract base class...
class Base : public boost::noncopyable
{
public:

	Base() {};
    ~Base() {};

    virtual std::string testMethod() = 0;
};

// A derived class...
class Derived : public Base
{
public:

	Derived() {}
    ~Derived() {}

    std::string testMethod()
    {
        return "testMethod() of a C++ Derived object called!";
    }
};

// Boost.Python wrapper class for Base
struct BaseWrap : public Base
{
    BaseWrap(PyObject* self_) : self(self_) {}

    std::string testMethod()
    {
        return python::call_method<std::string>(self, "testMethod");
    }

    PyObject* self;
};

// Use Boost.Python to pack information concerning the Base class and its 
// wrapper class into a module.
BOOST_PYTHON_MODULE( testDerived )
{
    python::class_<Base, BaseWrap, boost::noncopyable>( "Base" );
}

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

//-----------------------------------------------------------------------------
// Name: main()
// Desc: Application's main entry point.
//-----------------------------------------------------------------------------
void main( void )
{
	//
	// Register the module with the interpreter. It's important to do this 
	// before the call to Py_Initialize(). Note that the function called 
	// "inittestDerived" is automatically declared by the BOOST_PYTHON_MODULE
	// macro, which was declared earlier in this file.
	//

	if( PyImport_AppendInittab( "testDerived", inittestDerived ) == -1 )
		throw runtime_error( "Failed to add \"testDerived\" to the "
		                     "interpreter's built-in modules" );

	// Setup Python to be embedded...
	Py_Initialize();

	//
	// Access the "__main__" module and its name space dictionary.
	//

	python::handle<> hMainModule( python::borrowed( PyImport_AddModule( "__main__" ) ) );
	python::handle<> hMainNamespace( python::borrowed( PyModule_GetDict( hMainModule.get() ) ) );

	//
	// Load and run the Python script as a string.
	//

	string *pythonScript = readPythonScript( "derived.py" );

	if( pythonScript != NULL )
	{
		PyRun_String( pythonScript->c_str(), Py_file_input,
					  hMainNamespace.get(), hMainNamespace.get() );
	}

	delete pythonScript;

	//
	// Extract the raw Python object representing the derived class defined in
	// the "derived.py" script that we just executed.
	//

	python::handle<> hClassPtr( PyRun_String( "PythonDerived", Py_eval_input,
	                                          hMainNamespace.get(), 
                                              hMainNamespace.get()) );

	// Wrap the raw Python object in a Boost.Python object
	python::object PythonDerived( hClassPtr );

	//
	// Creating an instance of our C++ derived class...
	//

	Derived cpp;
	cout << cpp.testMethod() << endl;

	//
	// Creating an instance of our Python derived class...
	//

	python::object pyBase = PythonDerived();
	Base &py = python::extract< Base& >( pyBase );
	cout << py.testMethod() << endl;

	// Cleanup after Python...
	Py_Finalize();
}
