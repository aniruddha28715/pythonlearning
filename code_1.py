# print("Hello world")


# name="Alice"
# age=25
# price= 100.1
# print(f"My name is {name} and I am {age} years old. The price of the product is {price}.")


# assignment operator
# a=b


# age2=age
# print(age2)


#indentifiers
# valid: my_variable, _single_
# invalid: 123, -myvar, $SYS, A1, 


# print(type(name))
# print(type(age))
# print(type(price))


#data types
# int : integer (whole number), positive
# float : floating point number, decimal numbers
# bool : boolean True or False
# str : string 'hello', "world",
# list : list [1,2,3]
# dict : dictionary {'key':value}, key
# tuple : ordered collection of items ()

# none
# a = None
# print(type(a))


#Keywords
# reserved words that have special meanings in python
# cannot be used as variable names


#print sum
# a = 256
# b = 323
# sum = (a+b)
# print(sum)


#type of token
#    (), {}, @, [], #, -=,...


# A, B = 2, 7
# C = A + B
# print(C, A//B, A/B, 2*A+B*3)

#input
# name = input("name:  ")
# age = int(input("age:  "))
# price = float(input("price: "))
# print("My name is ",name, "and I am", age, "years old")


#conditional statements
# if <condition>:
#         Statement1
#     elif <condition>:
#               Statement2
#     else:
#                Statement3

# x = 40
# if x >= 50:
#     print("x is greater than  50")
# elif x == 50:
#     print("x equals to 50")
# else:
#     print("x is less than  50")


# A = int(input("A: "))
# G = input("M/F : ")
# if((A == 1 or A ==2) and G == "M"):
#     print('fess is 100')
# elif(A == 3 or A == 4 or G  == "F"):
#     print('fees are 200')
# elif(A == 5 or G == "M"):
#     print('Fees are 300')
# else:
#     print('no fee')
    
#ternary operator
# score = input("score: ")
# result = "True" if score == 60 else "False"
# print(result)

#clever if 
# age = int(input("age : ") )
# vote = ("yes", "no") [age> 18]
# print(vote)


# str = "Anirudha_Kulakrni"
# print(str[1:9])
# print(str[5:])
# print(str[-3:-1])

#string Function
# str= 'Hello World'
# print(str.endswith("ld"))
# print(str.capitalize())
# print(str.replace( "o","k"))
# print(str.find("H"))
# print(str.count('W'))




#LIST
# list1 = ['a','b','c','d','e']
# print(len(list1))
# print(type(list1))
# print(list1[4][0])
# del list1[2]
# print(list1)

# list2 = [1,2,4,7,9]
# print(max(list2))
# print(min(list2))
# list2.remove(4)
# print(list2)

# list3 = [1,2,3,4,5]
# list4 = [6,7,8,9,10]
# combined = list3 + list4
# print(combined)

# list slicing   
# list5 = [1,2,3,4,5,6,7,8,9]
# print(list5[:3])  #from start to third element
# print(list5[3:])   # from fourth element till the end     
# print(list5[3:8]) # from fourth element till eight element
# list5.append(10)
# print(list5)
# list5.sort(reverse=True)  #list.sort()
# print(list5)
# list5.reverse()
# list5.insert(0,34)
# print(list5)
# list5.remove(1)
# print(list5)
# list5.pop(4)
# print(list5)

#Difference between strings and list
# string is immutable while list is mutable
#mutable means we can change the value of a particular element in a list but cannot do so with a string 

#Tuple