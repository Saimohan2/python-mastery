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
print(id(original))
print(id(alias)) # same as original
print(id(copy)) # different

print(sys.getrefcount(original)) # guessing 3 actual original, alias pointing, this call

del alias

print(sys.getrefcount(original)) # guessing 2, as alias is now deleted