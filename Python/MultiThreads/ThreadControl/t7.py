from threading import Event, Condition, Thread
from time import sleep

event = Event()

# event.wait()
# event.clear()
# event.set()
# event.is_set() # get the status of event



def producer():
	for index in range(10):
		print('producer sent event')
		event.set()
		sleep(2)


def consumer(index):
	while True:
		event.wait()
		print(f'got it! {index}')
		event.clear()

Thread(target=producer).start()
Thread(target=consumer, args=(0, )).start()
Thread(target=consumer, args=(1, )).start()



