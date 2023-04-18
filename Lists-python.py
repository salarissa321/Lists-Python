

#------------------
#---Lists------
#------------------
#{1} List Items Are Enclosed In Square Brackets
#{2} List Are Orderd, To Use Index to Access Items
#{3} List Are mutable => Add , Edit , Delete
#{4} List Items Is Not Unique
#{5} List can Have Data Types
#-------------------



myAwesomList = ["One" , "Two" , "One", 1, 100.5 , True]

print(myAwesomList) # Whole List
print(myAwesomList[1]) # Two
print(myAwesomList[-1]) # True
print(myAwesomList[-3]) #1

print(myAwesomList[1:4]) # ["Two" , "One" , 1]
print(myAwesomList[:4]) # ['One', 'Two', 'One', 1]
print(myAwesomList[1:]) # ['Two', 'One', 1, 100.5, True]


print(myAwesomList[::1]) # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomList[::2]) # ['One', 'One', 100.5]



print(myAwesomList) # ['One', 'Two', 'One', 1, 100.5, True]
myAwesomList[1] = 2  # ['One', 'Two', '2', 1, 100.5, True]
myAwesomList[-1] =  False # ['One', 'Two', '2', 1, 100.5, False]
myAwesomList[0:3] =  ["A" , "B"] # ['A', 'B', 1, 100.5, False]
print(myAwesomList) # ['A', 'B', 1, 100.5, False]