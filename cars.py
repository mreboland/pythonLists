# Sorting a list permanently with the sort() method
cars = ["bmw", "audi", "toyota", "subaru"]
# sort() changes the order of the list permanently. It cannot be reverted back to it's original list. It sorts alphabetically.
cars.sort()
print(cars)

# sort in reverse
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

# If we want to maintain the original list but presend it sorted with use the sorted() function
cars = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# The sorted() function can also use the reverse=True to reverse the sorting.
print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))

# To reverse the original order of a list we use the reverse() method
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

# reverse() doesn't sort alphabetically, just a strait flipping of the list
cars.reverse()
print(cars)

# The change is permanent, however you can re-use the reverse() function to change it back
cars.reverse()
print(cars)

# To find the length of the list we use the len() function
# python counts the list starting with 1 so no issues with off-by-one errors
print(len(cars)) # outputs 4

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.

destinations = ["japan", "vietnam", "france", "new zealand", "spain"]

# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.

print(destinations)

# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.

print(sorted(destinations))

# • Show that your list is still in its original order by printing it.

print(destinations)

# • Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.

print(sorted(destinations, reverse=True))

# • Show that your list is still in its original order by printing it again.

print(destinations)

# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.

destinations.reverse()
print(destinations)

# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.

destinations.reverse()
print(destinations)

# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.

destinations.sort()
print(destinations)

# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

destinations.sort(reverse=True)
print(destinations)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 42), use len() to print a message indicating the number
# of people you are inviting to dinner.

guests = ["richard dawkins", "albert einstein", "stephen hawking"]

# Using a loop as i'm too lazy to write out three sentences
for guest in guests:
    message = f"Hello {guest.title()}! I'd like to invite you over for dinner. Would you be interested? There are currently {len(guests)} of you being invited!"
    print(message)

