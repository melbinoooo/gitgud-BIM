# Function and Arguments Deepdive




#----------------------------------------#
# Part 1: Passing Arguments to a defined Function

def greet(name, message):
    print("Hello", name, ",", message)


greet("Monica", "How was your day?") #Function Call
#"Monica", "How was your day?" - is the Argument to be passed into the defined function.

# Rule is we must only provide an argument to be passed on based on the same number that is stated on the defined function.




#----------------------------------------#
# Part 2: Creating a default argument within a define function

def address(city, country = "Philippines"):
    print("Welcome to the",city + ",",country)

address("Manila")
# Output: Welcome to the Manila, Philippines // Default Argument

address("Paris", "France")
# Output: Welcome to the Paris, France



#----------------------------------------#
# Part 3: Arbitrary Aguments
# In case of that we do not know how many arguments are needed to be passed into the defined function.
# We can use an "*" asterisk before the parameter.


def list_of_names(*name):
    print(name)

list_of_names("Ben", "John", "Trent", "Poy")

