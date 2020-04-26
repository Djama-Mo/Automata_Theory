import matplotlib.pyplot as plt
import re


def main():

    timing_list1 = []
    counts_list1 = []
    timing_list2 = []
    counts_list2 = []
    timing_list3 = []
    counts_list3 = []

    pattern1 = re.compile(r'^\d*\.\d*$', re.MULTILINE)
    pattern2 = re.compile(r'^\d+$', re.MULTILINE)

    timing1 = get_from_file_regex(pattern1)
    counts1 = get_from_file_regex(pattern2)
    timing2 = get_from_file_smc(pattern1)
    counts2 = get_from_file_smc(pattern2)
    timing3 = get_from_file_ply(pattern1)
    counts3 = get_from_file_ply(pattern2)

    for string in timing1:
        timing_list1.append(float(string.group()))
    for string in counts1:
        counts_list1.append(int(string.group()))
    for string in timing2:
        timing_list2.append(float(string.group()))
    for string in counts2:
        counts_list2.append(int(string.group()))
    for string in timing3:
        timing_list3.append(float(string.group()))
    for string in counts3:
        counts_list3.append(int(string.group()))

    plt.title('RegEx, SMC, PLY')
    plt.xlabel('Time')
    plt.ylabel('Count')
    plt.plot(timing_list1, counts_list1, timing_list2, counts_list2, timing_list3, counts_list3)
    plt.show()


def get_from_file_regex(pattern):
    with open('RegEx_time.txt', 'r') as fh:
        strings = fh.read()
    return re.finditer(pattern, strings)


def get_from_file_smc(pattern):
    with open('/home/djama/Рабочий стол/SMC/SMC_time.txt', 'r') as fh:
        strings = fh.read()
    return re.finditer(pattern, strings)


def get_from_file_ply(pattern):
    with open('PLY_time.txt', 'r') as fh:
        strings = fh.read()
    return re.finditer(pattern, strings)


if __name__ == '__main__':
    main()
