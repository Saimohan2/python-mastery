"""print(len('naive')) # 5, 5 different ords chained together
print(type('data'[1])) # python only has a str type no char type
# a character is the actual letter, code point is the code assigned to it can be retrieved by ord()

import sys, ctypes

print(sys.getsizeof('data'))

raw = ctypes.string_at(id('data'), sys.getsizeof('data'))

print(len(raw))

print(list(raw))

print(len('హైదరాబాద్ ok'))

name = ' Sai'
print(name.strip())
print(name)"""

import sys, ctypes

# 1. Code points (step 1)
s = 'naïve'
print(len(s), [ord(c) for c in s]) # len 5, prinsts ord(code point of each character one by one)
print(type(s[2]), s[2] == chr(239)) # class str, s[2] == chr(239) code point of ï is 239
# Comment: why is there no separate char type, and what does s[2] give you?

# 2. Memory layout (step 2) # understood, but dont think reading and understanding these every number is important
x = ''.join(['p', 'y', 't', 'h', 'o', 'n'])   # runtime-built, NOT a literal
raw = ctypes.string_at(id(x), sys.getsizeof(x))
print(sys.getsizeof(x))
print(int.from_bytes(raw[16:24], 'little'))               # length field
print(int.from_bytes(raw[24:32], 'little', signed=True))  # hash field, before hash()
hash(x)
raw = ctypes.string_at(id(x), sys.getsizeof(x))
print(int.from_bytes(raw[24:32], 'little', signed=True) == hash(x))
print(list(raw[40:]))
# Comment: explain every number printed, using the header fields.

# 3. kind / character width (step 3) # understood, but should calculate sizes and need to have ord memorisation
for t in ['data', 'café', 'cafā', 'cafe\u0C05', 'cafe' + chr(128512)]:
    print(repr(t), len(t), sys.getsizeof(t))
# Comment: state the kind of each string and show the size formula you used.

# 4. Immutability & rebinding (step 4)
a = ''.join(['spa', 'rk']) # 'spark'
b = a
before = id(a)
a += '!'
print(a, b, id(a) == before, a is b) # spark!, spark, false, false
name = '  Sai  '
name.upper()
print(repr(name)) # ' Sai ' discussed already in the chat, performed an operation, but didn't assign to anything, name still holds its original object
# Comment: what does b refer to at the end, and why did the name.upper() line do nothing?

# 5. Interning (step 5)
p = 'order_id'
q = 'order' + '_id'
r = ''.join(['order', '_id'])
print(p is q, p is r, p == r, sys.intern(r) is p) # already discussed, true, false, true, interned during runtime
u = 'IN PROGRESS'
v = ' '.join(['IN', 'PROGRESS'])
print(sys.intern(v) is u) # true
# Comment: explain each result. Why does the last line differ from sys.intern(r) is p?

# 6. Concatenation cost (step 6) # understood the ref points and inplace mutability risk, but there are code parts which we didnt cover like functions
import timeit
def plus(n):
    s = ''
    for _ in range(n):
        keep = s          # second reference: disables the in-place trick
        s += 'x'
    return s
def join(n):
    return ''.join(['x' for _ in range(n)])
for n in [10_000, 20_000, 40_000]:
    t_plus = timeit.timeit(lambda: plus(n), number=3)
    t_join = timeit.timeit(lambda: join(n), number=3)
    print(n, round(t_plus, 4), round(t_join, 4))
# Comment: when n doubles, roughly what happens to each time? Connect it to the
# copy count n(n+1)/2.

# 7. Encoding, light (step 7)
w = 'café'
print(len(w), len(w.encode('utf-8')))
print(w.encode('utf-8').decode('latin-1'))
# Comment: why do the two lengths differ, and what is the third line's output called?

# 8. f-strings (step 8)
rows, rate, table = 1234567, 0.0825, 'orders'
print(f'{rows:,}') # 1,234,567
print(f'{rate:.1%}') # 82.5 - multiplication mistake with 100, otherwise 8.2 is correct, with one decimal place
print(f'{table:>10}|') # |          orders - why not?
print(f'{table:^10}|') # orders          |
print(f'{42:05}') # 0000042
print(f'{rows=}') # rows = 1234567
print(f'{table!r}') # 'orders'
# Comment: break each spec into its parts (fill/align, width, separator, precision, type).
print(f"{"id":>5}|") #   id|
print(f"{7:04}") # 0007