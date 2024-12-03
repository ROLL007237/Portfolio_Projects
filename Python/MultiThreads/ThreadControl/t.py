import requests
from time import time
from threading import Thread


def read():
	size = 0
	response = requests.get('https://en.wikipedia.org/wiki/Microsoft_ergonomic_keyboards')
	size += len(response.text)

#### example of classic way
start_time = time()
for _ in range(10):
	read()
end_time = time()
print(end_time - start_time)

start_time = time()

#### example of thread way
all_threads = []
for _ in range(10):
	thread = Thread(target=read)
	all_threads.append(thread)

for thread in all_threads:
	thread.start()

for thread in all_threads:
	thread.join()
end_time = time()
print(end_time - start_time)

