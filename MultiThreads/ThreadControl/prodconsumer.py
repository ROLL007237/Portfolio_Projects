class OurCoolQueue:
	value = 0

	def __init__(self):
		self.collection = []

	def add(self, element):
		self.collection.append(element)

	def process(self):
		element = self.collection.pop()
		print(element)

	def get_result(self):
		print(self.collection)

from threading import Thread, get_ident
from time import sleep
from queue import Queue

def producer(queue: Queue):
	for index in range(10):
		queue.put(index)

def consumer(queue: Queue):
	while True:
		data = queue.get()
		print(get_ident(), data)
		queue.task_done()


queue = Queue()

print(queue.join())

producer_thread = Thread(target=producer, args=(queue, ))
consumer_thread_1 = Thread(target=consumer, args=(queue, ), daemon=True)
consumer_thread_2 = Thread(target=consumer, args=(queue, ), daemon=True)

producer_thread.start()
consumer_thread_1.start()
consumer_thread_2.start()

producer_thread.join()
queue.join()

