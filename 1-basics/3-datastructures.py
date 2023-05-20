print('=====List=====')
# List of Numbers
list = [1,2,3,4]
print(list)
# Lenght of list
print(len(list))

# List of characters
list = ['p','y','t','h','o','n']
print(list)

#Mixed List
list = [1,'a', True]
print(type(list))

#List of List objects
list = [[1,2],[3,4]]
print(len(list[0]))

print([2,1] == [2,1])
#Oreder of elements matters here
print([2,1] == [1,2])

print('=====Sets=====')
#Set of Unique elements
# We use curly brackets
sets = {1,2,2,3,4}
print(sets)
print(type(sets))

sets = {1,1,2,2}
print(sets)
print(len(sets))

#Oreder of elements does not matter here
print({1,2} == {2,1}) #True
print({1,2,3} == {3,2,1,1,1}) #True it is a  set. Dupicates will be removed. It is like {1,2,3} == {3,2,1}
print({1,2} == {2,1,3}) #False
print({1,2} == {4,2,3,1}) #False
print({1,2} == [2,1]) #False


print('=====Tuples=====')
tuples = (1,2,3)
print(type(tuples))
print(len(tuples))
# Oreder of elements matters here
print((1,2) == (1,2)) #True
print((1,2) == (2,1)) #False
# We cannot append or add elements in tuples like in a list and a set.
# We can not modify tuple.
# These are memory efficient. Good for storing lots of little things like x,y coordinates.
# We can store things which are fixed in nature. Like cooridanates, number of days/ months


print('=====Dictionaries=====')
dictionaries = {
    'apple' : 'Red',
    'banana' : 'yellow'
}
print(type(dictionaries)) #<class 'dict'>
print(dictionaries) #{'apple': 'Red', 'banana': 'yellow'}
print(dictionaries['apple']) #Red
# Key has to be unique
#If you repeat the key with a different value then pyhton picks up the last value in the dictionary.

## Sets and Dictionary
# Both are defined with curly braces.
# Sets have unique values and dictionaries have unique keys.
# in both, order does not matter.