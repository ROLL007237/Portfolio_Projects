from HW6 import *

k=t.time()
c=t.time()
data2obj(data)
print(t.time()-c)

c=t.time()
sub_category(messages)
print(t.time()-c)

c=t.time()
mean_msg_size(messages)
print(t.time()-c)
print()
print(t.time()-k)