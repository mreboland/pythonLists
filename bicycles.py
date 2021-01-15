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

# To change the value in the list at a specific point set the list item you want to change to a new value
motorcycles[0] = "honda"
print(motorcycles)

# To add an element to this list we use append which puts the new item and the end of list
motorcycles.append("suzuki")
print(motorcycles)

# Building a list from nothing
newMotorcycles = []

newMotorcycles.append("triumph")
newMotorcycles.append("ktm")
newMotorcycles.append("ducati")

print(newMotorcycles)

# You can add an element at any position in a list by using insert() method.
motorcycles = ["triumph", "ktm", "ducati"]

# The 0 tells python to open a space at position 0 and insert the second argument into it. The other items in the list all shift to the right by one position.
motorcycles.insert(0, "honda")
print(motorcycles)

# To remove an item from a list, we use the del statement
motorcycles = ["triumph", "ktm", "ducati"]
print(motorcycles)

# The below will delete the element in the first position "triumph"
del motorcycles[0]
print(motorcycles)

# To remove an item that you want to manipulate afterwards (say removing an active user and moving them to inactive) we use pop() method.
# pop() removes the last item in a list.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# We store the value taken from pop() into a new variable so we can later manipulate it
poppedMotorcycle = motorcycles.pop()
# Suzuki is gone from list
print(motorcycles)
# Suzuki is store in poppedMotorcycle
print(poppedMotorcycle)

# How might this pop() method be useful? Imagine that the motorcycles
# in the list are stored in chronological order according to when we owned
# them. If this is the case, we can use the pop() method to print a statement
# about the last motorcycle we bought:

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}.")


# You can use pop() to remove an item from any position in a list by including its index within the brackets
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# You can remove an item from a list by it's value (useful when you don't know it's position)
# We use the remove() method to facilitate that
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# You can also use remove to work with the value that is being removed
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# Assing the value of ducati to a new variable
tooExpensive = "ducati"
# Use said variable to have ducati removed from the list
motorcycles.remove(tooExpensive)
# print the list to show ducati is gone
print(motorcycles)
# ducati is gone from the list but we can still access it through the variable we saved it too earlier
print(f"\nA {tooExpensive.title()} is too expensive for me.")

# The remove() method only deletes the first iteration of the value specified. If there were two ducatis in the list it will only delete the first one and leave the second one. In order to over come that, you'll need to loop over the list to remove all iterations of it. Loops will be learned in a later lesson.


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guests = ["richard dawkins", "albert einstein", "stephen hawking"]

# Using a loop as i'm too lazy to write out three sentences
for guest in guests:
    message = f"Hello {guest.title()}! I'd like to invite you over for dinner. Would you be interested?"
    print(message)

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.

print(f"Unfortunately, {guests[0].title()} is unable to make the dinner!")

# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.

del guests[0]
guests.insert(0, "muhammad ali")

# • Print a second set of invitation messages, one for each person who is still
# in your list.

for guest in guests:
    message = f"Hello {guest.title()}! I'd like to invite you over for dinner. Would you be interested?"
    print(message)

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger
# dinner table.

print("Great news! I've found a larger table so we can invite more people!")

# • Use insert() to add one new guest to the beginning of your list.

guests.insert(0, "lance armstrong")
# • Use insert() to add one new guest to the middle of your list.

guests.insert(2, "wayne gretzky")

# • Use append() to add one new guest to the end of your list.

guests.append("michael jackson")

# • Print a new set of invitation messages, one for each person in your list.

for guest in guests:
    message = f"Hello {guest.title()}! I'd like to invite you over for dinner. Would you be interested?"
    print(message)
    
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

print("Unfortunately the new table wont arrive in time so i'll only be able to invite two of you...")

# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.

print(guests)

removedGuest = guests.pop()
print(f"Sorry {removedGuest.title()} we don't have enough space so I have to take back the invitation.")

removedGuest = guests.pop()
print(f"Sorry {removedGuest.title()} we don't have enough space so I have to take back the invitation.")

removedGuest = guests.pop()
print(f"Sorry {removedGuest.title()} we don't have enough space so I have to take back the invitation.")

removedGuest = guests.pop()
print(f"Sorry {removedGuest.title()} we don't have enough space so I have to take back the invitation.")

# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.

for guest in guests:
    message = f"Hello {guest.title()}! you are still invited to dinner!"
    print(message)    
    
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

del guests[0]
del guests[0]
print(guests)
