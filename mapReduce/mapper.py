import sys

word_list = list()
for line in sys.stdin:
    fraze, counter = line.strip().split(',')
    word_list = word_list + fraze.strip().split(' ')

for element in word_list:
    print (element+'\n')


