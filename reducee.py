ENCODING = "utf-8"


def reducee(red_index, n):
    freq_ = {}
    for map_index in range(n):

        try:
            f = open(
                f"intermediate-files/mr-{map_index}-{red_index}", "r", encoding=ENCODING)
        except:
            print(
                f'intermediate-files/mr-{map_index}-{red_index} does not exist')
            continue

        line_num = 0
        for x in f:
            line = x.split(':')

            try:
                x_freq = int(line[1].replace('\\n', ''))
            except:
                print(
                    f'Mapper file: mr-{map_index}-{red_index};\nLine: {line_num}')
                x_freq = 0

            if line[0] in freq_:
                freq_[line[0]] += x_freq
            else:
                freq_[line[0]] = x_freq
            line_num += 1

    text = [f'{word}: {freq_[word]}' for word in freq_]

    with open(f'out-files/out-{red_index}', "w", encoding=ENCODING) as out_file:
        out_file.write('\n'.join(text))
        pass
    pass
