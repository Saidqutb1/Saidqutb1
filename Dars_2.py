# a = 1
# f = 1
# s = 1
# print(a+f+s)

def to_binary(n):
    return bin(n)[2:]

# Test cases
print(to_binary(1))   # Output: '1'
print(to_binary(5))   # Output: '101'
print(to_binary(11))  # Output: '1011'
