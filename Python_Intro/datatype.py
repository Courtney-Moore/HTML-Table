#Boolean Values-asses the truth value of something.It has only two values: True or False (always uppercase the T and F)

is_hungry = True
has_freckles = False

#Numbers-Integers(whole numbers), floating point numbers(known as decimal numbers), and complex numbers

age = 35 # storing an int
weight = 160.57 # storing a float

#Strings-literal text

name = "Joe Blue"

#Tuples- a type of dadat tat is immutable ( can not be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)


#List is a type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data. 

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

#Dictionaries is a group of key-value pairs. Dictionary elemnets are indexed by uniquie keys which are used to access values.

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

#If unsure of a value or a variable's data we can use the type fucnction to find out. We can use (len) function to get the length in data types that have a length attribute. 

#There are 3 basic types of numbers in Python. int, float and complex. If you are unsure use the type() to view the object. All python objects have data type methods we can use to convert number types from one to another. 

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

#Python does not have a built in random number generator, use the random module. 