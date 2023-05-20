print("=====if/else statements=====")
a  = True
if a:
    print("I got into the if block")
    print("Indentation is very much required after colon")
print("Out of if/else statements")

#Nested if/else statements
b = True
c = True
if a:
    print("First If block")
    if b:
        print("Second if block")
        if c:
            print("Third if block")
else:
    print("Else block")

# if and else if statements
if type(a) == "boolean":
    print("Boolean")
elif type(a) == "string":
    print("String")
else :
    print("Not a boolean")


print("=====Loops====")
a = [5,6,7,8,9]
for number in a:
    print(number)
