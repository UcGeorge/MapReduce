from reducee import reducee
from mapp import word_counter
from threading import Thread as thread
from pathlib import Path


# GET N and M
n = int(input('[?] Input N '))  # Number of map threads
m = int(input('[?] Input M '))  # Number of reduce threads

# NOTE: thread_ maps each mapper to their work
thread_ = {}
# NOTE: work stores the indexed inputs
work = {}
map_thread_pool = []
reduce_thread_pool = []

# NOTE: INDEX ALL INPUTS
input_location = Path('inputs/')
for iinput in input_location.rglob('*.txt'):
    work[iinput.stem] = iinput.read_text()

# NOTE: Creates an N number of thread_ elements
for thread_index in range(n):
    thread_[thread_index] = []


def thread_generator():
    '''Generates the next thread index'''
    index = 0
    while True:
        if index == n:
            index = 0
        yield index
        index += 1


thread_gen = thread_generator()

# NOTE: Assigns work to thread
for w in work:
    thread_[next(thread_gen)].append(w)


# Put threads in pool
for thrd in thread_:
    map_thread_pool.append(thread(target=word_counter, args=[
        thrd, thread_[thrd], work, m]))

for red_index in range(m):
    reduce_thread_pool.append(thread(target=reducee, args=[red_index, n]))

# Start all map threads
for thread in map_thread_pool:
    thread.start()

# Wait for all of them to finish
for thread in map_thread_pool:
    thread.join()

# Start all reduce threads
for thread in reduce_thread_pool:
    thread.start()
