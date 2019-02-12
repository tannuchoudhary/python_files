print("DATA TYPES : NUMBERS, BOOLEANS, STRINGS, LISTS, TUPLES, DICTIONARIES")
print("1. NUMBERS")
print("INTEGER NUMBERS")
my_int = 20
my_int2 = 40
print( my_int + my_int2 )
'''While using integer values you don't need to put quotation, just simply assign the numbers'''

print("-----------------------------------------------------------------------------------")

print("FLOAT NUMBERS")
my_float = 4.5
my_float2 = 8.9
print(my_float + my_float2)
''' For storing float values, simply write the decimal numbers'''
print("-----------------------------------------------------------------------------------")

print("2. BOOLEANS")
my_boolean = 56<24
my_boolean2 = 12>10
print(my_boolean)
print(my_boolean2)
'''We can also store a Boolean value, as boolean is expressed in either true or false, so it
will return either true or false value, always remember the first alphabet of True and False
 wil always be capital.'''

print("-----------------------------------------------------------------------------------")

print("3. STRINGS")
'''string can be enclosed in either double quotes or single quote, but whichever you use,
just be consistent within a program'''
string = "My name is Tannu Kumari"
string2 = "i am very good girl."
print(string)
print(string2)

print("----------------------------------------------------------------------------------")

print("4. LISTS")
'''A list is a mutable, or changeable, ordered sequence of elements. Each element or value
 that is inside of a list is called an item. Just as strings are defined as characters
  between quotes, lists are defined by having values between square brackets [ ].

  A list of integers looks like this:
[-3, -2, -1, 0, 1, 2, 3]

A list of floats looks like this:
[3.14, 9.23, 111.11, 312.12, 1.05]

A list of strings:
['shark', 'cuttlefish', 'squid', 'mantis shrimp']

If we define our string list as sea_creatures:
sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp'] '''
sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp']
print(sea_creatures)

print("---------------------------------------------------------------------------------")

print("5. TUPLES")
'''
A tuple is used for grouping data. It is an immutable, or unchangeable, ordered sequence of
 elements.Tuples are very similar to lists, but they use parentheses ( ) instead of square
  brackets and because they are immutable their values cannot be modified.
A tuple looks like this:
('blue coral', 'staghorn coral', 'pillar coral')
We can store a tuple in a variable and print it out:
coral = ('blue coral', 'staghorn coral', 'pillar coral')
print(coral)
Ouput
('blue coral', 'staghorn coral', 'pillar coral')
Like in the other data types, Python prints out the tuple just as we had typed it, with
 parentheses containing a sequence of values.
'''
coral = ('blue coral', 'staghorn coral', 'pillar coral')
print(coral)

print("----------------------------------------------------------------------------------")

'''The dictionary is Python’s built-in mapping type. This means that dictionaries map keys
 to values and these key-value pairs are a useful way to store data in Python. A dictionary
  is constructed with curly braces on either side { }.
Typically used to hold data that are related, such as the information contained in an ID, a
 dictionary looks like this:
{'name': 'Sammy', 'animal': 'shark', 'color': 'blue', 'location': 'ocean'}
You will notice that in addition to the curly braces, there are also colons throughout the
dictionary. The words to the left of the colons are the keys. Keys can be made up of any
immutable data type. The keys in the dictionary above are: 'name', 'animal', 'color', 'location'.
The words to the right of the colons are the values. Values can be comprised of any data
 type. The values in the dictionary above are: 'Sammy', 'shark', 'blue', 'ocean'.
Like the other data types, let’s store the dictionary inside a variable, and print it out:
'''

sammy = {'name': 'sammy', 'animal': 'shark', 'color': 'blue', 'location': 'ocean'}
print(sammy)
print(sammy['color'])

'''
This was all about data types in Python
'''