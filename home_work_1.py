from re import findall, IGNORECASE
from operator import itemgetter
from collections import defaultdict

wordcount = defaultdict(int)

file = open('C:\\Users\\ICM\\PycharmProjects\\Lesson_1\\Book.txt')

for vocab in findall(r"[A-Z]+", file.read(), flags=IGNORECASE):
    wordcount[vocab.lower()] += 1

for word, number in sorted(wordcount.items(), key= itemgetter(0), reverse=False):
    print(word, str(number) + " " + "times")
