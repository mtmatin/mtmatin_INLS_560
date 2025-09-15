# expressions are basically anything combined 
# orders of operation 
"a=2 : this is not pythonic!"

a = 2
b = 5
c = 1

# Default order of operations
result1 = a + b * c
print("a + b * c =", result1)

# With parenthesis: addition first
result2 = (a + b) * c
print("(a + b) * c =", result2)

# More variations
result3 = a * (b + c)
print("a * (b + c) =", result3)

result4 = (a + b + c)
print("a + b + c) =", result4)