"""print(type(10/2))

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

from decimal import Decimal

print(Decimal('0.1') * 3 == Decimal('0.3')) # should be true, these are decimal literals and wont be an overflowing float approximate
print(Decimal(0.1) * 3 == Decimal('0.3')) # should be false, as decimal of 0.1 would be again 0.0999999something, so we dont get an exact 0.3
print(Decimal('10')/Decimal('4')) # 2.5 (if rounded, falls back to 2, as its nearest even number)

from fractions import Fraction

print(Fraction(0.5)) # Fraction(1, 2) goes for exact rounding as 5/10 is exactly divisible and yields to half
print(Fraction(1, 3) + 0.5) # hits an error? # after running it gave me a float
print(Fraction('0.25') * 4 == 1) #true
print(Fraction(0.1))"""

import sys, math
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

x = 10
y = x

print(id(x))
print(id(y))
print(id(x) == id(y))

print(x, y, x is y)

x += 1

print(id(x) == id(y))

print(x, y, x is y)

# although x is changed, y wouldn't change, x is a refrence point that points to address of 10
# when we mutate x, it wont change in place, creates a new int object 11 and rebinds x to that id
# y wouldn't change because, y was created refrering to x's address in the heap before we ever changed x's value
# so y was created and it wouldn't change like it does in arrays.

for n in [0, 1, 2**30 - 1, 2**30, 2**60, 2**100]:
    print(n, sys.getsizeof(n))

# didn't calculate binary, but size jumps when the binary exceeds 30 bits, a chunk size is 32 bits and 2 bits are left for carrying during operations
# so size jumps for every 30 bits, otherwise number of bits by 30 fives you exact chunk size, n chunks * 4 gives exact bytes, bytes + 24 hk bytes gives exact size

print(0.1 + 0.2 == 0.3) # should be false, as decimals with denominator which is not in power of 2 gives approx values than exact
print(math.isclose(0.1 + 0.2, 0.3)) # true, as this is math comparison, it checks whether the result is mathematically close to addition
print(sum([0.1] * 10) == 1.0) # false
print(math.fsum([0.1] * 10) == 1.0) # true, fractional sum

print(7 // 2, -7 // 2) # 3, -4 floor rounds to nearest least multiple, while going negative -8 is closer to -7, so -4 it is and there a rule in python that (a//b)*b+(a%b) == a
print(-7 % 2) # 1 nearest 1 -8 and its one step away from -1 in number line
print(int(-3.5)) # same may be
print(round(2.5), round(3.5)) # half round to nearest even so 2, 4

amounts = ['19.99', '5.01', '0.10']
print(sum(float(a) for a in amounts)) # wouldn't be exact, as float stores approx values for denoms that are not powers of 2 
print(sum(Decimal(a) for a in amounts)) # now exact
print(Decimal('2.345').quantize(Decimal('0.01'))) # default for decimal is round down halfs so 2.34
print(Decimal('2.345').quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)) # round half up to 2 places 2.35

for v in [0.1, 0.25, 0.3, 0.375]:
    print(v, v.as_integer_ratio())

# first one prints large values, 0.25 prints proper 1/4, 0.3 goes for large as denom wont be power of 2, same with 0.375 didnt calculate when calculated it denom was power of 2 proper fraction

print(int('256') is int('256')) # true, 256 is within range -5 to 256
print(int('257') is int('257')) # false