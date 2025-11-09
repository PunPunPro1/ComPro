sentence = input().strip()
words = sentence.split()
longest = max(words, key=len)
print(longest)
