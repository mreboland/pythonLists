# Avoiding index errors when working with lists
motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3])
# The above will generate an index error as there is no third position in the list (0,1,2)
# If you're not sure of the list length and are looking for the last item, remember to use -1 to get it.
print(motorcycles[-1])
# The only time using -1 will generate an error is when the list is empty.
motorcycles = []
print(motorcycles[-1])
