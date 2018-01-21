

def my_function1():
	print("This is my function!")
	print("a second string.")


def my_function2(str1, str2):
	print(str1)
	print(str2)

#  default argument
def my_function3(name = "Someone", age = "unknown"):
	print("my name is", name, " and my age is", age)

#  keyword argument. use key word: None
def my_function4(name = "Someone", age = "unknown"):
	print("my name is", name, " and my age is", age)

# infinite argument
def print_people(*people):   #  * means an array
    for person in people:
    	print("This person is", person)



my_function1()

my_function2("hello", "function2")


my_function3("Nick",27)

my_function3("Nick")

my_function3()


my_function4(None, 27)

print_people("Nick", "Dan", "Jack", "King")