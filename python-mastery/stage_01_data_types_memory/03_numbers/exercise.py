print(type(10/2))

x = 5
y = x

x = x+1

print(y)

print(2 ** 31)
print(2 ** 1000)
print(2**100)

import sys

print(sys.getsizeof(1))
print(sys.getsizeof(2**4))
print(sys.getsizeof(2**7))
print(sys.getsizeof(2**100))
print(sys.getsizeof(2**1000))

print(sys.getsizeof(-5))
print(sys.getsizeof(5))

print(bin(5)) # 3 bits
print(sys.getsizeof(5)) # 28 bytes

a = 1000000000000

print(bin(a))
print(sys.getsizeof(a))
print(len('0b1110100011010100101001010001000000000000') - 2) # 40 bits so 5 bytes - 2 chunks - 8 bytes + 24 bytes HK is 32 bytes total

print(-9//4)

print(-9%4)