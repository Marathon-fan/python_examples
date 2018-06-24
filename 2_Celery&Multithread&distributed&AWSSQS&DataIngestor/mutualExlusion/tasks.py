import threading

counter_buffer = 0
counter_buffer_ = 0

counter_lock = threading.Lock()

COUNTER_MAX = 1000000

def consumer1_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        counter_lock.acquire()
        counter_buffer += 1
        counter_lock.release()


def consumer2_counter():
    global counter_buffer
    for i in range(COUNTER_MAX):
        counter_lock.acquire()
        counter_buffer += 1
        counter_lock.release()

def consumer3_counter():
    global counter_buffer_
    for i in range(COUNTER_MAX):
        counter_buffer_ += 1


def consumer4_counter():
    global counter_buffer_
    for i in range(COUNTER_MAX):
        counter_buffer_ += 1

t1 = threading.Thread(target=consumer1_counter)
t2 = threading.Thread(target=consumer2_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter_buffer)

t3 = threading.Thread(target=consumer3_counter)
t4 = threading.Thread(target=consumer4_counter)

t3.start()
t4.start()

t3.join()
t4.join()

print(counter_buffer_)