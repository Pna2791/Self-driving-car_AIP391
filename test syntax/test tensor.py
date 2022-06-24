from queue import Queue

A = Queue()

A.put(1)
A.put(1)
A.put(1)
A.put(1)

print((A.get()))
print((A.get()))
print((A.get()))
print(A.empty())
print((A.get()))
print(A.empty())
