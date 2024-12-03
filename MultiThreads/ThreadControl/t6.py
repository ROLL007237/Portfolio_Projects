from threading import Lock, RLock, Thread, Barrier, Timer, Semaphore, Event, Condition
from time import sleep

event = Event()
event.set()
event.clear()
event.wait()


def hello():

	print('hello')
	Timer(interval=5, function=hello).start()

lock = Lock()
def f(index: int, b: Barrier):
	print(f'thread #{index} is waiting for')
	# b.wait()
	print(f'done {index}')

# barrier = Barrier(2)


def f(index: int, semaphore: Semaphore):
	print(f'before semaphore t #{index}')
	with semaphore:
		print(f'inside {index}')
		sleep(2)
	print(f'out {index}')

semaphore = Semaphore(2)

threads = []
for index in range(4):
	threads.append(Thread(target=f, args=(index, semaphore)))

for thread in threads:
	thread.start()


