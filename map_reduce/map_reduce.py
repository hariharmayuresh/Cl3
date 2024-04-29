
from mrjob. job import MRJob
import re

class CharacterCount (MRJob):
    def mapper(self, _,line):
        for char in line:
            yield char, 1

    def reducer(self, char, counts):
        yield char, sum(counts)

class WordCount(MRJob):
    def mapper(self, _, Line):
        words = re.findall(r'\w+', Line.lower())
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    CharacterCount.run()
    WordCount.run()