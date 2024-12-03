import requests
from time import time, sleep
from threading import Thread, Lock, RLock

size = 0
# create 4 threads
# create an array with any data by size 100_000
# make the sum of elements of array by n-th elements
# (by number of thread) e.g. [number_thread::4]
# print sum result inside that function
# thread1 process values by index [0, 4, 8, 12.. 96]
# thread2 process values by index [1, 5, 9, 13.. 97]
# thread3 process values by index [2, 6, 10, 14.. 98]
# thread3 process values by index [3, 7, 11, 15.. 99]
"""
elements 100
6 threads
6 parts
100 elments / 6 = 16

16 16 16 16 16 18
"""

# [0:16]
# [16:32]
# [80:]
# [chunksize:chunksize+chunksize]

def parallel_function(start_from, threads_count, array):
	print(sum(array[start_from::threads_count]))

def main():
	array = range(100_000)
	threads = []
	for index in range(3):
		thread = Thread(target=parallel_function, args=(index, 4, array))
		threads.append(thread)
	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()

main()
#### example of classic way
# start_time = time()
# for _ in range(4):
# 	read()
# end_time = time()
# print(size, end_time - start_time)




start_time = time()
lock = Lock()
#### example of thread way
all_threads = []
for _ in range(4):
	thread = Thread(target=read, args=(array, ))
	all_threads.append(thread)

for thread in all_threads:
	thread.start()

for thread in all_threads:
	thread.join()
end_time = time()
print(size, end_time - start_time)
