print('=====Arithmetic operators =====')
print(1 + 2)
print(1 * 2)
print(1 / 2)
print(1 - 2)
print(7 % 2)

print('=====Arithmetic operators With Strings =====')
#print(1 + '2') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('Python ' * 2) #Prints Python 2 times. Python Python


print('=====Comparison operators =====')
print(1 == 1);
print(True == True);
print(1 < 1);
print(1 <= 1);
print( 2 > 1)
print( 2 >= 1) 

print(True == 1); #Prints True




print('=====Logical operators <and>,<or>, <not> =====')
print( True and True) #True
print( True and False) #False
print( False and True) #False
print( False and False) #False

print( True or True) #True
print( True or False) #True
print( False or True) #True
print( False or False) #False

print(not True)
print(not False)



print('=====Membership operators <in>, <not in> =====')
print(1 in [1,2,3]) #True
print(10 in [1,2,3]) #False

print(10 not in [1,2,3]) #True
print('cat' in 'My pet cat') #True
