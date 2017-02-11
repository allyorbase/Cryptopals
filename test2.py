input_string = input('Please enter a string to be reversed => ')
inter_string = ""
for p in range(len(input_string)):
     inter_string += input_string[-p-1]
print(inter_string)