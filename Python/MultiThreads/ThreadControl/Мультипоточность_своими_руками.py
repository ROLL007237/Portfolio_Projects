from threading import Thread, current_thread


all_threads = []


def gavno():
    hueta = 10
    for _ in range(1000):
        hueta += 10
        print(hueta)


def thread_creation(amount):
    global all_threads
    for _ in range(amount):
        all_threads.append(Thread(target=gavno))

    for thread in all_threads:
        thread.start()

    for thread in all_threads:
        thread.join()

thread_creation(2)

