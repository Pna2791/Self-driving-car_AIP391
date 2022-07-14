def each_file(name):
    file = open(name)
    lines = []
    for line in file:
        e = line[-1]
        words = line[:-1].split()
        line = '0'
        line += ' ' + words[1]
        line += ' ' + words[2]
        line += ' ' + words[3]
        line += ' ' + words[4]
        line += e
        lines.append(line)
    file.close()

    file = open(name, 'w')

    file.writelines(lines)
    file.close()


# each_file('2.txt')
