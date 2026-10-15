import sys

original = [10,20,30] # the main list
alias = original # still points to the main list's address(so the same address)
copy = original[:] # copies the list and creates a new list object in the heap

original.append(40)

print(original) # one extra element
print(alias) # same as original
print(copy) # original without 40

''' alias changed but copy didn't because copy is a separate object not just a refrence to 
original. After the copy was created, original was mutated, alias picked it up because alias
was pointing to the original and alias is not a separate object. alias in namespace holds
the same address as original which points to [10,20,30]
'''
print(id(original)) # prints the address of the object in heap, which is ref'd in namespace
print(id(alias)) # same as original
print(id(copy)) # different

print(sys.getrefcount(original)) # guessing 3 actual original, alias pointing, this call

del alias

print(sys.getrefcount(original)) # guessing 2, as alias is now deleted


# revise

a = [1,2,3]
b = a
c = a[:]

print(id(a))
print(id(b))

print(id(a) == id(b))
print(a is b)

a.append(10)

print(sys.getrefcount(a))

print(a)
print(b)
print(c)

sample = [10000,2]
another = sample
print(sys.getrefcount(sample[0]))
print(sample)
print(f"Sample address: {id(sample)}, another address: {id(another)}")
print(id(sample) == id(another))
print(id(sample[0]))
print(id(another[0]))
print(f"same id? : {id(sample[0]) == id(another[0])}")
print(f"same object? : {sample[0] is another[0]}")

i = sample[0]

print(sys.getrefcount(sample[0]))

p = [20000]

print("Before:", sys.getrefcount(p[0]))

j = p[0]
print("After:", sys.getrefcount(p[0]))

del j
print("After deleting j:", sys.getrefcount(p[0]))

import dis

def test():

    ls = [5000, int("2000")]

    x = ls[0]

    print(x)

dis.dis(test)

print(globals())