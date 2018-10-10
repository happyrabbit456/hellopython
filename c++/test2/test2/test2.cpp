/*
�����¼�->���������¼�����->������

ע�⣺ԭ·����Ŀ��·��Ҫ��˫����������

copy "$(TargetPath)" "$(TargetDir)test2.pyd"
*/

#include <boost/python.hpp>
#include <iostream>
#include <string>

using namespace std;

using namespace boost::python;

int Add(const int x, const int y)
{
	return x + y;
}

int Del(const int x, const int y)
{
	return x - y;
}

class World
{
	public:	
		World(string s):msg(s) {}
		void	set(string s)	{ msg = s; }
		string	greet()	{ return msg; }
		string msg;
};

BOOST_PYTHON_MODULE(test2)
{
	def("Add", Add);
	def("Del", Del);

	class_<World>("World", init<std::string>())
		.def("greet", &World::greet)
		.def("set", &World::set);
}