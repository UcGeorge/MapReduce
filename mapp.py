ENCODING = "utf-8"


def word_counter(thread_index, workload: list, work: dict, m):
    '''Cmputes the frequency of all words in each workload'''

    freq_ = {}

    for i in range(m):
        freq_[i] = {}

    for workk in workload:
        wordlist = work[workk].split()

        for word in wordlist:

            if not str(word).isalnum():
                continue

            int_index = ord(word[0]) % m

            if word in freq_[int_index]:
                freq_[int_index][word] += 1
            else:
                freq_[int_index][word] = 1

    for red_index in freq_:
        text = [f'{word}:{freq_[red_index][word]}' for word in freq_[red_index]]

        with open(f'intermediate-files/mr-{thread_index}-{red_index}', "w", encoding=ENCODING) as intermediate_file:
            intermediate_file.write('\n'.join(text))
