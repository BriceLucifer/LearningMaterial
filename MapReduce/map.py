# map.py
import sys
from collections import defaultdict

class WordCountMapper():
    def __init__(self):
        self.word_counts = defaultdict(int)
    
    def map(self, line):
        words = line.strip().split()
        for word in words:
            yield(word, 1)

if __name__ == "__main__":
    mapper = WordCountMapper()
    
    for line in sys.stdin:
        for key, value in mapper.map(line):
            print(f"{key}\t{value}")