from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
l = [input() for _ in range(N)]
word_counts = Counter(l)

max_count = max(word_counts.values())
most_common_words = [word for word, count in word_counts.items() if count == max_count]

print(min(most_common_words))
