stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
x_location = stdform.find('x')
caret_location = stdform.find('^')
sig = stdform[0:x_location]
exponent = stdform[caret_location + 1:]

print(f"This number in E notation is {sig}E{exponent}.")