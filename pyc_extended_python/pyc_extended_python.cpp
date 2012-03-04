//------------------------------------------------------------------------------
//           Name: pyc_extended_python.cpp
//         Author: Kevin Harris
//  Last Modified: 01/19/07
//    Description: This sample demonstrates how to use Boost.Python library to
//                 extend Python by creating a new Python module called, 
//                 "extended_test". This will allow Python to access and make  
//                 use of C++ functions and classes.
// Note: 
//
// To test your new module, you'll need to either place a copy of the
// "extended_test.pyd" in the "DLLs" directory of your Python installation
// (example: C:\Python25\DLLs), or move this script to be in the same 
// directory as the "extended_test.pyd" so it can be loaded locally.
//
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
using namespace std;

#include <boost/python.hpp>
namespace python = boost::python;

//------------------------------------------------------------------------------
// Define a few simple functions to test Boost.Python with.
//------------------------------------------------------------------------------

int g_someValue = 0;

void returnNothing( void )
{
	cout << "returnNothing() called" << endl;
}

char const* returnString( void )
{
    return "returnString() called";
}

void setValue( int nValue )
{
	g_someValue = nValue;
}

int getValue( void )
{
	return g_someValue;
}

//------------------------------------------------------------------------------
// Define a simple class to test Boost.Python with.
//------------------------------------------------------------------------------

class Player
{
public:

	Player() {}

	Player( std::string name ) 
		: m_name(name) {}

	Player( std::string name, int score ) 
		: m_name(name),
		  m_score(score) {}

	void setName( std::string name ) { m_name = name; }
	std::string getName() { return m_name; }

	void setScore( int score ) { m_score = score; }
	int getScore() { return m_score; }

private:

	std::string m_name;
	int m_score;
};


//------------------------------------------------------------------------------
// Define a new Python module using Boost.Python and then make our functions 
// and class available to Python script.
//------------------------------------------------------------------------------

BOOST_PYTHON_MODULE( extended_test )
{	
    python::def( "returnNothing", returnNothing );
    python::def( "returnString", returnString );
	python::def( "setValue", setValue );
	python::def( "getValue", getValue );

	python::class_<Player>("Player")
		.def( python::init<std::string>() )        // Overloaded constructor version #1
		.def( python::init<std::string, int>() )   // Overloaded constructor version #2
		.def( "setName", &Player::setName )
		.def( "getName", &Player::getName )
		.def( "setScore", &Player::setScore )
		.def( "getScore", &Player::getScore )
		;
}

