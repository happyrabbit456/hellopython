#test001.py
def helloworld():
    print("Hello World")

def add(a, b):
    return a+b

def testdict(mydict):
    print(mydict)
    mydict["Age"] = 17
    return mydict

class Person:
    def greet(self, greetstr):
        print(greetstr)
    def say_hello(self, name):
        print("hello", name)
        return name

#print add(5,7)
#a = raw_input("Enter To Continue...")