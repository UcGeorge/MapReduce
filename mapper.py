from os import name
from threading import Thread as thread
from pathlib import Path
from pprint import pprint

# Stores all results from all threads
total_results = {}

# Cmputes the frequency of all words in each workload


def word_counter(thread_index, workload: list):
    total_results[thread_index] = {}

    for workk in workload:
        wordlist = work[workk].split()

        for word in wordlist:
            if word in total_results[thread_index]:
                total_results[thread_index][word] += 1
            else:
                total_results[thread_index][word] = 1
    pass


work = {}

input_location = Path('inputs/')

for iinput in input_location.rglob('*.txt'):
    work[iinput.stem] = iinput.read_text()

n = int(input('[?] Input N '))

thread_ = {}

for thread_index in range(n):
    thread_[thread_index] = []


def thread_generator():
    index = 0

    while True:

        if index == n:
            index = 0

        yield index
        index += 1


thread_gen = thread_generator()

for w in work:
    thread_[next(thread_gen)].append(w)

for thrd in thread_:
    thread(target=word_counter, args=[thrd, thread_[thrd]]).start()

pprint(total_results)
