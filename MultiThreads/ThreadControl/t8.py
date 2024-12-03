from threading import Condition, Thread, Lock
from time import sleep

condition = Condition()
condition.notify_all()
condition.notify()
condition.wait()

def producer():
	for index in range(10):
		with condition:
			condition.notify_all()
			print('notify all')
		sleep(2)


def consumer(index):
	while True:
		with condition:
			condition.wait()
		print(f'got it! {index}')

Thread(target=producer).start()
Thread(target=consumer, args=(0, )).start()
Thread(target=consumer, args=(1, )).start()



