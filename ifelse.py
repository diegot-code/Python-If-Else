
# Logic

print("Start of Intro to Python Logic")

x = 40

y = 70.30

z = 17.00

# print(x == y)

# print(x > y)

# print(x < y)

#----------------------------------------------

# print(int == type(x))

# print(type(x) == int)


#----------------------------------------------

# if (x < y):
#     print(x, "is less than", y) # good

# if x < y: # the ()'s are not needed, but helpful
#     print(x, "is less than", y) # good

#----------------------------------------------

# if (x < y): print(x, "is less than", y) #good

# if (x > y): print(x, "is less than", y) elif(x==40):print("x is 40") # bad

# if (x > y): print(x, "is less than", y)  else(x==40):print("x is 40") # bad


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

highscore = 190500

# if (type(highscore) == str):
#     print("highscore is a string")
# elif (type(highscore) == float):
#     print("highscore is a float")
# elif (type(highscore) == int): 
#     print("highscore is an integer")
# else: 
#     print("I don't know what highscore is.")

#______________________________________________________________________________________________________________________________________
#----------------------------------------------

username = "CoderFixerUpper12"

# if (type(username) == str):
#     if(username.isspace()):  # check for whitespace
#         print("You need a username containing numbers and letters", username)
#     elif(username.isdigit()): # check if everything in the string is all numbers
#         print("Your username needs at least 3 letters:", username)
#     elif(username.isalpha()): # checks if everything is a letter
#         print("You need at least 1 number in your username to register:", username)
#     elif(username.isidentifier() == False):
#         print("Your username is in the wrong syntax:", username)
#     else:
#         print("Your username", username, "is being registered...")
# else:
#     print("Your Username must be a string:", username)


