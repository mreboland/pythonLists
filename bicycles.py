# Lists are denoted with []. Lists start at 0 and count up
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)  # Outputs ['trek', 'cannondale', 'redline', 'specialized']

# To access individual items
print(bicycles[0]) # Outputs 'trek'

# You can use string methods from Chapter 2 on this list
print(bicycles[0].title())

# Printing others in the list
print(bicycles[1])
print(bicycles[3])

# Python has a special syntax in that if you us -1 it'll return the last item in the list
print(bicycles[-1])

# To expand, if you use -2, -3 and so on, you'll return the items in the list in reverse order
print(bicycles[-2]) # Outputs 'redline'

# You can use individual items from the list to print messages
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.

friends = ["friendOne", "friendTwo", "friendThree"]
print(friends[0])
print(friends[1])
print(friends[2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

message = f"Hello, {friends[0].title()}, {friends[1].title()}, and {friends[2].title()}!"
print(message)


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

motorcycles = ["triumph", "ktm", "ducati"]

for x in motorcycles:
    newMessage = f"{x.title()} is the best manufacturer!"
    print(newMessage)