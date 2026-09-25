import sys

data = (1,2,3,4,5)
first, *rest = data
print(first, rest) # first = 1 rest[2,3,4,5]

a = b = [10,20]
a.append(30)
print(b) # [10,20,30] as a and b refer to same address one change can change both

shared = [1,2,3]
ref = shared
print(sys.getrefcount(shared)) #3
del ref #ref-1
print(sys.getrefcount(shared)) #2

dic = {'name': 'Sai', 'age': 29}
print(f"before deleting: {dic}")
del dic['name']
print(f"after deleting: {dic}")

# adding comment to commit