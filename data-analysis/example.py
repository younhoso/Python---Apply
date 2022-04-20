numbers = "1. 2. 3. 4. 5. 6"
number_data = numbers.split(". ")
print(int(number_data[0]) + int(number_data[1]))

full_name = "Kim, Tuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]
print(last_name, first_name)

some_string = "   abc   def  \n gh   ijk lmnop    q  r\n s    "
print(some_string.split())


