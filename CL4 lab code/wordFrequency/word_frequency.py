
from mrjob. job import MRJob
import re

class WordCount(MRJob):
    def mapper(self, _, Line):
        words = re.findall(r'\w+', Line.lower())
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    WordCount.run()