
# Logic

x = 40

y = 70.30

z = 17.00

# print(x == y)

# print(x > y)

# print(x < y)

#----------------------------------------------

# if (x < y):
#     print(x, "is less than", y)


# if (x < y): print(x, "is less than", y)

#----------------------------------------------

# if(x):
#     print("x has been set")


start = "This variable just needs to be set."

# if(start):
#     print("The Process has started.")
#     if(y > z):
#         print(y, "is bigger than", z)

#----------------------------------------------

# if(x == 20):
#     print("x is equal to 20")

# elif(y == 20):
#     print("y is equal to 20")

# elif(z == 20):
#     print("z is equal to 20")

# else:
#     print("None of the variables equal to 20")

#----------------------------------------------


# if (type(x) == str):
#     print("x is a string")
# elif (type(x) == float):
#     print("x is a float")
# elif (type(x) == int): 
#     print("x is a integer")
# else: 
#     print("I don't know what x is.")

#______________________________________________________________________________________________________________________________________
#----------------------------------------------

username = "CoderFixerUpper12"

if (type(username) == str):
    if(username.isalpha()):
        print("You need at least 1 number in your username to register:", username)
    elif(username.isdigit()):
        print("Your username needs at least 3 letters:", username)
    # elif


