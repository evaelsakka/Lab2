# Create list1 containing numbers between 1 and 20
list1 = [i for i in range(1, 21)]

# Create a list containing the squares of list1 using list comprehension
squares_list = [i**2 for i in list1]

# Create a list with only the even values in list1 using list comprehension
even_list = [i for i in list1 if i % 2 == 0]

# Print the results
print("list1:", list1)
print("squares_list:", squares_list)
print("even_list:", even_list)
